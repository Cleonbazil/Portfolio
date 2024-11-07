## Search Traffic Analysis

**In this challenge we are trying to explore the data in tow tracks:**
- **The first using the pandas,numpy and matplotlib libraries.**
- **The Second utilizing the Prophet library.**

**Each path attempts to bring clarity to interesting aspects of the data set by answering various questions**

## First Track:

### Search trends EDA
**After reading in the data set we calculate the total search traffic for the month, and then compare the value to the monthly median across all months.** 
**The figures show that in November 2020 search traffic reaches its highest level to then dip,rise and drop to its lowest in August 2020.**
**The month of May is of particular interest to the client, in this month search traffic shows an increase above the median compared to the previous month**
**but below the overall max.**

**In this next step the seasonality of the trends is explored:**
**The figures show that in the hourly trend the most searches happen around midnight with a downward trend up until 11:00am to then rise.**
**In weekdays the highest point is on Modays to then tapper of sharply to the weekend**
**The yearly observations show a choppy downward trend.**

### Stock closing price
**In this exploration one of the most salient aspects is the company's stock price and its relation to the search trends, we start by looking at its overall**
**behavior throughout the dataset, we can readily observe an upward trend with a sharp increase in 2020, for this reason there is particular focus time period**
**spanning from January to June where the stock price has a moderate climb towards after a decline in the preceeding months. The seach tendendies are choppy but**
**steady within the 60/hr-20/hr range and apperently do not exhibit any correlation with the stock price.**
**To further dig into the relationship betwee stock price and search trends the features of 'Stock volatility' and 'Hourly Stock Return' are developed also the**
**search trends are shifted 'lagged' by one hour in the 'Lagged Search Trends' feature.** 
**As the table shows the correlation between searches and stock price is very week albeit with negative correlation.**

**                     **Stock Volatility	    Lagged Search Trends	Hourly Stock Return**
**Stock Volatility	       1.000000	                -0.125327	          0.030513**
**Lagged Search Trends	  -0.125327	                 1.000000	          0.017929**
**Hourly Stock Return	   0.030513	                 0.017929	          1.000000**



## Second Track
**In this section we use the prophet library to examine and visulize the data, although the process is less cumbersome the results are the confirmed.Towards the end of 2020 the search trends are in decline.**














