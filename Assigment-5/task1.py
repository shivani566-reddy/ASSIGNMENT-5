import hashlib
import json
import os
from typing import Dict, Tuple

class LoginSystem:
    def __init__(self, credentials_file: str = "credentials.json"):
        """Initialize login system with credentials file path."""
        self.credentials_file = credentials_file
        self.credentials = self._load_credentials()

    def _load_credentials(self) -> Dict[str, str]:
        """Load credentials from file or create empty ones if file doesn't exist."""
        if os.path.exists(self.credentials_file):
            with open(self.credentials_file, 'r') as f:
                return json.load(f)
        return {}

    def _save_credentials(self) -> None:
        """Save credentials to file."""
        with open(self.credentials_file, 'w') as f:
            json.dump(self.credentials, f)

    def _hash_password(self, password: str) -> str:
        """Hash password using SHA-256."""
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self, username: str, password: str) -> bool:
        """Register a new user."""
        if username in self.credentials:
            return False
        
        self.credentials[username] = self._hash_password(password)
        self._save_credentials()
        return True

    def login(self, username: str, password: str) -> bool:
        """Verify login credentials."""
        if username not in self.credentials:
            return False
        
        return self.credentials[username] == self._hash_password(password)

def get_user_input() -> Tuple[str, str]:
    """Get username and password from user with validation."""
    while True:
        username = input("Username: ").strip()
        if username and username.isalnum():
            break
        print("Username must be alphanumeric and non-empty.")
    
    while True:
        password = input("Password: ").strip()
        if len(password) >= 8:
            break
        print("Password must be at least 8 characters long.")
    
    return username, password

def main():
    login_system = LoginSystem()
    
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            print("\nRegister new user:")
            username, password = get_user_input()
            if login_system.register(username, password):
                print("Registration successful!")
            else:
                print("Username already exists!")

        elif choice == '2':
            print("\nLogin:")
            username, password = get_user_input()
            if login_system.login(username, password):
                print("Login successful!")
            else:
                print("Invalid credentials!")

        elif choice == '3':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()