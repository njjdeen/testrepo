'''

This file prompts for a ZIP code and uses this to obtain 15-day weather forecast from Weather.com

'''


import bs4
import requests
from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


#use chrome webdriver to let user search for zip code
chrome_options = Options()
chrome_options.add_argument("--headless")
d = webdriver.Chrome(chrome_options=chrome_options)
url = "https://weather.com/weather/tenday/l/99b09a6443608f513a37ae7d163acc4bcb20640058c77d0741beceb4f5993165"
d.get(url)

Zip_Code = input("please provide the zip/postal code of your area: ") #ask user for ZIP code input


searchbar_location = d.find_element_by_id("LocationSearch_input")
query = searchbar_location.send_keys(Zip_Code)
time.sleep(2)
searchbar_location.send_keys(Keys.ENTER)



test = 5



print("\n"*5)



res = requests.get(d.current_url)

soup = bs4.BeautifulSoup(res.text, 'lxml')

weather_location = soup.select(".styles--locationName--DD-D9")
weather_location = weather_location[0].getText()




print(f"The weather in {weather_location} for the next days:\n\n")

# dates
days = soup.select(".DetailsSummary--daypartName--2FBp2")

#max and min temperature
maxtemp = soup.select(".DetailsSummary--highTempValue--3Oteu")
mintemp = soup.select(".DetailsSummary--lowTempValue--3H-7I")


# general forecast of the day in couple of words
general_forecast = soup.select('.DetailsSummary--extendedData--365A_')


#chance of precipitation

#precip_chance = soup.find_all('span', attrs = {'data-testid' : "PercentageValue"})
precip_chance = soup.select(".DailyContent--value--37sk2")

#humidity

additional_info = soup.select('.DetailsTable--value--1q_qD')

#wind strength and direction

wind = soup.select(".Wind--windWrapper--3aqXJ.undefined")

index_general = 0
index_precip = 0
index_humid = 0
index_sunrise = 2
index_sunset = 3

for daynum in range(len(days)):
    print(days[daynum].getText())
    
    print(f"Max temp: {maxtemp[daynum].getText()}")
    print(f"Min temp: {mintemp[daynum].getText()}")
    
    print(general_forecast[index_general].getText())
    index_general = index_general + 2
    
    print(f"Precipitation chance: {precip_chance[index_precip].getText()}")
    index_precip = index_precip + 4
    
    print(f"Humidity: {additional_info[index_humid].getText()}")
    index_humid = index_humid + 8
    
    print(f"sunrise at {additional_info[index_sunrise].getText()}")
    index_sunrise = index_sunrise + 8
    
    print(f"sunset at {additional_info[index_sunset].getText()}")
    index_sunset = index_sunset + 8
    
    print(f"wind: {wind[daynum].getText()}")
    
    print("--------------------")

'''
for percentage in precip_chance:
    
    print(percentage.getText())
    
print("\n"*100)

for humid in additional_info:
    
    print(humid.getText())
    
'''