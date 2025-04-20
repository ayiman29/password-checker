from flask import Flask, render_template, request, session
import random
import string
import hashlib
import requests

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required for using sessions

# Function to generate a password
def generate_password():
    length = 12  # You can customize the length
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

# Function to check if the password is found in data breaches
def check_password_breach(password):
    hashed_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = hashed_password[:5]
    suffix = hashed_password[5:]
    
    response = requests.get(f'https://api.pwnedpasswords.com/range/{prefix}')
    hashes = response.text.splitlines()

    for line in hashes:
        # Split each line into suffix and count based on the ':' separator
        suffix_hash, count = line.split(':')
        if suffix_hash == suffix:
            return True  # Password is found in data breaches
    return False  # Password is not found

@app.route("/", methods=["GET", "POST"])
def index():
    safe_status = ""
    if request.method == "POST":
        if 'generate_password' in request.form:
            # Generate a new password and store it in session
            password = generate_password()
            session['password'] = password
        elif 'check_breach' in request.form:
            # Get the password from session and check breach
            password = session.get('password', '')
            if check_password_breach(password):
                safe_status = "This password is found in a data breach!"
            else:
                safe_status = "This password is safe!"
    else:
        # Initialize password if not already in session
        password = session.get('password', None)
        if not password:
            password = generate_password()
            session['password'] = password

    return render_template("index.html", password=password, safe_status=safe_status)

if __name__ == "__main__":
    app.run(debug=True)
