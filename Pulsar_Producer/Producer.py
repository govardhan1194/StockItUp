#These are the required modules to be imported.
import boto3
import pandas as pd
import pulsar
from pulsar.schema import *
from schemas import Stock

client = pulsar.Client('pulsar://localhost:6650')

producer = client.create_producer('StockItUp-topic',AvroSchema(Stock))

s3 = boto3.resource('s3', aws_access_key_id = '', aws_secret_access_key = '')

bucket = s3.Bucket('deutscheboercestockitup')

for object in bucket.objects.all():
    
    #Eliminating empty csv files which are of 136 bytes of size.
    if object.size > 136:
        url = 'https://deutscheboercestockitup.s3-us-west-2.amazonaws.com/' + object.key
        data = pd.read_csv(url)
        
        #read through each line of csv and send the line to the pulsar topic
        for index, row in data.iterrows():
            '''
            output = ''
            for element in row:
                    output = output + str(element) + ","
            producer.send(output.encode('utf-8'))
            '''
            #instead of sending out as bytes, utilizing a custom schema to send as an AvroSchema
            output = Stock(Mnemonic = row["Mnemonic"],SecurityType = row["SecurityType"],Currency = row["Currency"],
                           Date = row["Time"],StartPrice	= row["StartPrice"],MaxPrice = row["MaxPrice"],
                           MinPrice = row["MinPrice"],EndPrice = row["EndPrice"],TradedVolume = row["TradedVolume"],
                           NumberOfTrades = row["NumberOfTrades"], ProfitOrLoss = 0.0)
            producer.send(output)
