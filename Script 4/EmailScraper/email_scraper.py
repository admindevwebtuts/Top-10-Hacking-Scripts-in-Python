# Import necessary libraries
import re
import requests
from bs4 import BeautifulSoup

# Fetch the web page


#response = requests.get('http://localhost/test.html')
with open('G:\My Drive\Books\Devwebtuts\PythonHack\CodeExamples\Chapter6\EmailScraper\index.html', 'r') as file:
    content = file.read()

# Parse the page content

#soup = BeautifulSoup(response.text, 'html.parser')
soup = BeautifulSoup(content, 'html.parser')

# Find Emails in the Page Content
email_regex = r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+"
emails = re.findall(email_regex, str(soup))

# Print all found emails
print(emails)
