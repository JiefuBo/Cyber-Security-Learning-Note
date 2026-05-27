#!/usr/bin/env python3
"""
Broken Access Control target machine for Defence1-4 demonstrations.

This local lab now behaves like a small shopping system. It keeps the original
vulnerable and defended routes, then adds customer, manager, and administrator
business pages so access-control behaviour can be demonstrated through a more
realistic workflow.
"""

from copy import deepcopy
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse
import html
import secrets
import time


HOST = "127.0.0.1"
PORT = 8080
SESSION_TIMEOUT_SECONDS = 5 * 60

INITIAL_USERS = {
    "101": {
        "username": "alice",
        "password": "alice123",
        "email": "alice@student.local",
        "role": "CUSTOMER",
        "account": "Personal learning account",
        "preferences": "Email alerts enabled",
    },
    "102": {
        "username": "bob",
        "password": "bob123",
        "email": "bob@student.local",
        "role": "CUSTOMER",
        "account": "Assessment testing account",
        "preferences": "SMS alerts enabled",
    },
    "500": {
        "username": "manager",
        "password": "manager123",
        "email": "manager@student.local",
        "role": "MANAGER",
        "account": "Order operations account",
        "preferences": "Daily order digest enabled",
    },
    "900": {
        "username": "admin",
        "password": "admin123",
        "email": "admin@student.local",
        "role": "ADMIN",
        "account": "Administration account",
        "preferences": "Audit digest enabled",
    },
}

INITIAL_PRODUCTS = {
    "P100": {
        "name": "Wireless Keyboard",
        "description": "Compact keyboard for study and lab work.",
        "price": 49.00,
        "stock": 12,
    },
    "P200": {
        "name": "USB-C Security Key",
        "description": "Hardware token for MFA demonstrations.",
        "price": 39.00,
        "stock": 8,
    },
    "P300": {
        "name": "Network Cable Pack",
        "description": "Three Cat6 cables for home lab builds.",
        "price": 18.50,
        "stock": 20,
    },
    "P400": {
        "name": "Privacy Screen",
        "description": "Laptop privacy filter for shared spaces.",
        "price": 64.00,
        "stock": 5,
    },
}

USERS = deepcopy(INITIAL_USERS)
PRODUCTS = deepcopy(INITIAL_PRODUCTS)
ORDERS = []
SESSIONS = {}
SECURITY_LOGS = []
LOGIN_LOGS = []
NEXT_USER_ID = 1000
NEXT_ORDER_NUMBER = 1001

ROLE_LABELS = {
    "CUSTOMER": "Customer",
    "MANAGER": "Manager",
    "ADMIN": "Administrator",
}


def now() -> int:
    return int(time.time())


def timestamp() -> str:
    return time.strftime("%Y-%m-%d %H:%M:%S")


def username_to_id() -> dict[str, str]:
    return {user["username"]: user_id for user_id, user in USERS.items()}


def money(value: float) -> str:
    return f"${value:.2f}"


def log_security(event: str) -> None:
    line = f"{timestamp()} WARNING {event}"
    SECURITY_LOGS.append(line)
    print(line)


def log_login(username: str, success: bool, detail: str) -> None:
    LOGIN_LOGS.append(
        {
            "time": timestamp(),
            "username": username,
            "success": success,
            "detail": detail,
        }
    )


def make_session(user_id: str) -> str:
    token = secrets.token_urlsafe(24)
    SESSIONS[token] = {
        "user_id": user_id,
        "created_at": now(),
        "last_seen": now(),
    }
    return token


def parse_cookies(header: str) -> dict[str, str]:
    cookies = {}
    for part in header.split(";"):
        if "=" in part:
            key, value = part.strip().split("=", 1)
            cookies[key] = value
    return cookies


def role_home_path(user: dict) -> str:
    if user["role"] == "ADMIN":
        return "/admin"
    if user["role"] == "MANAGER":
        return "/manager"
    return "/user"


def public_profile(user_id: str, user: dict) -> dict:
    return {
        "userId": user_id,
        "username": user["username"],
        "email": user["email"],
        "account": user["account"],
        "preferences": user["preferences"],
        "role": user["role"],
    }


def order_total(order: dict) -> float:
    return sum(item["price"] * item["quantity"] for item in order["items"])


def reset_state() -> None:
    global USERS, PRODUCTS, ORDERS, SESSIONS, SECURITY_LOGS, LOGIN_LOGS, NEXT_USER_ID
    global NEXT_ORDER_NUMBER
    USERS = deepcopy(INITIAL_USERS)
    PRODUCTS = deepcopy(INITIAL_PRODUCTS)
    ORDERS = []
    SESSIONS = {}
    SECURITY_LOGS = []
    LOGIN_LOGS = []
    NEXT_USER_ID = 1000
    NEXT_ORDER_NUMBER = 1001


