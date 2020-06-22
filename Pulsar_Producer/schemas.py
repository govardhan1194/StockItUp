# A custom helper module for defining schema for the data set
from pulsar.schema import *

class Stock(Record):
    Mnemonic = String()
    SecurityType = String()
    Currency = String()
    Date = String()
    Time = String()
    StartPrice	= Float()
    MaxPrice = Float()	
    MinPrice = Float()
    EndPrice = Float()
    TradedVolume = Integer()
    NumberOfTrades = Integer()
    ProfitOrLoss = Float()
