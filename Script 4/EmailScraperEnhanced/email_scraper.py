# Import necessary libraries
import re
from bs4 import BeautifulSoup

def scrape_emails(file):
    try:
        # Open the local HTML file
        with open(file, 'r') as file:
            content = file.read()

        # Parse the HTML content
        soup = BeautifulSoup(content, 'html.parser')

        # Improve the regular expression for finding emails
        email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        emails = re.findall(email_regex, str(soup))

        # Print all found emails
        print(emails)

    except Exception as e:
        print(f"An error occurred: {e}")

# Ask the user to input the filename
file = input("Enter the name of the HTML file: ")
scrape_emails(file)