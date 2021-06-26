# Surfs Up with SQLAlchemy

## Overview of the Analysis
This project was completed to give a client more information before they pursued a business endeavor. The client wanted to know about the weather trends in the city that they're opening up a surf shop in. In order to give them this information, I preformed queries to provide them with summary statistics for the weather in June and December to see if their business will be viable throughout the year. 

## Results
There were two summary tables created. The first table (seen below) shows summary statistics for the weather in June.

![June Temperature](https://github.com/naomishields/surfs_up/blob/main/Resources/june_Temps.png)

The second deliverable (seen below) gives us the summary statistics for the weather in December.

![December Temperature](https://github.com/naomishields/surfs_up/blob/main/Resources/dec_Temps.png)

Based on the two tables we can see that:
* June has an average temperature of 74.94 and December has an average temperature of 71.04. 
* The min temperature for June was 64 and the min temperature was 56 for December.
* The IQR for June was 4 degrees and the IQR for December was 5 degrees. 

## Summary 
Overall, there is not such a drastic differences in the summary statistics for June and December, so I think that indicates that the business would be sustainable year-round. June's average temperature was only 3.9 degrees higher than December's average temperature, which is not huge difference when comparing a summer month to a winter month. However, December's lowest temperature was 8 degrees colder than June's lowest temperature, which indicates that it can get significantly colder in December. Then, when looking at the IQR'S we can see that the temperature in December varies just a little bit more than it does in June, but again it's not significantly different. 


Additional Queries:
* Provide a count for the average number of times the temperature was below 60 degrees in December. I think this would be helpful to see how often it gets cold in Decemeber so the client has a general idea of what to expect.
* Pull the summary statistics for January or February since those are also cold months. I think this could also be helpful because December is not always the coldest month of the year, so it would be useful to pull data from other cold months. 
