# project-grizzly
Project 1 UCSD Extension Data Analytics Bootcamp

# Correlation Between Elon Musk's Twitter and Bitcoin Values
This dataset is looking to determine if Elon Musk's tweets about bitcoin, dogecoin, and/or Tesla influence the value of each coin.

Tools & Databases Used:
- Python / Jupyter
- Textblob
- Klines Binance Data Collection
- Twint

What this data will be collecting:
- All Elon Musk tweets from 2019 to 2021 using Twint.
- All Bitcoin values and trades from 2019 to 2021 using Klines Binance Data.
- All Dogecoin values and trades from 2019 to 2021 using Klines Binance Data.
 
Our methods and observation directions:
- First we'll be using Textblob to create a function that can read all the tweets and identify when selected words are being used. Is this case we'll be looking for "Telsa", "Bitcoin", "Dogecoin, and all other phrases within those categories that we identify.
- Using the new DataFrame we compared tweets containing the specific values above within a certain timeframe, to the value of bitcoin that correlates to the same timeframe. In order to improve accuracy we'll be looking between 5 and 30 minute intervals and calculating the percent change of the coin during those intervals.
- We then used 30 minutes before and after a tweet to check the trajectory of the coin value.
- Using percent change in value we created a scatter plot to show a visualization of how Elon Musk's tweets have a positive or negative influence over bitcoin value.
- Lastly we determine if there is any correlation between the quantity of tweets in a day and the quantity of trades that happened that same day.
- Dogecoin data was analyzed in the same way to test our findings against another coin.
- Tweets contining the word "Tesla" are being analyzed to determine if values of each coin changed prior to and/or after Telsa accepting bitcoin.
