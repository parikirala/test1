# hello_copilot.py — AI-assisted code

import json
from utils.math_helper import average

def greet_user(name: str):
    """Greets a user by name."""
    print(f"👋 Hello {name}, welcome to Copilot world!")

def load_user_data(filename: str):
    """Load user data from a JSON file."""
    with open(filename, 'r') as f:
        return json.load(f)

if __name__ == "__main__":
    users = load_user_data("user_data.json")
    ages = [user["age"] for user in users]
    print(f"Average age: {average(ages):.1f}")
    for user in users:
        greet_user(user["name"])
