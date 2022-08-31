# Sports Arbitrage

Due to the recent legalization of sports betting in the US and Canada, Sports betting sites and markets are very fragmented. With many different sites and services that offer sports odds, there are plenty of opportunities to profit off their inefficencies. Currently, there are around 50 different online sportsbooks in the US that offer odds for a myriad of different sports. This project is a basic attempt to find arbitrage opportunities using readily available odds data in python.

## How it Works
In this case, the method of arbitrage is similar to Pure arbitrage in traditional financial markets. Pure arbitrage usually consists of buying and selling a security simultaneously on different markets to profit from the difference. In a similar fashion, sports arbitrage usually involves betting that a team will win on one sportsbook, and betting that the opposing team will lose on a different sportsbook. Then, profiting no matter who wins or loses.

This project currently only uses two way odds. 
The formula for finding a arbitrage bet is (1/A) + (1/B) < 1, where A and B are the decimal odds of opposing teams.
The way that this works is by finding the cost to earn a fixed amount, in this case $1. By dividing 1 by the odds, we find the cost to earn $1 or how much you would need to bet to earn back $1 when you win. If we sum the cost to earn $1 for both sides of the bet and it is less than $1, then there is opportunity for guaranteed profit.

So, to search for these arbitrage bets, we compare every odd on every sportsbook for every game and apply the above formula. This method has a time complexity of O(n^2) for each game where n is the number of odds. With many games and sportsbooks, this can be slow and there is room for improvement. 
For example, instead of iterating through every odd, we instead find the highest and lowest and compare those instead.

### Disclaimer
This should not be used for financial purposes, it is simply a cool project to test my python skills and explore some interesting topics in finance and math.

