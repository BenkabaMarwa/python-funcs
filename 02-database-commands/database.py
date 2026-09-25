import sqlite3

database=sqlite3.connect("database.db")
cursor= database.cursor()

#create table
cursor.execute("create table if not exists database(id, password)")

# insert value into table
id=1
password="stay_save"
cursor.execute(f""" insert into database values ("{id}","{password}")""")
database.commit()

#read values from database
cursor.execute("select * from database")
data= cursor.fetchall()
print(data)

#update data
cursor.execute(f""" update database set password="stay_save" where password="password" """)
database.commit()

#delete line from database
cursor.execute(f""" delete from database where id="{id}" """)
database.commit()




