import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

bollywood_base_url = 'http://103.213.238.85:8090/bollywood/'
hollywood_base_url = 'http://103.213.238.85:8090/hollywood/'
web_series_base_url = 'http://103.213.238.85:8090/tv-series/'

movie_type = input("(1)Bollywood\n(2)Hollywood\n(3)Web series\nEnter your choice: ")

if movie_type == '1':
    base_url = bollywood_base_url + input("Enter year: ")
elif movie_type == '2':
    base_url = hollywood_base_url + input("Enter year: ")
elif movie_type == '3':
    base_url = web_series_base_url

response = requests.get(base_url)
soup = BeautifulSoup(response.content, 'html.parser')

movie_name = input("Enter the movie name: ")
found = False

for link in soup.find_all('a'):
    if movie_name in link.text:
        new_url = urljoin(f'{base_url}/', link['href'])
        print(f"If you are searching the web series click on this link {new_url}")
        response = requests.get(new_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        for link in soup.find_all('a'):
            href = link.get('href')
            if href.endswith('.mp4') or href.endswith('.avi') or href.endswith('.mkv'):
                absolute_link = urljoin(new_url, href)
                print(absolute_link)
                found = True


if not found:
    print(f"No results found for '{movie_name}'.")
