import requests

def get_random_quote():
    url = "https://api.quotable.io/random"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return f'"{data["content"]}" - {data["author"]}'
    else:
        return "Could not fetch a quote. Try again later."

if __name__ == "__main__":
    print("Here’s a random inspirational quote for you:\n")
    print(get_random_quote())
