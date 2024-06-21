# utils.py
def get_api_key():
    """
    Reads the API key from a file named 'api_key.txt'.
    """
    try:
        with open('api_key.txt', 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        print("Error: 'api_key.txt' file not found.")
        return None