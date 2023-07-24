import requests
from bs4 import BeautifulSoup

def save_to_file(data, filename):
    with open(filename, 'w') as file:
        file.write(data)

url = 'https://www.devwebtuts.com'

response = requests.get(url)

if response.status_code != 200:
    print("Failed to access website")
else:
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')

    text = ""
    for para in paragraphs:
        text += para.text + '\n'

    save_to_file(text, 'scraped_data.txt')