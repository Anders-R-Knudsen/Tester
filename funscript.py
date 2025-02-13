import requests
import random

# Fallback quotes in case the API request fails
fallback_quotes = [
    {"content": "The best way to get started is to quit talking and begin doing.", "author": "Walt Disney"},
    {"content": "Success is not final, failure is not fatal: it is the courage to continue that counts.", "author": "Winston Churchill"},
    {"content": "The only limit to our realization of tomorrow is our doubts of today.", "author": "Franklin D. Roosevelt"},
    {"content": "Do what you can, with what you have, where you are.", "author": "Theodore Roosevelt"},
    {"content": "Believe you can and you're halfway there.", "author": "Theodore Roosevelt"}
]

def get_random_quote():
    url = "https://api.quotable.io/random"
    try:
        response = requests.get(url, timeout=5)  # Timeout to prevent hanging
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
        data = response.json()
        return f'"{data["content"]}" - {data["author"]}'
    except (requests.RequestException, ValueError):  
        # If the API fails, return a random fallback quote
        quote = random.choice(fallback_quotes)
        return f'"{quote["content"]}" - {quote["author"]}'

if __name__ == "__main__":
    print("Here’s a random inspirational quote for you:\n")
    print(get_random_quote())
