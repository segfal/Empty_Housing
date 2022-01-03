import rental_data as rd
import rental_prices as rp
import psycopg2 as pg
import os
from dotenv import load_dotenv


load_dotenv()
USER = os.environ.get("USER")
KEY = os.environ.get("KEY")


con = pg.connect(host = 'localhost', database = 'rentals' , user = USER , password=KEY )
cur = con.cursor()

#cur.execute('CREATE DATABASE rentals')



#cur.execute('CREATE TABLE totals(date varchar(255) , Total_apartments int , avg_rent int)')
'''
for keys in rd.nyc_totals:
    insertdata = 'INSERT INTO totals VALUES({},{},{})'.format(keys,rd.nyc_totals[keys] ,rp.nyc_avg_price[keys])
    cur.execute(insertdata)
'''
    
#cur.execute('DROP TABLE totals') #just in case if the data isnt needed

full_data = 'SELECT * FROM totals'
cur.execute(full_data)
records = cur.fetchall()

#print(records)


con.commit()
con.close()
cur.close()



    