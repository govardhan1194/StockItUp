# A script to show that python can be used for querying the pulsar cluster using pulsarSQL
import prestodb
import schedule
import time
from datetime import datetime

# A function to query presto every 10 seconds 
def queryjob():

        conn=prestodb.dbapi.connect(
                host='ec2-54-186-138-107.us-west-2.compute.amazonaws.com',
                port=8080,
                user='Govi')
        cur = conn.cursor()
        cur.execute('SELECT mnemonic,avg(profitorloss) FROM pulsar."public/default".ProcessedData group by mnemonic')
        rows = cur.fetchall()
        

schedule.every(10).seconds.do(queryjob)

while 1:
        schedule.run_pending()
        time.sleep(1)

