'''

Webscraping exercises


'''

#import libraries for scraping

import requests
import bs4

res = requests.get('http://quotes.toscrape.com/')
soup = bs4.BeautifulSoup(res.text, 'lxml')

#print(soup)

authors = soup.select(".author")

author_list = []

for author in authors:
    
    author_name = author.getText()
    
    author_list.append(author_name)
    

print(set(author_list))
print("\n")

##### collect all quotes
quotes = soup.select(".text")

quote_collection = []
for quote in quotes:
    
    quote = quote.getText()
    
    quote_collection.append(quote)
    
    
print(quote_collection)
print("\n")

#### collect all tags
tags = soup.select("span .tag")

tag_list = []

for tag in tags:
    
    tag = tag.getText()
    
    tag_list.append(tag)


print(tag_list)
print("\n")


