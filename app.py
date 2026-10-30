from flask import Flask, request, render_template_string
import os
import requests

app = Flask(_name_)

# --- SETTINGS ---
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

def send_telegram(text):
    if not BOT_TOKEN or not CHAT_ID:
        return
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": CHAT_ID, "text": text}, timeout=10)
    except:
        pass

# --- YOUR SHOP PAGE ---
HTML = """
<h1>Avis Shop X - Jersey Order</h1>
<form method="POST">
  Name on Jersey: <input name="jersey_name" required><br><br>
  Number: <input name="number" required><br><br>
  Size: <select name="size"><option>Small</option><option>Medium</option><option>Large</option></select><br><br>
  First Name: <input name="first_name" required><br><br>
  School: <input name="school" required><br><br>
  <button type="submit">Order Now</button>
</form>
"""

ORDER_HTML = """
<h1>✅ Order Received!</h1>
<p>Kevin will contact you soon.</p>
<a href="/"><button>Go to Shop Now</button></a>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        data = request.form
        msg = f"NEW JERSEY ORDER:\nJersey: {data.get('jersey_name')}\nNumber: {data.get('number')}\nSize: {data.get('size')}\nName: {data.get('first_name')}\nSchool: {data.get('school')}"
        send_telegram(msg)
        return ORDER_HTML
    return HTML

if _name_ == "_main_":
    app.run()
