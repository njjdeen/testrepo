'''
In this document book titles are scraped from bookstoscrape.com
Only books with a 2 star rating will be listed

'''
import requests
import bs4


base_URL = 'http://books.toscrape.com/catalogue/page-{}.html'

#star_ratings = ["One", "Two", "Three", "Four", "Five"]

title_list = []

for n in range(1,51):    
    
    page = n
    
    res = requests.get(base_URL.format(page))
    
    soup = bs4.BeautifulSoup(res.text,'lxml')
    
    products = soup.select(".product_pod")
    
    
    
    print("\n all titles on this page with 2 star ratings are: \n")
    for product in products:
        
        star_rating = product.select(".star-rating.Two")
        
        #print(len(star_rating))
        
        
        #print(star_rating)
        
        title = product.select("h3 a")[0]
        
        print(title['title'])
        
        
        if len(star_rating) > 0:
            title_list.append(title['title'])
            print(title['title'])
        
        
        
    
    