class DefenceTarget(BaseHTTPRequestHandler):
    server_version = "DefenceShopTarget/2.0"

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        routes = {
            "/": self.home,
            "/user": self.user_dashboard,
            "/manager": self.manager_dashboard,
            "/login": self.login_form,
            "/logout": self.logout,
            "/reset": self.reset_lab,
            "/shop": self.shop,
            "/orders": self.customer_orders,
            "/manager/orders": self.manager_orders,
            "/admin": self.admin_dashboard,
            "/admin/products": self.admin_products,
            "/admin/users": self.admin_users,
            "/logs": self.logs,
            "/defence/session/check": self.session_check,
            "/internal/admin": self.vulnerable_admin,
            "/defence/admin": self.defended_admin,
        }
        if parsed.path == "/profile":
            return self.vulnerable_profile(parsed)
        if parsed.path == "/account/profile":
            return self.defended_profile(parsed)
        handler = routes.get(parsed.path)
        if handler:
            return handler()
        self.send_error_page(HTTPStatus.NOT_FOUND, "Page not found", "The requested page does not exist.")

    def do_POST(self) -> None:
        parsed = urlparse(self.path)
        routes = {
            "/login": self.login,
            "/shop/order": self.place_order,
            "/admin/products/add": self.add_product,
            "/admin/products/update": self.update_product,
            "/admin/products/delete": self.delete_product,
            "/admin/users/add": self.add_user,
            "/admin/users/delete": self.delete_user,
            "/internal/admin/updateRole": self.vulnerable_update_role,
            "/defence/admin/updateRole": self.defended_update_role,
        }
        handler = routes.get(parsed.path)
        if handler:
            return handler()
        self.send_error_page(HTTPStatus.NOT_FOUND, "Page not found", "The requested action does not exist.")

    def read_form(self) -> dict[str, str]:
        length = int(self.headers.get("Content-Length", "0"))
        raw = self.rfile.read(length).decode("utf-8")
        return {key: values[0] for key, values in parse_qs(raw).items()}

    def current_session(self) -> tuple[str | None, dict | None]:
        cookies = parse_cookies(self.headers.get("Cookie", ""))
        token = cookies.get("DEFENCESESSION")
        session = SESSIONS.get(token or "")
        if not token or not session:
            return None, None
        if now() - session["last_seen"] > SESSION_TIMEOUT_SECONDS:
            user_id = session["user_id"]
            SESSIONS.pop(token, None)
            log_security(f"Session timeout for user_id={user_id}")
            return None, None
        session["last_seen"] = now()
        return token, session

    def current_user(self) -> tuple[str | None, dict | None]:
        _, session = self.current_session()
        if not session:
            return None, None
        user_id = session["user_id"]
        return user_id, USERS.get(user_id)

    def require_login(self) -> tuple[str | None, dict | None]:
        user_id, user = self.current_user()
        if not user:
            self.send_error_page(
                HTTPStatus.UNAUTHORIZED,
                "Login required",
                "Please sign in before opening this page.",
                "/login",
                "Go to login",
            )
            return None, None
        return user_id, user

    def require_role(self, roles: set[str]) -> tuple[str | None, dict | None]:
        user_id, user = self.require_login()
        if not user:
            return None, None
        if user["role"] not in roles:
            log_security(
                f"Unauthorised access blocked username={user['username']} role={user['role']} path={self.path}"
            )
            self.send_error_page(
                HTTPStatus.FORBIDDEN,
                "Access denied",
                f"This page requires one of these roles: {', '.join(sorted(roles))}.",
                "/",
                "Back to dashboard",
            )
            return None, None
        return user_id, user

    def require_admin(self) -> tuple[str | None, dict | None]:
        return self.require_role({"ADMIN"})

    def require_manager(self) -> tuple[str | None, dict | None]:
        return self.require_role({"MANAGER", "ADMIN"})

    def login_form(
        self,
        error: str = "",
        username_value: str = "alice",
        status: HTTPStatus = HTTPStatus.OK,
    ) -> None:
        user_id, user = self.current_user()
        if user:
            return self.redirect(role_home_path(user))
        error_html = (
            f'<div class="auth-error">{html.escape(error)}</div>'
            if error
            else ""
        )
        content = f"""
        <section class="auth-shell">
          <div class="auth-panel">
            <p class="eyebrow">Secure Shop Lab</p>
            <h1>Sign in to the target machine</h1>
            <p class="muted">Use one of the demo accounts to test customer, manager, and administrator access control.</p>
            {error_html}
            <form method="post" action="/login" class="stack">
              <label>Username <input name="username" value="{html.escape(username_value)}" autocomplete="username"></label>
              <label>Password <input name="password" value="alice123" type="password" autocomplete="current-password"></label>
              <button class="primary">Sign in</button>
            </form>
            <a class="reset-link" href="/reset">One-click restore lab state</a>
          </div>
          <aside class="account-panel">
            <h2>Demo accounts</h2>
            <div class="credential"><strong>alice</strong><span>alice123</span><small>Customer</small></div>
            <div class="credential"><strong>bob</strong><span>bob123</span><small>Customer</small></div>
            <div class="credential"><strong>manager</strong><span>manager123</span><small>Manager</small></div>
            <div class="credential"><strong>admin</strong><span>admin123</span><small>Administrator</small></div>
          </aside>
        </section>
        """
        self.send_html(page("Login", content, user_id, user, auth_page=True), status)

    def login(self) -> None:
        form = self.read_form()
        username = form.get("username", "").strip()
        password = form.get("password", "")
        user_id = username_to_id().get(username)
        # Verify user id if exit, password is correct, and log the attempt. 
        if not user_id or USERS[user_id]["password"] != password:
            log_security(f"Failed login username={username}")
            log_login(username, False, "Invalid credentials")
            return self.login_form(
                error="Username or Password is incorrect",
                username_value=username,
                status=HTTPStatus.OK,
            )
        token = make_session(user_id)
        log_login(username, True, f"Signed in as {USERS[user_id]['role']}")
        cookie = (
            f"DEFENCESESSION={token}; Path=/; Max-Age={SESSION_TIMEOUT_SECONDS}; "
            "HttpOnly; SameSite=Strict"
        )
        self.send_response(HTTPStatus.SEE_OTHER)
        self.send_header("Location", role_home_path(USERS[user_id]))
        self.send_header("Set-Cookie", cookie)
        self.end_headers()

    def logout(self) -> None:
        token, session = self.current_session()
        if token:
            user_id = session["user_id"] if session else "unknown"
            SESSIONS.pop(token, None)
            if user_id in USERS:
                log_login(USERS[user_id]["username"], True, "Signed out")
        self.send_response(HTTPStatus.SEE_OTHER)
        self.send_header("Location", "/login")
        self.send_header("Set-Cookie", "DEFENCESESSION=deleted; Path=/; Max-Age=0; HttpOnly; SameSite=Strict")
        self.end_headers()

    def home(self) -> None:
        user_id, user = self.current_user()
        if not user:
            return self.login_form()
        return self.redirect(role_home_path(user))

    def user_dashboard(self) -> None:
        user_id, user = self.require_role({"CUSTOMER", "ADMIN"})
        if not user:
            return
        cards = [
            stat_card("Products", str(len(PRODUCTS)), "Available items in the shop"),
            stat_card("My orders", str(len([o for o in ORDERS if o["user_id"] == user_id])), "Purchases linked to this account"),
            stat_card("Account", html.escape(user["username"]), "Signed-in shopping profile"),
        ]
        actions = """
        <div class="action-grid">
          <a class="action" href="/shop"><strong>Shop products</strong><span>Place customer orders from the product catalogue.</span></a>
          <a class="action" href="/orders"><strong>My purchase records</strong><span>View your order numbers, items, and totals.</span></a>
        """
        if user["role"] == "ADMIN":
            actions += """
              <a class="action" href="/admin"><strong>Admin console</strong><span>Manage products, users, and audit logs.</span></a>
            """
        actions += "</div>"
        self.send_html(
            page(
                "Secure Shop Dashboard",
                f"""
                <section class="hero">
                  <div>
                    <p class="eyebrow">Broken Access Control Defence Target</p>
                    <h1>Welcome, {html.escape(user['username'])}</h1>
                    <p class="muted">Role: {html.escape(ROLE_LABELS.get(user['role'], user['role']))} | User ID: {html.escape(user_id)}</p>
                  </div>
                </section>
                <section class="stats">{''.join(cards)}</section>
                {actions}
                """,
                user_id,
                user,
            )
        )

    def manager_dashboard(self) -> None:
        user_id, user = self.require_manager()
        if not user:
            return
        self.send_html(
            page(
                "Manager Dashboard",
                f"""
                <section class="hero">
                  <div>
                    <p class="eyebrow">Manager workspace</p>
                    <h1>Order Operations</h1>
                    <p class="muted">Logged in as {html.escape(user['username'])} | User ID: {html.escape(user_id)}</p>
                  </div>
                </section>
                <section class="stats">
                  {stat_card("Total orders", str(len(ORDERS)), "Orders visible to operations")}
                  {stat_card("Customers", str(len([u for u in USERS.values() if u["role"] == "CUSTOMER"])), "Customer accounts")}
                  {stat_card("Products", str(len(PRODUCTS)), "Catalogue records")}
                </section>
                <div class="action-grid">
                  <a class="action" href="/manager/orders"><strong>Customer orders</strong><span>Review order numbers, customers, and shopping content.</span></a>
                  <a class="action" href="/shop"><strong>Product catalogue</strong><span>View current products and stock levels.</span></a>
                </div>
                """,
                user_id,
                user,
            )
        )

    def shop(self) -> None:
        user_id, user = self.require_login()
        if not user:
            return
        product_cards = []
        for product_id, product in PRODUCTS.items():
            product_cards.append(
                f"""
                <article class="product">
                  <div>
                    <h2>{html.escape(product['name'])}</h2>
                    <p>{html.escape(product['description'])}</p>
                    <p class="price">{money(product['price'])}</p>
                    <small>Stock: {product['stock']} | Product ID: {html.escape(product_id)}</small>
                  </div>
                  <form method="post" action="/shop/order" class="inline-form">
                    <input type="hidden" name="product_id" value="{html.escape(product_id)}">
                    <input type="number" name="quantity" value="1" min="1" max="{product['stock']}">
                    <button>Order</button>
                  </form>
                </article>
                """
            )
        self.send_html(
            page(
                "Product Catalogue",
                f"""
                <section class="page-head">
                  <div>
                    <p class="eyebrow">Customer workflow</p>
                    <h1>Product Catalogue</h1>
                  </div>
                  <a class="button secondary" href="/orders">My orders</a>
                </section>
                <section class="product-grid">{''.join(product_cards)}</section>
                """,
                user_id,
                user,
            )
        )

    def place_order(self) -> None:
        global NEXT_ORDER_NUMBER
        user_id, user = self.require_login()
        if not user:
            return
        if user["role"] not in {"CUSTOMER", "ADMIN"}:
            return self.send_error_page(
                HTTPStatus.FORBIDDEN,
                "Ordering blocked",
                "Only customer accounts can place shopping orders in this lab.",
                "/shop",
                "Back to shop",
            )
        form = self.read_form()
        product_id = form.get("product_id", "")
        product = PRODUCTS.get(product_id)
        if not product:
            return self.send_error_page(HTTPStatus.NOT_FOUND, "Product not found", "The selected product no longer exists.")
        try:
            quantity = int(form.get("quantity", "1"))
        except ValueError:
            quantity = 1
        if quantity < 1 or quantity > product["stock"]:
            return self.send_error_page(
                HTTPStatus.BAD_REQUEST,
                "Invalid quantity",
                "The requested quantity is not available.",
                "/shop",
                "Back to shop",
            )
        product["stock"] -= quantity
        order = {
            "order_no": f"ORD-{NEXT_ORDER_NUMBER}",
            "created_at": timestamp(),
            "user_id": user_id,
            "username": user["username"],
            "items": [
                {
                    "product_id": product_id,
                    "name": product["name"],
                    "price": product["price"],
                    "quantity": quantity,
                }
            ],
        }
        NEXT_ORDER_NUMBER += 1
        ORDERS.append(order)
        return self.redirect("/orders")

    def customer_orders(self) -> None:
        user_id, user = self.require_login()
        if not user:
            return
        own_orders = [order for order in ORDERS if order["user_id"] == user_id]
        self.send_html(
            page(
                "My Orders",
                f"""
                <section class="page-head">
                  <div>
                    <p class="eyebrow">Customer records</p>
                    <h1>My Purchase Records</h1>
                  </div>
                  <a class="button secondary" href="/shop">Continue shopping</a>
                </section>
                {orders_table(own_orders, show_customer=False)}
                """,
                user_id,
                user,
            )
        )

    def manager_orders(self) -> None:
        user_id, user = self.require_manager()
        if not user:
            return
        self.send_html(
            page(
                "Manager Orders",
                f"""
                <section class="page-head">
                  <div>
                    <p class="eyebrow">Manager workflow</p>
                    <h1>Customer Order Overview</h1>
                  </div>
                  <a class="button secondary" href="/manager">Dashboard</a>
                </section>
                {orders_table(ORDERS, show_customer=True)}
                """,
                user_id,
                user,
            )
        )

    def admin_dashboard(self) -> None:
        user_id, user = self.require_admin()
        if not user:
            return
        self.send_html(
            page(
                "Admin Console",
                f"""
                <section class="page-head">
                  <div>
                    <p class="eyebrow">Administrator workflow</p>
                    <h1>Admin Console</h1>
                  </div>
                </section>
                <section class="stats">
                  {stat_card("Users", str(len(USERS)), "Customer, manager, and administrator accounts")}
                  {stat_card("Products", str(len(PRODUCTS)), "Catalogue records")}
                  {stat_card("Login logs", str(len(LOGIN_LOGS)), "Successful and failed sign-in activity")}
                </section>
                <div class="action-grid">
                  <a class="action" href="/admin/products"><strong>Manage products</strong><span>Add, update, and delete catalogue items.</span></a>
                  <a class="action" href="/admin/users"><strong>Manage users</strong><span>Add or delete lab accounts.</span></a>
                  <a class="action" href="/logs"><strong>Login and security logs</strong><span>Review sign-ins and blocked attempts.</span></a>
                </div>
                """,
                user_id,
                user,
            )
        )

    def admin_products(self) -> None:
        user_id, user = self.require_admin()
        if not user:
            return
        rows = []
        for product_id, product in PRODUCTS.items():
            form_id = f"update-{html.escape(product_id)}"
            rows.append(
                f"""
                <tr>
                  <td>{html.escape(product_id)}</td>
                  <td><input form="{form_id}" name="name" value="{html.escape(product['name'])}"></td>
                  <td><input form="{form_id}" name="description" value="{html.escape(product['description'])}"></td>
                  <td><input form="{form_id}" name="price" type="number" step="0.01" min="0" value="{product['price']}"></td>
                  <td><input form="{form_id}" name="stock" type="number" min="0" value="{product['stock']}"></td>
                  <td>
                    <form id="{form_id}" method="post" action="/admin/products/update">
                      <input type="hidden" name="product_id" value="{html.escape(product_id)}">
                      <button>Save</button>
                    </form>
                  </td>
                  <td>
                    <form method="post" action="/admin/products/delete">
                      <input type="hidden" name="product_id" value="{html.escape(product_id)}">
                      <button class="danger">Delete</button>
                    </form>
                  </td>
                </tr>
                """
            )
        self.send_html(
            page(
                "Manage Products",
                f"""
                <section class="page-head">
                  <div>
                    <p class="eyebrow">Admin catalogue</p>
                    <h1>Manage Products</h1>
                  </div>
                  <a class="button secondary" href="/admin">Admin console</a>
                </section>
                <section class="panel">
                  <h2>Add product</h2>
                  <form method="post" action="/admin/products/add" class="grid-form">
                    <label>Product ID <input name="product_id" placeholder="P500"></label>
                    <label>Name <input name="name" placeholder="Product name"></label>
                    <label>Description <input name="description" placeholder="Short description"></label>
                    <label>Price <input name="price" type="number" step="0.01" min="0" value="25.00"></label>
                    <label>Stock <input name="stock" type="number" min="0" value="5"></label>
                    <button>Add product</button>
                  </form>
                </section>
                <section class="panel scroll">
                  <table>
                    <thead><tr><th>ID</th><th>Name</th><th>Description</th><th>Price</th><th>Stock</th><th>Save</th><th>Delete</th></tr></thead>
                    <tbody>{''.join(rows) or '<tr><td colspan="7">No products.</td></tr>'}</tbody>
                  </table>
                </section>
                """,
                user_id,
                user,
            )
        )

    def add_product(self) -> None:
        _, user = self.require_admin()
        if not user:
            return
        form = self.read_form()
        product_id = form.get("product_id", "").strip().upper()
        if not product_id or product_id in PRODUCTS:
            return self.send_error_page(HTTPStatus.BAD_REQUEST, "Invalid product", "Use a unique product ID.", "/admin/products", "Back")
        PRODUCTS[product_id] = product_from_form(form)
        log_security(f"Product added admin={user['username']} product_id={product_id}")
        self.redirect("/admin/products")

    def update_product(self) -> None:
        _, user = self.require_admin()
        if not user:
            return
        form = self.read_form()
        product_id = form.get("product_id", "")
        if product_id not in PRODUCTS:
            return self.send_error_page(HTTPStatus.NOT_FOUND, "Product not found", "The selected product does not exist.")
        PRODUCTS[product_id] = product_from_form(form)
        log_security(f"Product updated admin={user['username']} product_id={product_id}")
        self.redirect("/admin/products")

    def delete_product(self) -> None:
        _, user = self.require_admin()
        if not user:
            return
        form = self.read_form()
        product_id = form.get("product_id", "")
        if product_id in PRODUCTS:
            PRODUCTS.pop(product_id)
            log_security(f"Product deleted admin={user['username']} product_id={product_id}")
        self.redirect("/admin/products")

    def admin_users(self) -> None:
        user_id, user = self.require_admin()
        if not user:
            return
        rows = []
        for target_id, target in USERS.items():
            delete_button = (
                "<span class=\"muted\">Current user</span>"
                if target_id == user_id
                else f"""
                <form method="post" action="/admin/users/delete">
                  <input type="hidden" name="user_id" value="{html.escape(target_id)}">
                  <button class="danger">Delete</button>
                </form>
                """
            )
            rows.append(
                f"""
                <tr>
                  <td>{html.escape(target_id)}</td>
                  <td>{html.escape(target['username'])}</td>
                  <td>{html.escape(target['email'])}</td>
                  <td>{html.escape(target['role'])}</td>
                  <td>{delete_button}</td>
                </tr>
                """
            )
        self.send_html(
            page(
                "Manage Users",
                f"""
                <section class="page-head">
                  <div>
                    <p class="eyebrow">Admin identity</p>
                    <h1>Manage Users</h1>
                  </div>
                  <a class="button secondary" href="/admin">Admin console</a>
                </section>
                <section class="panel">
                  <h2>Add user</h2>
                  <form method="post" action="/admin/users/add" class="grid-form">
                    <label>Username <input name="username" placeholder="charlie"></label>
                    <label>Password <input name="password" placeholder="password123"></label>
                    <label>Email <input name="email" type="email" placeholder="charlie@student.local"></label>
                    <label>Role
                      <select name="role">
                        <option>CUSTOMER</option>
                        <option>MANAGER</option>
                        <option>ADMIN</option>
                      </select>
                    </label>
                    <button>Add user</button>
                  </form>
                </section>
                <section class="panel scroll">
                  <table>
                    <thead><tr><th>User ID</th><th>Username</th><th>Email</th><th>Role</th><th>Action</th></tr></thead>
                    <tbody>{''.join(rows)}</tbody>
                  </table>
                </section>
                """,
                user_id,
                user,
            )
        )

    def add_user(self) -> None:
        global NEXT_USER_ID
        _, admin = self.require_admin()
        if not admin:
            return
        form = self.read_form()
        username = form.get("username", "").strip()
        password = form.get("password", "").strip()
        email = form.get("email", "").strip()
        role = form.get("role", "CUSTOMER").upper()
        if not username or not password or role not in {"CUSTOMER", "MANAGER", "ADMIN"}:
            return self.send_error_page(HTTPStatus.BAD_REQUEST, "Invalid user", "Username, password, and valid role are required.", "/admin/users", "Back")
        if username in username_to_id():
            return self.send_error_page(HTTPStatus.BAD_REQUEST, "Duplicate username", "Choose a username that does not already exist.", "/admin/users", "Back")
        user_id = str(NEXT_USER_ID)
        NEXT_USER_ID += 1
        USERS[user_id] = {
            "username": username,
            "password": password,
            "email": email or f"{username}@student.local",
            "role": role,
            "account": "Created from admin console",
            "preferences": "No notification preference set",
        }
        log_security(f"User added admin={admin['username']} username={username} role={role}")
        self.redirect("/admin/users")

    def delete_user(self) -> None:
        admin_id, admin = self.require_admin()
        if not admin:
            return
        form = self.read_form()
        target_id = form.get("user_id", "")
        if target_id == admin_id:
            return self.send_error_page(HTTPStatus.BAD_REQUEST, "Delete blocked", "The active administrator cannot delete their own account.", "/admin/users", "Back")
        if target_id in USERS:
            username = USERS[target_id]["username"]
            USERS.pop(target_id)
            for token, session in list(SESSIONS.items()):
                if session["user_id"] == target_id:
                    SESSIONS.pop(token)
            log_security(f"User deleted admin={admin['username']} username={username}")
        self.redirect("/admin/users")

    def logs(self) -> None:
        user_id, user = self.require_admin()
        if not user:
            return
        login_rows = [
            f"""
            <tr>
              <td>{html.escape(entry['time'])}</td>
              <td>{html.escape(entry['username'])}</td>
              <td>{'Success' if entry['success'] else 'Failed'}</td>
              <td>{html.escape(entry['detail'])}</td>
            </tr>
            """
            for entry in LOGIN_LOGS
        ]
        security_body = "\n".join(SECURITY_LOGS) or "No security events yet."
        self.send_html(
            page(
                "Logs",
                f"""
                <section class="page-head">
                  <div>
                    <p class="eyebrow">Defence4</p>
                    <h1>Login and Security Logs</h1>
                  </div>
                  <a class="button secondary" href="/admin">Admin console</a>
                </section>
                <section class="panel scroll">
                  <h2>Login log</h2>
                  <table>
                    <thead><tr><th>Time</th><th>Username</th><th>Status</th><th>Detail</th></tr></thead>
                    <tbody>{''.join(login_rows) or '<tr><td colspan="4">No login events.</td></tr>'}</tbody>
                  </table>
                </section>
                <section class="panel">
                  <h2>Security log</h2>
                  <pre>{html.escape(security_body)}</pre>
                </section>
                """,
                user_id,
                user,
            )
        )

    def reset_lab(self) -> None:
        reset_state()
        self.send_response(HTTPStatus.SEE_OTHER)
        self.send_header("Location", "/login")
        self.send_header("Set-Cookie", "DEFENCESESSION=deleted; Path=/; Max-Age=0; HttpOnly; SameSite=Strict")
        self.end_headers()

    def session_check(self) -> None:
        user_id, user = self.require_login()
        if not user:
            return
        self.send_json(
            {
                "mode": "defended",
                "control": "Session timeout plus HttpOnly and SameSite cookie attributes",
                "timeoutSeconds": SESSION_TIMEOUT_SECONDS,
                "currentUserId": user_id,
                "currentRole": user["role"],
            }
        )

    def vulnerable_profile(self, parsed) -> None:
        if not self.require_login()[1]:
            return
        target_id = parse_qs(parsed.query).get("user", ["101"])[0]
        target = USERS.get(target_id)
        if not target:
            return self.send_error_page(HTTPStatus.NOT_FOUND, "No such user", "The requested user ID was not found.")
        self.send_json(
            {
                "mode": "vulnerable",
                "issue": "Profile lookup accepted a client-supplied user parameter",
                "requestedUserId": target_id,
                "profile": public_profile(target_id, target),
            }
        )

    def defended_profile(self, parsed) -> None:
        user_id, user = self.require_login()
        if not user:
            return
        target_id = parse_qs(parsed.query).get("user", [user_id])[0]
        if target_id != user_id and user["role"] not in {"MANAGER", "ADMIN"}:
            log_security(
                f"Profile access attempt blocked username={user['username']} requested_user={target_id}"
            )
            return self.send_error_page(
                HTTPStatus.FORBIDDEN,
                "Access denied",
                "The requested profile does not belong to this session.",
                "/",
                "Back to dashboard",
            )
        target = USERS.get(target_id)
        if not target:
            return self.send_error_page(HTTPStatus.NOT_FOUND, "No such user", "The requested user ID was not found.")
        self.send_json(
            {
                "mode": "defended",
                "control": "Server-side resource ownership validation",
                "requestedUserId": target_id,
                "profile": public_profile(target_id, target),
            }
        )

    def vulnerable_admin(self) -> None:
        if not self.require_login()[1]:
            return
        self.send_html(
            page(
                "Internal Admin",
                """
                <section class="panel danger-zone">
                  <p class="bad">Administrative maintenance action.</p>
                  <form method="post" action="/internal/admin/updateRole" class="grid-form">
                    <label>User ID <input name="user" value="101"></label>
                    <label>Role <input name="role" value="ADMIN"></label>
                    <button>Update role</button>
                  </form>
                </section>
                """,
                *self.current_user(),
            )
        )

    def defended_admin(self) -> None:
        user_id, user = self.require_admin()
        if not user:
            return
        self.send_html(
            page(
                "Admin Role Management",
                """
                <section class="panel">
                  <form method="post" action="/defence/admin/updateRole" class="grid-form">
                    <label>User ID <input name="user" value="101"></label>
                    <label>Role
                      <select name="role">
                        <option>CUSTOMER</option>
                        <option>MANAGER</option>
                        <option>ADMIN</option>
                      </select>
                    </label>
                    <button>Update role as admin</button>
                  </form>
                </section>
                """,
                user_id,
                user,
            )
        )

    def vulnerable_update_role(self) -> None:
        if not self.require_login()[1]:
            return
        form = self.read_form()
        target_id = form.get("user", "101")
        role = form.get("role", "CUSTOMER").upper()
        if target_id in USERS:
            USERS[target_id]["role"] = role
        self.send_json(
            {
                "mode": "vulnerable",
                "issue": "Privilege escalation: trusted client-supplied role parameter",
                "updatedUserId": target_id,
                "newRole": USERS.get(target_id, {}).get("role"),
            }
        )

    def defended_update_role(self) -> None:
        admin_id, admin = self.require_admin()
        if not admin:
            return
        form = self.read_form()
        target_id = form.get("user", "")
        role = form.get("role", "CUSTOMER").upper()
        if role not in {"CUSTOMER", "MANAGER", "ADMIN"}:
            log_security(f"Invalid role update blocked admin={admin['username']} role={role}")
            return self.send_error_page(HTTPStatus.BAD_REQUEST, "Invalid role", "Use CUSTOMER, MANAGER, or ADMIN.")
        if target_id not in USERS:
            return self.send_error_page(HTTPStatus.NOT_FOUND, "No such user", "The requested user ID was not found.")
        USERS[target_id]["role"] = role
        log_security(
            f"Authorised role update admin={admin['username']} target_user={target_id} role={role}"
        )
        self.send_json(
            {
                "mode": "defended",
                "control": "RBAC and server-side role validation",
                "updatedBy": admin_id,
                "updatedUserId": target_id,
                "newRole": role,
            }
        )

    def redirect(self, location: str) -> None:
        self.send_response(HTTPStatus.SEE_OTHER)
        self.send_header("Location", location)
        self.end_headers()

    def send_text(self, text: str, status: HTTPStatus = HTTPStatus.OK) -> None:
        self.send_response(status)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(text.encode("utf-8"))

    def send_json(self, payload: dict, status: HTTPStatus = HTTPStatus.OK) -> None:
        import json

        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(json.dumps(payload, indent=2).encode("utf-8"))

    def send_html(self, body: str, status: HTTPStatus = HTTPStatus.OK) -> None:
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(body.encode("utf-8"))

    def send_error_page(
        self,
        status: HTTPStatus,
        title: str,
        message: str,
        action_href: str = "/",
        action_text: str = "Back to dashboard",
    ) -> None:
        user_id, user = self.current_user()
        content = f"""
        <section class="error-page">
          <p class="eyebrow">{status.value} {html.escape(status.phrase)}</p>
          <h1>{html.escape(title)}</h1>
          <p>{html.escape(message)}</p>
          <a class="button" href="{html.escape(action_href)}">{html.escape(action_text)}</a>
        </section>
        """
        self.send_html(page(title, content, user_id, user), status)

    def log_message(self, fmt: str, *args) -> None:
        print("%s - %s" % (self.address_string(), fmt % args))


