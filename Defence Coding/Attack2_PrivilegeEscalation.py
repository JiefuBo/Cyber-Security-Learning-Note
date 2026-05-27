#!/usr/bin/env python3
"""
Attack 2 - Privilege Escalation demonstration target.

This standalone lab intentionally contains a vulnerable role-update endpoint so
the report can demonstrate how a standard user can manipulate a client-supplied
role parameter and become an administrator.
Run only in a local lab environment.
"""

from copy import deepcopy
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse
import html
import secrets
import time


HOST = "127.0.0.1"
PORT = 8081
SESSION_COOKIE = "ATTACK2SESSION"

INITIAL_USERS = {
    "101": {
        "username": "alice",
        "password": "alice123",
        "role": "USER",
        "email": "alice@student.local",
    },
    "900": {
        "username": "admin",
        "password": "admin123",
        "role": "ADMIN",
        "email": "admin@student.local",
    },
}

USERS = deepcopy(INITIAL_USERS)
SESSIONS = {}
EVENTS = []


def now_text() -> str:
    return time.strftime("%Y-%m-%d %H:%M:%S")


def reset_state() -> None:
    global USERS, SESSIONS, EVENTS
    USERS = deepcopy(INITIAL_USERS)
    SESSIONS = {}
    EVENTS = []


def log_event(message: str) -> None:
    line = f"{now_text()} {message}"
    EVENTS.append(line)
    print(line)


def username_to_id() -> dict[str, str]:
    return {user["username"]: user_id for user_id, user in USERS.items()}


def parse_cookies(header: str) -> dict[str, str]:
    cookies = {}
    for part in header.split(";"):
        if "=" in part:
            key, value = part.strip().split("=", 1)
            cookies[key] = value
    return cookies


def make_session(user_id: str) -> str:
    token = secrets.token_urlsafe(24)
    SESSIONS[token] = {"user_id": user_id, "created_at": time.time()}
    return token


