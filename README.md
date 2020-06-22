# StockItUp

## Introduction: 

Stock data is one of the resources that is widely used and is in demand. It can be utilized in several ways to provide insightful information in various aspects. There are numerous stand-alone approaches by individuals to address each use case. StockItUp aims to bridge this gap by providing an easy to use single infrastructure, where data can be manipulated in any way which would facilitate any use case. 

StockItUp is a unified streaming pipeline to process historical as well as real-time stock data to provide insightful dashboards to rookie investors and also to provide clean, processed, critical features to data scientists on-demand. Another important business aspect that StockItUp addresses is that it eliminates the need for an external data warehouse, making this a data warehouse-less infrastructure. 


## The Unified Approach:

StockItUp utilizes a single tool called Apache Pulsar, a pub/sub messaging system where data from the data source is ingested and making use of Pulsar functions, the data is processed and stored in another topic. By setting up appropriate retention period threshold either by setting up a time or ledger size, the data is then offloaded to an external object storage service like s3. Towards the end, utilizing pulsar SQL, data can be queried from the cluster as well as from s3, to satisfy front end query demands. This facilitates the data requirements for data scientists and also for a front end which provides an insightful dashboard for rookie investors. 

### Typical tech stack:

![TypicalTechStack](https://github.com/govardhan1194/StockItUp/images/Typical tech stack.PNG)

A typical tech stack for a project like this would look like this where there is a data source and the data is ingested by kafka and processed by spark streaming and so on and so forth. But if you look at this infrastructure , there are a lot of tools interacting with one another and there are a lot of complications
