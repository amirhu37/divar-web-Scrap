import mysql.connector

cnx = mysql.connector.connect(user=input('username: '), password=input('username: '),
                              host=input('host: '),
                              database= input('database name: '))
cursor = cnx.cursor()

sorting = 'SELECT * FROM peaple ORDER BY height DESC, weight ASC'
cursor.execute(sorting)
 
result = cursor.fetchall()
#print(result)
#print(150*'-')
for row in result:
    print(row[0],row[2], row[1])
    #print("\n")

cnx.close()

#ALTER USER 'root'@'localhost' IDENTIFIED BY 'new_password';