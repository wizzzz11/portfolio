from flask import Flask, render_template, request, redirect, session
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "fanverse_secret"

DB = "database.db"

def connect_db():
    return sqlite3.connect(DB)

# Home
@app.route("/")
def home():
    return render_template("home.html")

# Shop
@app.route("/shop")
def shop():
    products = [
        {"name": "Barcelona Jersey", "price": 799, "image": "jersey1.jpg"},
        {"name": "Real Madrid Jersey", "price": 799, "image": "jersey2.jpg"}
    ]
    return render_template("shop.html", products=products)

# Checkout
@app.route("/checkout/<product>/<price>")
def checkout(product, price):
    return render_template("checkout.html", product=product, price=price)

# Order
@app.route("/order", methods=["POST"])
def order():

    name = request.form["name"]
    phone = request.form["phone"]
    address = request.form["address"]
    product = request.form["product"]
    price = request.form["price"]

    conn = connect_db()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS orders(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        phone TEXT,
        address TEXT,
        product TEXT,
        price TEXT)
    """)

    cur.execute("INSERT INTO orders(name,phone,address,product,price) VALUES(?,?,?,?,?)",
                (name, phone, address, product, price))

    conn.commit()
    conn.close()

    return redirect("/success")

@app.route("/success")
def success():
    return render_template("success.html")

# Admin login
@app.route("/admin", methods=["GET", "POST"])
def admin():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "fanverse123":
            session["admin"] = True
            return redirect("/dashboard")

    return render_template("admin_login.html")

# Dashboard
@app.route("/dashboard")
def dashboard():

    if "admin" not in session:
        return redirect("/admin")

    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM orders")
    orders = cur.fetchall()

    conn.close()

    return render_template("admin_dashboard.html", orders=orders)


# Render Port
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)