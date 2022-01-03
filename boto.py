from datetime import datetime
import boto3
import psycopg2 as pg
import dotenv
import os
import pgres
import pandas as pd
##boto file

from dotenv import load_dotenv

load_dotenv()

AWSKEY = os.environ.get("AWSKEY")
AWSPASS = os.environ.get("AWSPASS")
AWSREGION = os.environ.get("AWSREGION")


client = boto3.client('s3')



s3 = boto3.resource(
    service_name = 's3',
    region_name = AWSREGION,
    aws_access_key_id = AWSKEY,
    aws_secret_access_key = AWSPASS
)


import time
import datetime

con = pg.connect(host = 'localhost', database = 'rentals' , user = pgres.USER , password= pgres.KEY )
cur = con.cursor()

full_data = 'SELECT * FROM totals'
cur.execute(full_data)
records = cur.fetchall()
dict = {'2021': records}
xb = 'medianrent.xlsx'.format(datetime.date)
xl = pd.DataFrame.to_excel(pd.DataFrame.from_dict(dict),xb)

s3.Bucket('randomfrozenbucket').upload_file(xb,'{}medianAskingRent_Studio.xlsx'.format(str(datetime.date.today())))
os.remove(xb)
con.commit()
cur.close()
con.close()