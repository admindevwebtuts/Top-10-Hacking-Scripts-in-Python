import requests
from bs4 import BeautifulSoup

url = 'https://www.devwebtuts.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

paragraphs = soup.find_all('p')
for para in paragraphs:
    print(para.text)
