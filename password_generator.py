import random
import string
import hashlib
import requests

# Function to generate a random password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to check if the password has been pwned (breached)
def check_breach(password):
    # Hash the password with SHA1 (as required by the API)
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    
    # First 5 characters of the hash
    hash_prefix = sha1_hash[:5]
    
    # API endpoint to check for breaches
    url = f"https://api.pwnedpasswords.com/range/{hash_prefix}"
    
    # Make the API request
    response = requests.get(url)
    
    # If the request is successful
    if response.status_code == 200:
        # Check if the password hash exists in the response
        hashes = response.text.splitlines()
        for hash_entry in hashes:
            hash_suffix, count = hash_entry.split(':')
            if hash_suffix == sha1_hash[5:]:
                return True, int(count)
        return False, 0
    else:
        raise Exception("Error checking the password against the database")

# Main program
if __name__ == "__main__":
    # Step 1: Generate a random password
    password = generate_password(12)  # You can change the length here
    print(f"Generated Password: {password}")
    
    # Step 2: Check if the password is breached
    is_breached, breach_count = check_breach(password)
    
    # Output results
    if is_breached:
        print(f"Warning! This password has been breached {breach_count} times.")
    else:
        print("This password is safe!")