def product_from_form(form: dict[str, str]) -> dict:
    try:
        price = max(0.0, float(form.get("price", "0")))
    except ValueError:
        price = 0.0
    try:
        stock = max(0, int(form.get("stock", "0")))
    except ValueError:
        stock = 0
    return {
        "name": form.get("name", "Unnamed product").strip() or "Unnamed product",
        "description": form.get("description", "No description").strip() or "No description",
        "price": price,
        "stock": stock,
    }


def stat_card(label: str, value: str, detail: str) -> str:
    return f"""
    <article class="stat">
      <span>{html.escape(label)}</span>
      <strong>{html.escape(value)}</strong>
      <small>{html.escape(detail)}</small>
    </article>
    """


def orders_table(orders: list[dict], show_customer: bool) -> str:
    if not orders:
        return '<section class="panel empty">No orders yet.</section>'
    rows = []
    for order in orders:
        item_text = ", ".join(
            f"{html.escape(item['name'])} x {item['quantity']} ({money(item['price'])})"
            for item in order["items"]
        )
        customer_cell = f"<td>{html.escape(order['username'])} ({html.escape(order['user_id'])})</td>" if show_customer else ""
        rows.append(
            f"""
            <tr>
              <td>{html.escape(order['order_no'])}</td>
              {customer_cell}
              <td>{html.escape(order['created_at'])}</td>
              <td>{item_text}</td>
              <td>{money(order_total(order))}</td>
            </tr>
            """
        )
    customer_header = "<th>Customer</th>" if show_customer else ""
    return f"""
    <section class="panel scroll">
      <table>
        <thead><tr><th>Order No.</th>{customer_header}<th>Created</th><th>Shopping Content</th><th>Total</th></tr></thead>
        <tbody>{''.join(rows)}</tbody>
      </table>
    </section>
    """


