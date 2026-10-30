from flask import Flask, request, send_from_directory
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('.', filename)

@app.route('/order', methods=['POST'])
def order():
    data = request.get_json() or request.form
    name = data.get('name', 'Customer')
    jersey = data.get('jersey', '')
    phone = data.get('phone', '')
    
    text = f"NEW ORDER!\nName: {name}\nJersey: {jersey}\nPhone: {phone}"
    
    if BOT_TOKEN and CHAT_ID:
        try:
            requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", params={"chat_id": CHAT_ID, "text": text}, timeout=10)
        except:
            pass
    
    return {"status": "order received", "message": f"Thanks {name}!"}

if _name_ == '_main_':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
