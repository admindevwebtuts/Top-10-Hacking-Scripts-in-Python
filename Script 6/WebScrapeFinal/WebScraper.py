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
    titles = soup.find_all('h4')
    authors = soup.find_all(class_='card-text')

    data = ""
    for i in range(len(titles)):
        data += f"Title: {titles[i].text}, Author: {authors[i].text}\n"

    save_to_file(data, 'blog_data.txt')