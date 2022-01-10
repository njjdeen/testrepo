'''

PDF and excel exercise

'''

#import packages
import PyPDF2
import csv
import requests
import bs4
import re


data = open('find_the_link.csv', encoding = 'utf-8')

csv_data = csv.reader(data)

data_lines = list(csv_data)

L = len(data_lines)

i = 0
link = ''
for line in data_lines:
    
    link = link + line[i]
    i = i + 1
    
print(link)

#download pdf from google drive using the link

res = requests.get(link)

soup = bs4.BeautifulSoup(res.text, 'lxml')

text = soup.getText()

## open pdf file in own directory

f = open("Find_the_Phone_Number.pdf", 'rb')

pdf_reader = PyPDF2.PdfFileReader(f)

numpages = pdf_reader.numPages

pattern = r'\d{3}.\d{3}.\d{4}'

for pagenumber in range(numpages):
    
    page = pdf_reader.getPage(pagenumber)

    text = page.extractText()
    
    #print(text)

    for match in re.findall(pattern,text):
            
        print(f"Phone number found: {match}")
        print("\n")
        print(f"found on page {pagenumber}")
        
        
        
        
    
    