def nav(user: dict | None) -> str:
    if not user:
        return ""
    home_href = role_home_path(user)
    manager_link = '<a href="/manager">Manager</a>' if user["role"] in {"MANAGER", "ADMIN"} else ""
    admin_link = '<a href="/admin">Admin</a>' if user["role"] == "ADMIN" else ""
    return f"""
    <header class="topbar">
      <a class="brand" href="{home_href}">Secure Shop Lab</a>
      <nav>
        <a href="{home_href}">Home</a>
        <a href="/shop">Shop</a>
        <a href="/orders">My orders</a>
        {manager_link}
        {admin_link}
        <a href="/logout">Logout</a>
      </nav>
    </header>
    """


def page(title: str, content: str, user_id: str | None = None, user: dict | None = None, auth_page: bool = False) -> str:
    signed_in = ""
    watermark = ""
    if user and user_id:
        username = html.escape(user["username"])
        signed_in = f"<div class=\"session-pill\">{username} | {html.escape(user['role'])}</div>"
        watermark = f"<div class=\"user-watermark\">{username}</div>"
    body_class = "auth-body" if auth_page else "app-body"
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <style>
    :root {{
      color-scheme: light;
      --ink: #19212a;
      --muted: #657282;
      --line: #d8e0e8;
      --panel: #ffffff;
      --soft: #f4f7f9;
      --accent: #136f63;
      --accent-dark: #0d4f47;
      --danger: #b42318;
      --warn-bg: #fff4ed;
    }}
    * {{ box-sizing: border-box; }}
    body {{ margin: 0; font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; color: var(--ink); background: var(--soft); line-height: 1.5; }}
    a {{ color: var(--accent-dark); text-decoration: none; }}
    h1, h2 {{ margin: 0; line-height: 1.15; letter-spacing: 0; }}
    h1 {{ font-size: 2rem; }}
    h2 {{ font-size: 1.1rem; }}
    p {{ margin: .5rem 0; }}
    input, select {{ width: 100%; border: 1px solid var(--line); border-radius: 6px; padding: .65rem .7rem; font: inherit; background: white; }}
    label {{ display: grid; gap: .35rem; font-weight: 700; font-size: .9rem; }}
    button, .button {{ display: inline-flex; align-items: center; justify-content: center; border: 1px solid var(--accent); background: var(--accent); color: white; padding: .68rem .9rem; border-radius: 6px; font: inherit; font-weight: 800; cursor: pointer; min-height: 42px; }}
    button:hover, .button:hover {{ background: var(--accent-dark); color: white; }}
    button.secondary, .button.secondary {{ background: white; color: var(--accent-dark); }}
    button.danger, .danger {{ border-color: var(--danger); background: var(--danger); color: white; }}
    table {{ width: 100%; border-collapse: collapse; min-width: 760px; }}
    th, td {{ text-align: left; border-bottom: 1px solid var(--line); padding: .75rem; vertical-align: top; }}
    th {{ color: var(--muted); font-size: .82rem; text-transform: uppercase; }}
    pre {{ background: #18222d; color: #f7fafc; border-radius: 8px; padding: 1rem; overflow: auto; }}
    .app-body main {{ width: min(1180px, calc(100% - 2rem)); margin: 1rem auto 3rem; position: relative; z-index: 1; }}
    .auth-body main {{ min-height: 100vh; display: grid; place-items: center; padding: 1rem; }}
    .topbar {{ display: flex; align-items: center; justify-content: space-between; gap: 1rem; padding: .9rem max(1rem, calc((100vw - 1180px) / 2)); background: white; border-bottom: 1px solid var(--line); position: sticky; top: 0; z-index: 2; }}
    .brand {{ font-weight: 900; color: var(--ink); }}
    nav {{ display: flex; align-items: center; gap: .8rem; flex-wrap: wrap; }}
    nav a {{ color: var(--muted); font-weight: 700; }}
    .session-pill {{ position: fixed; right: 1rem; bottom: 1rem; background: #203040; color: white; padding: .55rem .75rem; border-radius: 999px; font-size: .82rem; box-shadow: 0 8px 24px rgba(0,0,0,.16); }}
    .user-watermark {{ position: fixed; inset: 0; display: grid; place-items: center; pointer-events: none; z-index: 0; color: rgba(25, 33, 42, .055); font-size: clamp(4rem, 18vw, 13rem); font-weight: 900; text-transform: uppercase; transform: rotate(-22deg); user-select: none; white-space: nowrap; }}
    .auth-shell {{ display: grid; grid-template-columns: minmax(280px, 480px) minmax(260px, 360px); gap: 1rem; width: min(920px, 100%); }}
    .auth-panel, .account-panel, .panel, .stat, .action, .product {{ background: var(--panel); border: 1px solid var(--line); border-radius: 8px; }}
    .auth-panel, .account-panel {{ padding: 1.4rem; }}
    .auth-error {{ margin: 1rem 0 0; border: 1px solid #f5b5ae; background: #fff4f2; color: var(--danger); border-radius: 6px; padding: .72rem .8rem; font-weight: 800; }}
    .stack {{ display: grid; gap: .9rem; margin-top: 1rem; }}
    .reset-link {{ display: inline-block; margin-top: 1rem; font-weight: 800; }}
    .credential {{ display: grid; grid-template-columns: 1fr 1fr; gap: .2rem .75rem; border-top: 1px solid var(--line); padding: .7rem 0; }}
    .credential small {{ grid-column: 1 / -1; color: var(--muted); }}
    .hero, .page-head {{ display: flex; align-items: center; justify-content: space-between; gap: 1rem; margin: 1rem 0; }}
    .eyebrow {{ color: var(--accent-dark); font-size: .8rem; font-weight: 900; text-transform: uppercase; letter-spacing: .08em; }}
    .muted {{ color: var(--muted); }}
    .stats {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap: 1rem; margin: 1rem 0; }}
    .stat {{ padding: 1rem; display: grid; gap: .25rem; }}
    .stat span, .stat small {{ color: var(--muted); }}
    .stat strong {{ font-size: 1.8rem; }}
    .action-grid, .product-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin: 1rem 0; }}
    .action {{ padding: 1rem; display: grid; gap: .35rem; color: var(--ink); }}
    .action span {{ color: var(--muted); }}
    .product {{ padding: 1rem; display: grid; gap: 1rem; align-content: space-between; }}
    .price {{ font-weight: 900; font-size: 1.35rem; color: var(--accent-dark); }}
    .inline-form {{ display: grid; grid-template-columns: 90px 1fr; gap: .5rem; }}
    .panel {{ padding: 1rem; margin: 1rem 0; }}
    .scroll {{ overflow-x: auto; }}
    .grid-form {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: .8rem; align-items: end; }}
    .table-form {{ display: contents; }}
    .empty {{ color: var(--muted); }}
    .bad {{ color: var(--danger); font-weight: 900; }}
    .good {{ color: var(--accent-dark); font-weight: 900; }}
    .danger-zone {{ background: var(--warn-bg); border-color: #ffcfb8; }}
    .error-page {{ width: min(620px, 100%); margin: 4rem auto; background: white; border: 1px solid var(--line); border-radius: 8px; padding: 2rem; text-align: center; }}
    @media (max-width: 760px) {{
      .auth-shell {{ grid-template-columns: 1fr; }}
      .hero, .page-head, .topbar {{ align-items: flex-start; flex-direction: column; }}
      .inline-form {{ grid-template-columns: 1fr; }}
      h1 {{ font-size: 1.6rem; }}
    }}
  </style>
</head>
<body class="{body_class}">
  {watermark}
  {nav(user)}
  <main>{content}</main>
  {signed_in}
</body>
</html>"""


def main() -> None:
    server = ThreadingHTTPServer((HOST, PORT), DefenceTarget)
    print(f"Defence shopping target running at http://{HOST}:{PORT}")
    print("Accounts: alice/alice123, bob/bob123, manager/manager123, admin/admin123")
    server.serve_forever()


if __name__ == "__main__":
    main()
