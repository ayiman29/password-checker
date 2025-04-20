from flask import Flask, render_template, request, session
import random
import string
import hashlib
import requests

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required for using sessions

# Function to generate a password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Function to check if the password is found in data breaches
def check_password_breach(password):
    hashed_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = hashed_password[:5]
    suffix = hashed_password[5:]
    
    response = requests.get(f'https://api.pwnedpasswords.com/range/{prefix}')
    hashes = response.text.splitlines()

    for line in hashes:
        suffix_hash, count = line.split(':')
        if suffix_hash == suffix:
            return True
    return False

@app.route("/", methods=["GET", "POST"])
def index():
    password = session.get('password', '')
    safe_status = ''
    length = 12  # default

    if request.method == "POST":
        if 'generate_password' in request.form:
            try:
                length = int(request.form.get('length', 12))
                if length < 6 or length > 32:
                    length = 12  # clamp if invalid
            except ValueError:
                length = 12
            password = generate_password(length)
            session['password'] = password
            safe_status = ''
        elif 'check_breach' in request.form:
            password = session.get('password', '')
            if password:
                breached = check_password_breach(password)
                safe_status = "This password is found in a data breach!" if breached else "This password was not found in any data breach. It's safe to use!"
            else:
                safe_status = "Please generate a password first."

    return render_template("index.html", password=password, safe_status=safe_status, length=length)


if __name__ == "__main__":
    app.run(debug=True)
