from flask import Flask, render_template, request
import random
import string
import requests
import hashlib

app = Flask(__name__)

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
        hash_suffix, count = line.split(':')
        if hash_suffix == suffix:  # Compare the correct suffix
            return True  # Password is found in data breaches
    return False  # Password is not found



@app.route("/", methods=["GET", "POST"])
def index():
    password = ""
    safe_status = ""
    if request.method == "POST":
        password = generate_password()
        # Check if the generated password is safe
        if check_password_breach(password):
            safe_status = "This password is found in a data breach!"
        else:
            safe_status = "This password is safe!"
    return render_template("index.html", password=password, safe_status=safe_status)

if __name__ == "__main__":
    app.run(debug=True)
