## Title: TRADER PERFORMANCE VS MARKET SENTIMENT ANALYSIS

>> Objective <<
In order to analyze the impact of Bitcoin’s market sentiment (Fear/Greed Index) on the profitability of traders, their win rates, and their riskiness.

>> Dataset <<
** Fear & Greed Index (Market Sentiment)
** Historical Trader Data - Hyperliquid

>> Tech Stack <<
* Python
* Pandas
* Matplotlib
* Seaborn

>> Methodology <<
1. Data Cleaning and Standardization
2. Converted time stamps to datetime format and standardized dates
3. Merging Data on Common Date
4. Conducted Grouped Analysis Based on Sentiment Data
4. Evaluated Data:
5. Average PnL
6. Win Rate
7. Trade Size (Riskiness)

>> Key Insights <<
1. Extreme Greed has the highest profitability (~67.9 PnL)
>> Traders are most successful in high-bullish markets
2. Fear phase has higher profitability (~54.3 PnL) than Greed (~42.7 PnL)
>> There are opportunities for profitable trading during corrections
3. The win rate is the highest during the Extreme Greed phase (~46%)
>> Bullish momentum makes trading more successful
4. The highest risk is taken during the Fear phase (~7816 USD position size)
>> This could be due to dip buying
5. The Neutral and Extreme Fear markets have the lowest performance (~34 PnL)
>> There are fewer opportunities, or it’s too uncertain

>> Conclusion <<
Market sentiment plays a crucial role in the behavior and performance of traders.
Extreme Greed is the major contributor to profitability and success rates, while Fear results in high-risk trades.
These findings emphasize the need to include sentiment as a feature in trading strategies.

>> Scope <<
The sentiment feature can be added to the predictive model.
