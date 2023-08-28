# Stock Portfolio Analysis
Portfolio analysis is an area of investment management that allows investors and fund managers to assess or evaluate a collection of investments. In this project, I examined five tech stocks and a stock index, focusing on Apple, Google, Tesla, Microsoft, Meta, and the Nasdaq-100 index as tracked by the Invesco QQQ ETF.

The main objective was to compare the statistical metrics of each asset, build an equally weighted stock portfolio and compare its performance to the QQQ ETF. For the analysis, I downloaded historical stock data from 2015 to 2022 from yahoo finance using the yfinance python library. I also used log returns to compute the metrics because it takes into account the compounding effect of returns.

## Key Takeaways

* Tesla had the highest annual return among individual assets, however it was also the most volatile asset in  period.
* Microsoft had the highest sharpe ratio among all the stocks since it was the least volatile and had the second-highest return.
* While most stocks declined in 2022, Meta stock experienced a drawdown of about 77%.
* The longest drawdown period, lasting 566 days, was experienced by Tesla.
* The equal weight porfolio had a gross return of about 490%, however it was more volatile when compared to the Nasdaq-100 index.

I used [Dash]("https://plotly.com/dash/"), a Python framework for creating data apps, to create a stock comparison dashboard so that it would be easier to compare the metrics of various stocks. The app uses a list of SP500 stocks obtained from [wikipedia]("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"), and each stock's historical data is downloaded from Yahoo Finance for metrics computation and visualisation.

The dashboard consists of 4 main components:
1. A dropdown menu to search or select from a list of stock symbols.
2. A plotly graph to show different plots of the historical data and rolling statistics.
3. A collection of radio buttons to choose different plot options.
4. A table to show a summary of the computed metrics for selected stocks.

The app is currently hosted on [render]("render.com"), and it can be accessed via this [link]("https://stock-comparison-dashboard.onrender.com").