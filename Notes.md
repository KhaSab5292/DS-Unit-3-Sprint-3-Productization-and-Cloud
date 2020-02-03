ML deployment

1.  What is deployment?
'use' it for something - use a model

Build a model

1.  ETL - 
2.  preprocessing - 
3.  EDA - 
-----------
4.  Features -
5.  pick algos
6.  baseline
7.  pick a model
8.  test and tune as needed
-----------
9.  deployment



1.  Entanglement
2.  Data dependency
3.  Configuration
4.  Data and Feature prep
5.  Detecting Model Errors
6.  Separation of expertise - working in teams


deployment design considerations:

1.  real time / batch
2.  how often will you need to update the model?
3.  traffic demand - engineering
4.  size of data 
5.  type of algos/models
6.  Can this be done without ML?
7.  

four patterns for deployment
1.  Rest API - flask (example) - batch, preds 
are on the fly

older 2.  Shared DB - batch, super high latency

3.  Streaming - streaming data, message que ( 
ingestion pipelin), preds are streamed - hig 
maintenance - super costly (relevant to project
size)

4.  Mobile (app) - streaming, preds on the fly,
processed on a device

older 5.  PMML - pred modelling markup language


Web application development