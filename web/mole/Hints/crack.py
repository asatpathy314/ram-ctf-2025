import hashlib
import zipfile
import os

# The string to hash
password_string = "DarkKnight42"

# Generate different hashes
md5_hash = hashlib.md5(password_string.encode()).hexdigest()
sha1_hash = hashlib.sha1(password_string.encode()).hexdigest()
sha256_hash = hashlib.sha256(password_string.encode()).hexdigest()

# Print hashes for reference
print(f"MD5: {md5_hash}")
print(f"SHA-1: {sha1_hash}")
print(f"SHA-256: {sha256_hash}")

# Try to extract with each hash
zip_file = "passwords.zip"
passwords = [md5_hash, sha1_hash, sha256_hash]

for pwd in passwords:
    try:
        with zipfile.ZipFile(zip_file) as zf:
            zf.extractall(pwd=pwd.encode())
            print(f"Successfully extracted with password: {pwd}")
            break
    except Exception as e:
        print(f"Failed with {pwd}: {str(e)}")
