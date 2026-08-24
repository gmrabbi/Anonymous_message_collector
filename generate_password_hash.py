from getpass import getpass
from werkzeug.security import generate_password_hash

password = getpass("Enter the admin password you want to use: ")
confirm = getpass("Confirm the admin password: ")

if not password:
    raise SystemExit("Password cannot be empty.")

if password != confirm:
    raise SystemExit("Passwords do not match.")

print("\nCopy this value into ADMIN_PASSWORD_HASH in your .env file:\n")
print(generate_password_hash(password))
