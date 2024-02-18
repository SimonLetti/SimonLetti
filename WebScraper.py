import requests
from bs4 import BeautifulSoup

def simple_web_scraper(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            title = soup.find('title').text
            print(f"Title of the page: {title}")
            # Scrape and print the first paragraph content
            paragraph = soup.find('p').text
            print(f"First paragraph content: {paragraph}")
        else:
            print("Failed to retrieve the webpage")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = input("Enter the URL to scrape: ")
    simple_web_scraper(url)
