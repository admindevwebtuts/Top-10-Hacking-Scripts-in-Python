# phishing_detection.py
import http.client
import re

# A list of words that could indicate a phishing page
KEYWORDS = ["password", "credit card", "bank account"]

def fetch_page(url):
    conn = http.client.HTTPSConnection(url)
    conn.request("GET", "/")
    response = conn.getresponse()
    return response.read().decode()

def is_phishing_page(html_content):
    for keyword in KEYWORDS:
        if re.search(keyword, html_content, re.I):  # re.I makes the search case-insensitive
            return True
    return False

def check_page(url):
    html_content = fetch_page(url)
    if is_phishing_page(html_content):
        print(f"WARNING: The page at {url} may be a phishing page!")
    else:
        print(f"The page at {url} does not appear to be a phishing page.")

# Example usage:
check_page("localhost:8080")
