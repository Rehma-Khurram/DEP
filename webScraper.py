import requests
from bs4 import BeautifulSoup
import csv

## url of quotes website
url = 'http://quotes.toscrape.com/'
response = requests.get(url)

## Parsing the HTML content bs4
soup = BeautifulSoup(response.text, 'html.parser')

# quotes enclosed in <div> tags with class 'quote')
quotes = soup.find_all('div', class_='quote')
# listing the scraped data
quotations = []
# Looping through the quotes
for quote in quotes:
    text = quote.find('span', class_='text').text.strip()

    #  author
    authorName = quote.find('small', class_='author').text.strip()

    quotations.append([text, authorName])
# Writing into CSV file
with open('quotes.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Quote', 'Author'])

    writer.writerows(quotations)

print(f'Successfully saved {len(quotations)} quotes to quotes.csv')
