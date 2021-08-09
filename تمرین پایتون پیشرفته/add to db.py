import mysql.connector
import regex as re
cnx = mysql.connector.connect(user=input('user to SQL: '), password=input('password to SQL: '),
                              host=input('host: '),
                              database= input('database name: ') )
cursor = cnx.cursor()

regex = r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

query = ("INSERT INTO data(username , password) VALUES(%s,%s)")

while True:
    var = (input('username: '),input('password: '))
    if (re.search(regex,var[0])):
        cursor.execute(query, (var[0],var[1] ))
        cursor.fetchall()
        break
    else:
        print("Invalid Email corret type is expression@string.string")
        continue

cnx.commit()
cursor.close()
cnx.close()

