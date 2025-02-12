import requests
import bs4 as bs


# get the page
url = 'https://en.wikipedia.org/wiki/COVID-19_pandemic_by_country_and_territory'

response = requests.get(url)

# parse the page
soup = bs.BeautifulSoup(response.text, 'html.parser')

# get the table
table = soup.find('table', class_='wikitable')

# get the rows
rows = table.find_all('tr')

# get the headers
headers = rows[0].find_all('th')

# get the data
data = []

for row in rows[1:]:
    data.append([cell.text for cell in row.find_all('td')])

# print the data
for row in data:
    print(row)