class Attack2Target(BaseHTTPRequestHandler):
    server_version = "Attack2PrivilegeEscalation/1.0"

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path == "/":
            return self.home()
        if parsed.path == "/login":
            return self.login_form()
        if parsed.path == "/logout":
            return self.logout()
        if parsed.path == "/reset":
            return self.reset_lab()
        if parsed.path == "/admin":
            return self.admin_page()
        if parsed.path == "/evidence":
            return self.evidence_page()
        self.send_error_page(HTTPStatus.NOT_FOUND, "Page not found", "The requested page does not exist.")

    def do_POST(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path == "/login":
            return self.login()
        if parsed.path == "/vulnerable/account/update":
            return self.vulnerable_update_role()
        if parsed.path == "/secure/account/update":
            return self.secure_update_role()
        self.send_error_page(HTTPStatus.NOT_FOUND, "Action not found", "The requested action does not exist.")

    def read_form(self) -> dict[str, str]:
        length = int(self.headers.get("Content-Length", "0"))
        raw = self.rfile.read(length).decode("utf-8")
        return {key: values[0] for key, values in parse_qs(raw).items()}

    def current_user(self) -> tuple[str | None, dict | None]:
        cookies = parse_cookies(self.headers.get("Cookie", ""))
        token = cookies.get(SESSION_COOKIE)
        session = SESSIONS.get(token or "")
        if not session:
            return None, None
        user_id = session["user_id"]
        return user_id, USERS.get(user_id)

    def require_login(self) -> tuple[str | None, dict | None]:
        user_id, user = self.current_user()
        if not user:
            self.redirect("/login")
            return None, None
        return user_id, user

    def login_form(self, error: str = "") -> None:
        _, user = self.current_user()
        if user:
            return self.redirect("/")
        alert = f'<div class="alert">{html.escape(error)}</div>' if error else ""
        self.send_html(
            page(
                "Login",
                f"""
                <section class="login-layout">
                  <div class="login-panel">
                    <p class="eyebrow">Attack 2 Lab</p>
                    <h1>Privilege Escalation Demo</h1>
                    <p class="muted">Sign in as a standard user, then modify the role parameter to become admin.</p>
                    {alert}
                    <form method="post" action="/login" class="stack">
                      <label>Username <input name="username" value="alice" autocomplete="username"></label>
                      <label>Password <input name="password" value="alice123" type="password" autocomplete="current-password"></label>
                      <button>Sign in</button>
                    </form>
                    <a class="text-link" href="/reset">Reset lab state</a>
                  </div>
                  <aside class="panel">
                    <h2>Demo accounts</h2>
                    <div class="account-row"><strong>alice</strong><span>alice123</span><small>USER</small></div>
                    <div class="account-row"><strong>admin</strong><span>admin123</span><small>ADMIN</small></div>
                  </aside>
                </section>
                """,
                None,
            )
        )

    def login(self) -> None:
        form = self.read_form()
        username = form.get("username", "").strip()
        password = form.get("password", "")
        user_id = username_to_id().get(username)
        if not user_id or USERS[user_id]["password"] != password:
            log_event(f"FAILED_LOGIN username={username}")
            return self.login_form("用户名或密码有误")
        token = make_session(user_id)
        log_event(f"LOGIN username={username} role={USERS[user_id]['role']}")
        self.send_response(HTTPStatus.SEE_OTHER)
        self.send_header("Location", "/")
        self.send_header("Set-Cookie", f"{SESSION_COOKIE}={token}; Path=/; HttpOnly; SameSite=Strict")
        self.end_headers()

    def logout(self) -> None:
        cookies = parse_cookies(self.headers.get("Cookie", ""))
        token = cookies.get(SESSION_COOKIE)
        if token:
            SESSIONS.pop(token, None)
        self.send_response(HTTPStatus.SEE_OTHER)
        self.send_header("Location", "/login")
        self.send_header("Set-Cookie", f"{SESSION_COOKIE}=deleted; Path=/; Max-Age=0; HttpOnly; SameSite=Strict")
        self.end_headers()

    def reset_lab(self) -> None:
        reset_state()
        self.send_response(HTTPStatus.SEE_OTHER)
        self.send_header("Location", "/login")
        self.send_header("Set-Cookie", f"{SESSION_COOKIE}=deleted; Path=/; Max-Age=0; HttpOnly; SameSite=Strict")
        self.end_headers()

    def home(self) -> None:
        user_id, user = self.require_login()
        if not user:
            return
        self.send_html(
            page(
                "Attack 2 Dashboard",
                f"""
                <section class="hero">
                  <div>
                    <p class="eyebrow">Offensive Analysis</p>
                    <h1>Attack 2 - Privilege Escalation</h1>
                    <p class="muted">Current user: {html.escape(user['username'])} | User ID: {html.escape(user_id)} | Role: <strong>{html.escape(user['role'])}</strong></p>
                  </div>
                  <a class="button secondary" href="/logout">Logout</a>
                </section>

                <section class="grid">
                  <article class="panel">
                    <h2>Figure 4 - Original HTTP request</h2>
                    <p class="muted">This simulates a normal account update request sent by a standard user.</p>
                    <pre>POST /vulnerable/account/update
Content-Type: application/x-www-form-urlencoded

user_id={html.escape(user_id)}&email={html.escape(user['email'])}&role=USER</pre>
                    <form method="post" action="/vulnerable/account/update" class="stack">
                      <input type="hidden" name="user_id" value="{html.escape(user_id)}">
                      <label>Email <input name="email" value="{html.escape(user['email'])}"></label>
                      <label>Role parameter <input name="role" value="USER"></label>
                      <button>Send original request</button>
                    </form>
                  </article>

                  <article class="panel danger-panel">
                    <h2>Figure 5 - Manipulated request</h2>
                    <p class="muted">The attacker changes the client-supplied role value before resending the request.</p>
                    <pre>POST /vulnerable/account/update
Content-Type: application/x-www-form-urlencoded

user_id={html.escape(user_id)}&email={html.escape(user['email'])}&role=ADMIN</pre>
                    <form method="post" action="/vulnerable/account/update" class="stack">
                      <input type="hidden" name="user_id" value="{html.escape(user_id)}">
                      <label>Email <input name="email" value="{html.escape(user['email'])}"></label>
                      <label>Role parameter <input name="role" value="ADMIN"></label>
                      <button class="danger">Send manipulated request</button>
                    </form>
                  </article>
                </section>

                <section class="panel">
                  <h2>Figure 6 - Administrator access check</h2>
                  <p class="muted">After sending the manipulated request, open the admin page to confirm whether escalation succeeded.</p>
                  <div class="actions">
                    <a class="button" href="/admin">Open admin dashboard</a>
                    <a class="button secondary" href="/evidence">View request evidence</a>
                  </div>
                </section>

                <section class="panel">
                  <h2>Defended comparison</h2>
                  <p class="muted">The secure endpoint ignores ordinary user attempts to change role values.</p>
                  <form method="post" action="/secure/account/update" class="stack narrow">
                    <input type="hidden" name="user_id" value="{html.escape(user_id)}">
                    <input type="hidden" name="email" value="{html.escape(user['email'])}">
                    <label>Attempted role <input name="role" value="ADMIN"></label>
                    <button class="secondary">Try secure update</button>
                  </form>
                </section>
                """,
                user,
            )
        )

    def vulnerable_update_role(self) -> None:
        user_id, user = self.require_login()
        if not user:
            return
        form = self.read_form()
        requested_user_id = form.get("user_id", user_id)
        requested_role = form.get("role", user["role"]).upper()
        requested_email = form.get("email", user["email"]).strip()

        if requested_user_id in USERS:
            USERS[requested_user_id]["email"] = requested_email or USERS[requested_user_id]["email"]
            USERS[requested_user_id]["role"] = requested_role
            log_event(
                f"VULNERABLE_UPDATE actor={user['username']} target_user_id={requested_user_id} role={requested_role}"
            )

        self.send_html(
            page(
                "Vulnerable Update Result",
                f"""
                <section class="result success">
                  <p class="eyebrow">Vulnerable endpoint accepted request</p>
                  <h1>Role value processed by server</h1>
                  <p>The server trusted the client-supplied <code>role</code> parameter.</p>
                  <pre>updatedUserId={html.escape(requested_user_id)}
newRole={html.escape(USERS.get(requested_user_id, {}).get('role', 'UNKNOWN'))}</pre>
                  <div class="actions">
                    <a class="button" href="/admin">Open admin dashboard</a>
                    <a class="button secondary" href="/">Back to attack page</a>
                  </div>
                </section>
                """,
                USERS.get(user_id),
            )
        )

    def secure_update_role(self) -> None:
        user_id, user = self.require_login()
        if not user:
            return
        form = self.read_form()
        requested_role = form.get("role", "").upper()
        if user["role"] != "ADMIN":
            log_event(
                f"SECURE_UPDATE_BLOCKED actor={user['username']} attempted_role={requested_role}"
            )
            return self.send_html(
                page(
                    "Secure Update Blocked",
                    """
                    <section class="result blocked">
                      <p class="eyebrow">Defended endpoint blocked request</p>
                      <h1>403 Forbidden</h1>
                      <p>The server checked the authenticated user's role before allowing a role update.</p>
                      <a class="button" href="/">Back to attack page</a>
                    </section>
                    """,
                    user,
                ),
                HTTPStatus.FORBIDDEN,
            )

        requested_user_id = form.get("user_id", user_id)
        if requested_user_id in USERS and requested_role in {"USER", "ADMIN"}:
            USERS[requested_user_id]["role"] = requested_role
            log_event(
                f"SECURE_UPDATE_ALLOWED actor={user['username']} target_user_id={requested_user_id} role={requested_role}"
            )
        self.redirect("/")

    def admin_page(self) -> None:
        _, user = self.require_login()
        if not user:
            return
        if user["role"] != "ADMIN":
            log_event(f"ADMIN_ACCESS_DENIED username={user['username']} role={user['role']}")
            return self.send_html(
                page(
                    "Admin Access Denied",
                    """
                    <section class="result blocked">
                      <p class="eyebrow">Admin dashboard</p>
                      <h1>403 Forbidden</h1>
                      <p>This page requires the ADMIN role.</p>
                      <a class="button" href="/">Back to attack page</a>
                    </section>
                    """,
                    user,
                ),
                HTTPStatus.FORBIDDEN,
            )

        self.send_html(
            page(
                "Admin Dashboard",
                f"""
                <section class="result success">
                  <p class="eyebrow">Figure 6 - Successful administrator access</p>
                  <h1>Admin dashboard unlocked</h1>
                  <p>The current account is now treated as <strong>ADMIN</strong>.</p>
                </section>
                <section class="grid">
                  <article class="panel"><h2>User management</h2><p class="muted">Create, delete, and modify user accounts.</p></article>
                  <article class="panel"><h2>Restricted settings</h2><p class="muted">Change application security settings.</p></article>
                  <article class="panel"><h2>Audit records</h2><p class="muted">Review sensitive operational logs.</p></article>
                </section>
                <section class="panel">
                  <h2>Current users</h2>
                  {users_table()}
                </section>
                """,
                user,
            )
        )

    def evidence_page(self) -> None:
        _, user = self.require_login()
        if not user:
            return
        body = "\n".join(EVENTS) or "No events yet."
        self.send_html(
            page(
                "Request Evidence",
                f"""
                <section class="panel">
                  <p class="eyebrow">Evidence log</p>
                  <h1>Request and role-change evidence</h1>
                  <pre>{html.escape(body)}</pre>
                  <a class="button" href="/">Back to attack page</a>
                </section>
                """,
                user,
            )
        )

    def send_error_page(self, status: HTTPStatus, title: str, message: str) -> None:
        _, user = self.current_user()
        self.send_html(
            page(
                title,
                f"""
                <section class="result blocked">
                  <p class="eyebrow">{status.value} {html.escape(status.phrase)}</p>
                  <h1>{html.escape(title)}</h1>
                  <p>{html.escape(message)}</p>
                  <a class="button" href="/">Back home</a>
                </section>
                """,
                user,
            ),
            status,
        )

    def redirect(self, location: str) -> None:
        self.send_response(HTTPStatus.SEE_OTHER)
        self.send_header("Location", location)
        self.end_headers()

    def send_html(self, body: str, status: HTTPStatus = HTTPStatus.OK) -> None:
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(body.encode("utf-8"))

    def log_message(self, fmt: str, *args) -> None:
        print("%s - %s" % (self.address_string(), fmt % args))


def users_table() -> str:
    rows = []
    for user_id, user in USERS.items():
        rows.append(
            f"""
            <tr>
              <td>{html.escape(user_id)}</td>
              <td>{html.escape(user['username'])}</td>
              <td>{html.escape(user['email'])}</td>
              <td><strong>{html.escape(user['role'])}</strong></td>
            </tr>
            """
        )
    return f"""
    <table>
      <thead><tr><th>User ID</th><th>Username</th><th>Email</th><th>Role</th></tr></thead>
      <tbody>{''.join(rows)}</tbody>
    </table>
    """


def page(title: str, content: str, user: dict | None) -> str:
    nav = ""
    watermark = ""
    if user:
        watermark = f"<div class=\"watermark\">{html.escape(user['username'])}</div>"
        nav = f"""
        <header class="topbar">
          <a class="brand" href="/">Attack 2 Lab</a>
          <nav>
            <a href="/">Attack page</a>
            <a href="/admin">Admin</a>
            <a href="/evidence">Evidence</a>
            <a href="/logout">Logout</a>
          </nav>
        </header>
        """
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <style>
    :root {{
      --ink: #18212b;
      --muted: #647284;
      --line: #d8e1ea;
      --panel: #ffffff;
      --soft: #f4f7f9;
      --accent: #0f766e;
      --accent-dark: #115e59;
      --danger: #b42318;
      --danger-soft: #fff1f0;
      --success-soft: #eefbf4;
    }}
    * {{ box-sizing: border-box; }}
    body {{ margin: 0; font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; color: var(--ink); background: var(--soft); line-height: 1.5; }}
    main {{ width: min(1160px, calc(100% - 2rem)); margin: 1rem auto 3rem; position: relative; z-index: 1; }}
    h1, h2 {{ margin: 0; line-height: 1.15; letter-spacing: 0; }}
    h1 {{ font-size: 2rem; }}
    h2 {{ font-size: 1.12rem; }}
    a {{ color: var(--accent-dark); text-decoration: none; font-weight: 800; }}
    input {{ width: 100%; border: 1px solid var(--line); border-radius: 6px; padding: .65rem .7rem; font: inherit; }}
    label {{ display: grid; gap: .35rem; font-weight: 800; font-size: .9rem; }}
    button, .button {{ display: inline-flex; align-items: center; justify-content: center; border: 1px solid var(--accent); background: var(--accent); color: white; padding: .68rem .9rem; border-radius: 6px; font: inherit; font-weight: 900; cursor: pointer; min-height: 42px; }}
    button:hover, .button:hover {{ background: var(--accent-dark); color: white; }}
    .secondary {{ background: white; color: var(--accent-dark); }}
    .danger {{ border-color: var(--danger); background: var(--danger); color: white; }}
    .topbar {{ display: flex; justify-content: space-between; align-items: center; gap: 1rem; padding: .9rem max(1rem, calc((100vw - 1160px) / 2)); background: white; border-bottom: 1px solid var(--line); position: sticky; top: 0; z-index: 2; }}
    .brand {{ color: var(--ink); font-weight: 900; }}
    nav {{ display: flex; gap: .85rem; flex-wrap: wrap; }}
    nav a {{ color: var(--muted); }}
    .watermark {{ position: fixed; inset: 0; display: grid; place-items: center; pointer-events: none; color: rgba(24, 33, 43, .055); font-size: clamp(4rem, 18vw, 13rem); font-weight: 900; text-transform: uppercase; transform: rotate(-22deg); white-space: nowrap; z-index: 0; }}
    .hero, .panel, .result, .login-panel {{ background: var(--panel); border: 1px solid var(--line); border-radius: 8px; padding: 1rem; }}
    .hero {{ display: flex; justify-content: space-between; gap: 1rem; align-items: center; margin-bottom: 1rem; }}
    .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1rem; margin: 1rem 0; }}
    .stack {{ display: grid; gap: .85rem; margin-top: 1rem; }}
    .narrow {{ max-width: 420px; }}
    .muted {{ color: var(--muted); }}
    .eyebrow {{ margin: 0 0 .35rem; color: var(--accent-dark); font-size: .8rem; text-transform: uppercase; font-weight: 900; letter-spacing: .08em; }}
    pre {{ white-space: pre-wrap; overflow: auto; background: #17202b; color: #f8fafc; border-radius: 8px; padding: 1rem; }}
    code {{ background: #edf2f7; padding: .08rem .28rem; border-radius: 4px; }}
    .danger-panel {{ background: var(--danger-soft); border-color: #ffc9c2; }}
    .success {{ background: var(--success-soft); border-color: #b9ebce; }}
    .blocked {{ background: var(--danger-soft); border-color: #ffc9c2; }}
    .actions {{ display: flex; gap: .75rem; flex-wrap: wrap; margin-top: 1rem; }}
    .login-layout {{ width: min(920px, 100%); min-height: 100vh; display: grid; grid-template-columns: minmax(300px, 1fr) 320px; gap: 1rem; align-items: center; margin: 0 auto; padding: 1rem; }}
    .account-row {{ display: grid; grid-template-columns: 1fr 1fr; gap: .2rem .75rem; border-top: 1px solid var(--line); padding: .75rem 0; }}
    .account-row small {{ grid-column: 1 / -1; color: var(--muted); }}
    .alert {{ border: 1px solid #f5b5ae; background: #fff4f2; color: var(--danger); border-radius: 6px; padding: .72rem .8rem; font-weight: 900; margin-top: 1rem; }}
    .text-link {{ display: inline-block; margin-top: 1rem; }}
    table {{ width: 100%; border-collapse: collapse; min-width: 600px; }}
    th, td {{ text-align: left; border-bottom: 1px solid var(--line); padding: .75rem; }}
    th {{ color: var(--muted); font-size: .82rem; text-transform: uppercase; }}
    @media (max-width: 760px) {{
      .login-layout {{ grid-template-columns: 1fr; }}
      .hero, .topbar {{ align-items: flex-start; flex-direction: column; }}
      h1 {{ font-size: 1.55rem; }}
    }}
  </style>
</head>
<body>
  {watermark}
  {nav}
  <main>{content}</main>
</body>
</html>"""


def main() -> None:
    server = ThreadingHTTPServer((HOST, PORT), Attack2Target)
    print(f"Attack 2 privilege escalation lab running at http://{HOST}:{PORT}")
    print("Accounts: alice/alice123 role=USER, admin/admin123 role=ADMIN")
    server.serve_forever()


if __name__ == "__main__":
    main()
