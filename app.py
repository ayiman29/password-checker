from flask import Flask, render_template, request, session
import random
import string
import hashlib
import requests
from dotenv import load_dotenv
import os
load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'dev-fallback-key')

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def check_password_breach(password):
    sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1[:5], sha1[5:]
    resp = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}")
    if resp.status_code != 200:
        raise RuntimeError("API request failed")
    for line in resp.text.splitlines():
        h, count = line.split(':')
        if h == suffix:
            return True
    return False

@app.route("/", methods=["GET", "POST"])
def index():
    password = session.get('password', '')
    safe_status = ''
    length = 12

    if request.method == "POST":
        if 'generate_password' in request.form:
            try:
                length = int(request.form.get('length', 12))
                length = max(6, min(length, 32))
            except ValueError:
                length = 12
            password = generate_password(length)
            session['password'] = password
            safe_status = ''
        elif 'check_breach' in request.form:
            if password:
                try:
                    breached = check_password_breach(password)
                    safe_status = ("This password is found in a data breach!"
                                   if breached else
                                   "This password was not found in any data breach. It's safe to use!")
                except Exception:
                    safe_status = "Error checking breach. Try again later."
            else:
                safe_status = "Please generate a password first."

    return render_template("index.html",
                           password=password,
                           safe_status=safe_status,
                           length=length)

if __name__ == "__main__":
    app.run(debug=True)
