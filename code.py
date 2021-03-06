
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

page = requests.get(url)
print(page)

soup = bs(page.text,'html.parser')

data = soup.find_all('table')



temp_list= []
table_rows = data[4].find_all('tr')
for tr in table_rows:

    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

print(temp_list)



stars = []
dist =[]
mass = []
radius =[]


for i in range(1,len(temp_list)):
    
    stars.append(temp_list[i][0])
    dist.append(temp_list[i][5])
    mass.append(temp_list[i][7])
    radius.append(temp_list[i][8])

df = pd.DataFrame(list(zip(stars,dist,mass,radius,)),columns=['Star_name','dist','mass','radius'])
print(df)

df2.to_csv('dwarf_stars.csv')
