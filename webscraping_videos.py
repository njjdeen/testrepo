import requests
import bs4

#grabbing page title from a website
res = requests.get("http://www.example.com")

#print(type(res))

soup = bs4.BeautifulSoup(res.text,'lxml')

#print(soup)

title_tag = soup.select("title")

#print(title_tag[0])

#use gettext() to grab just the text of title element

#print(title_tag[0].getText())




####Grab all sections headings from a website

#get request 
res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
soup = bs4.BeautifulSoup(res.text,'lxml')

#print(soup.select(".toctext"))

#all headers have class called "toctext"

for item in soup.select(".toctext"):
    print(item.getText())
    
    
##############Grab image from website

#the image is to be retrieved from a wikipedia page

res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup = bs4.BeautifulSoup(res.text, 'lxml')

image_info = soup.select('.thumbimage')

computer = image_info[0]

####print(image_info['src']) ????

image_link = computer['src'] #link to the image of the chess computer

image_request = requests.get("https:" + image_link)

content = image_request.content

#make new jpg file to write the image to on pc

f = open('my_new_file.jpg', 'wb')
f.write(content)
f.close()




    
