import mysql.connector

mydb = mysql.connector.connect(host="34.100.219.166", user="gwc2023", passwd="gwc2023")

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE gwcpmp")

#mycursor.execute("SHOW DATABASES")
#for db in mycursor:
#    print(db)
