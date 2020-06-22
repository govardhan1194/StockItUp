# StockItUp

## Introduction: 

Stock data is one of the resources that is widely used and is in demand. It can be utilized in several ways to provide insightful information in various aspects. There are numerous stand-alone approaches by individuals to address each use case. StockItUp aims to bridge this gap by providing an easy to use single infrastructure, where data can be manipulated in any way which would facilitate any use case. 

StockItUp is a unified streaming pipeline to process historical as well as real-time stock data to provide insightful dashboards to rookie investors and also to provide clean, processed, critical features to data scientists on-demand. Another important business aspect that StockItUp addresses is that it eliminates the need for an external data warehouse, making this a data warehouse-less infrastructure. 


## The Unified Approach:

StockItUp utilizes a single tool called Apache Pulsar, a pub/sub messaging system where data from the data source is ingested and making use of Pulsar functions, the data is processed and stored in another topic. By setting up appropriate retention period threshold either by setting up a time or ledger size, the data is then offloaded to an external object storage service like s3. Towards the end, utilizing pulsar SQL, data can be queried from the cluster as well as from s3, to satisfy front end query demands. This facilitates the data requirements for data scientists and also for a front end which provides an insightful dashboard for rookie investors. 

### Typical tech stack:


![TypicalTechStack](https://github.com/govardhan1194/StockItUp/blob/master/images/Typical%20tech%20stack.PNG)


A typical tech stack for a project like this would look like this where there is a data source and the data is ingested by kafka and processed by spark streaming and so on and so forth. But if you look at this infrastructure , there are a lot of tools interacting with one another and there are a lot of complications. However, Pulsar eliminated all these complications with its inbuilt features.

### Tech stack that was implemented:


![TechStackImplemented](https://github.com/govardhan1194/StockItUp/blob/master/images/Techstackimplemented.PNG)


The data source that I am using here is called XETRA, which is the reference market for exchange trading in German shares and exchange-traded funds. 

Data is ingested from the data source into the Pulsar cluster. Pulsar functions are utilized to process the raw data ingested, for example, create new columns which indicates profit or loss, have data only during the trading hours, etc., and store them in another topic called processedData within the cluster. 

A retention period of a month is set, afterwhich data from the cluster is offloaded into s3 utilizing the Tiered storage feature of Pulsar. 

Complex queries can be executed on the available data through Pulsar SQL according to the front end queries as the data is being streamed in. Also queries can be executed to retrieve historical data from s3 for data scientists on demand. 
