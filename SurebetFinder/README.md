# Sure Bet Finder
## This should not be used to bet on sports, Odds could be incorrect or delayed. For educational purposes only

This project uses [The Odds API](https://the-odds-api.com/) to gather odds on sports. While The Odds API supports popular sports around the world, this project only includes major US sports. The API key included is limited to 500 calls per month, and a new key can be generated for free on their website.

# Logic
The logic behind this project is simple. The user chooses a sport and the API is called.  
The API responds with a JSON containing data about bookmakers, teams, times, and odds. 
Only the odds, bookmakers, teams, and dates are collected.  
Next, by iterating through the odds for each team and finding the average odds, the expected win % can be determined. 
Then, surebets can be found by comparing odds across different bookmakers. Usually, the potential gain from surebets are small and can be less than 1%. 
  
Overall, this was a project to test my python abilities and create a fun, semi-useful tool.
