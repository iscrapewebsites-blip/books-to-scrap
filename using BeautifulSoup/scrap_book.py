from bs4 import BeautifulSoup

'''
import requests

url = 'https://books.toscrape.com'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')
soup = soup.prettify()

with open('books.html', 'w', encoding='utf-8') as file:
     file.write(soup)
'''

page = ''
with open('books.html', 'r', encoding='utf-8') as file:
     page = file.read()

soup = BeautifulSoup(page, 'lxml')

# select (CSS selector) returns a list of element
titles = soup.select('article > h3 > a')
prices = soup.select('article > div.product_price > p.price_color')
ratings = soup.select('p.star-rating')
rate_map = {"One":1, "Two":2, "Three":3, "Four":4, "Five":5}

# to print data on the terminal
'''
for t, p, r in zip(titles, prices, ratings):
     t = t['title']
     p = p.text.strip().split('Â')[1]
     r = rate_map[r['class'][1]]

     print("title: ", t)
     print("rating: ", r, "star")
     print("price: ", p)
     print()


'''

# to store data in a csv file

import csv

data = [] # list of dict
for t, p, r in zip(titles, prices, ratings):
     t = t['title']
     p = p.text.strip().split('Â')[1]
     r = rate_map[r['class'][1]]

     dict = {'title':t, 'rating':r, 'price':p}
     data.append(dict)

field_names = ['title', 'rating', 'price']
with open('book_scrap.csv', 'w', encoding='utf-8', newline='') as file:
     writer = csv.DictWriter(file, fieldnames=field_names)
     writer.writeheader()
     writer.writerows(data)




