import mysql.connector
import regex as re
from bs4 import BeautifulSoup 
import requests
names = list()
prices = list()
miles = list()
wat_car = list()
n = int(input('how many pages wnat to search? '))
#phase 2 find 20 cars

print('insert the 20 cars: ')
for x in range(20):
    what = input()
    wat_car.append(what)

# phase 1 finding all cars

for page in range(n):

    r = requests.get('https://www.truecar.com/used-cars-for-sale/listings/' + 'page=' + str(page) )

    soup = BeautifulSoup(r.text , 'html.parser')

    cars_names = soup.find_all('span' , attrs = {'class' : 'vehicle-header-make-model text-truncate'} )

    mile_cars = soup.find_all('div' , attrs = {'data-test' : 'vehicleCardPricingBlockPrice'} )
    
    price_cars = soup.find_all('div' , attrs = {'data-test' : 'vehicleMileage'} )
    
    for name in cars_names:
        names.append(re.sub(r'\s+' , ' ' , name.text).strip())
    for mile in mile_cars:
        miles.append(re.sub(r'\s+' , ' ' , mile.text).strip())
    for price in price_cars:
        prices.append(re.sub(r'\s+' , ' ' , price.text).strip())

# phase 3 add cars in DB
cnx = mysql.connector.connect(user=input('user: '), password= input('password: ') , host= input('Host: ') , database= input('database name: ') )
cursor = cnx.cursor()

query = ("INSERT INTO cars(name , mile , price) VALUES(%s,%s,%s)")

for i in range(len(wat_car)):
    if wat_car[i] in names:
        cursor.execute(query, (names[i] , prices[i] , miles[i] ) )


cnx.commit()
cursor.close()
cnx.close()  
print('check your DataBase')

'''
exampls:
Kia Optima
Toyota Camry
Kia Soul
Jeep Wrangler
Mercedes-Benz CLA
Nissan Rogue
Chevrolet Malibu
Lincoln MKC
Dodge Grand Caravan
Hyundai Elantra
Toyota Camry
Nissan Rogue
Toyota Corolla
Hyundai Elantra
Chrysler 300 
Chrysler 300 
Honda Civic
Mercedes-Benz C-Class
Chevrolet Silverado 1500
Ford Escape
'''
#ALTER USER 'root'@'localhost' IDENTIFIED BY 'new_password';
#delete from cars;