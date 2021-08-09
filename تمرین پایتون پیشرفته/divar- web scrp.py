from bs4 import BeautifulSoup 
import requests
import regex
pr =list()
ob = list() 
r = requests.get('https://divar.ir/s/tehran')

soup =BeautifulSoup(r.text , 'html.parser')

all_objs = soup.find_all('div' , attrs={'class' : "kt-post-card__title"})

all_price = soup.find_all('div', attrs={'class' : "kt-post-card__description"})

for price in all_price:
  pr.append(regex.sub(r'\s+', ' ' , price.text).strip())

for objs in all_objs:
  ob.append(regex.sub(r'\s+', ' ' , objs.text).strip())

opr = dict(zip(ob , pr))

for k, v in opr.items():
    if v == 'توافقی':
      print(k)

