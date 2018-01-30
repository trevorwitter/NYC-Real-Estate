# NYC-Real-Estate-
Analysis of 2003-2015 NYC real estate prices

Web application running [here](http://trevorwitter.herokuapp.com/realestate)

Data obtained from [NYC.gov](http://www1.nyc.gov/site/finance/taxes/property-annualized-sales-update.page)


Annual borough sales data are combined into pandas DataFrame and grouped by neighborhood. Interactive Bokeh plots allow user to select neighborhood to compare to overall Manhattan average. 

![alt tag](https://github.com/trevorwitter/NYC-Real-Estate-/blob/master/greenwich_village_graph.tiff)



Additional variables, such as total number of sales, condos vs co-ops, property type, buiding codes and tax codes will be incorporated into analysis. 
![alt tag](https://github.com/trevorwitter/NYC-Real-Estate-/blob/master/Annual_Sales_graph.tiff)

### Next Steps
The current analysis only focuses on Manhattan; I would like to update to include all 5 boroughs. I would also like to further group sales by property type and add additional statistical measures. I developed this project primarily to get a feel for [flask](http://flask.pocoo.org) and creating interactive Bokeh plots with javascript callbacks. 

