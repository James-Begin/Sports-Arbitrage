import requests
import json
from dateutil import parser
import time
import pandas as pd
import os
from sys import exit

# The Odds API can be found at https://the-odds-api.com/
# API keys are free and allow for 500 API calls per month.
# Most of the code for calling the API can be found in the Docs: https://the-odds-api.com/liveapi/guides/v4/

# Define API keys and inputs for the Odds API
API_KEY = '81e0c976af3d0965966235cfed123347'
SPORT = 'upcoming'
REGIONS = 'us'
MARKETS = 'h2h'
ODDS_FORMAT = 'decimal'
DATE_FORMAT = 'iso'

# initalize variables
odds_response = 0
regionchoice = 0
sportchoice = 0

# Call the 'sport' key and get a list of in season sports and to make sure the API currently works
sports_response = requests.get(
    'https://api.the-odds-api.com/v4/sports',
    params={
        'api_key': API_KEY
    }
)

print("Welcome to the Sportsbook!")
time.sleep(1)
print("Warning: There may be no odds available during sports off seasons.")
time.sleep(1)

# choose sport
print("Choose a sport: ")
time.sleep(1)


while sportchoice < 1 or sportchoice > 13:
    sportchoice = int(input("1: Basketball (NBA) \n2: Baseball (MLB) \n3: Ice Hockey (NHL) \n4: Football (NFL) \n5: College Football (NCAAF)\n"
                            +"6: Soccer (MLS)\n7: Canadian Football (CFL)\n8: Aussie Football (AFL)" +
                            "\n9: Women's Basketball (WNBA)\n10: Cricket (T20)\n11: Soccer (EPL)\n12: Soccer (UEFA)\n"))

# call the API with sports chosen. The keys and names of the sports can be found at https://the-odds-api.com/liveapi/guides/v4/#example-request
if sportchoice == 1:
    odds_response = requests.get(
        f'https://api.the-odds-api.com/v4/sports/basketball_nba/odds',
        params={
            'api_key': API_KEY,
            'regions': REGIONS,
            'markets': MARKETS,
            'oddsFormat': ODDS_FORMAT,
            'dateFormat': DATE_FORMAT,
        }
    )
elif sportchoice == 2:
    odds_response = requests.get(
        f'https://api.the-odds-api.com/v4/sports/baseball_mlb/odds',
        params={
            'api_key': API_KEY,
            'regions': REGIONS,
            'markets': MARKETS,
            'oddsFormat': ODDS_FORMAT,
            'dateFormat': DATE_FORMAT,
        }
    )
elif sportchoice == 3:
    odds_response = requests.get(
        f'https://api.the-odds-api.com/v4/sports/icehockey_nhl/odds',
        params={
            'api_key': API_KEY,
            'regions': REGIONS,
            'markets': MARKETS,
            'oddsFormat': ODDS_FORMAT,
            'dateFormat': DATE_FORMAT,
        }
    )
elif sportchoice == 4:
    odds_response = requests.get(
        f'https://api.the-odds-api.com/v4/sports/americanfootball_nfl/odds',
        params={
            'api_key': API_KEY,
            'regions': REGIONS,
            'markets': MARKETS,
            'oddsFormat': ODDS_FORMAT,
            'dateFormat': DATE_FORMAT,
        }
    )
elif sportchoice == 5:
    odds_response = requests.get(
        f'https://api.the-odds-api.com/v4/sports/americanfootball_ncaaf/odds',
        params={
            'api_key': API_KEY,
            'regions': REGIONS,
            'markets': MARKETS,
            'oddsFormat': ODDS_FORMAT,
            'dateFormat': DATE_FORMAT,
        }
    )
elif sportchoice == 6:
    odds_response = requests.get(
        f'https://api.the-odds-api.com/v4/sports/soccer_usa_mls/odds',
        params={
            'api_key': API_KEY,
            'regions': REGIONS,
            'markets': MARKETS,
            'oddsFormat': ODDS_FORMAT,
            'dateFormat': DATE_FORMAT,
        }
    )
elif sportchoice == 7:
    odds_response = requests.get(
        f'https://api.the-odds-api.com/v4/sports/americanfootball_cfl/odds',
        params={
            'api_key': API_KEY,
            'regions': REGIONS,
            'markets': MARKETS,
            'oddsFormat': ODDS_FORMAT,
            'dateFormat': DATE_FORMAT,
        }
    )
elif sportchoice == 8:
    odds_response = requests.get(
        f'https://api.the-odds-api.com/v4/sports/aussierules_afl/odds',
        params={
            'api_key': API_KEY,
            'regions': REGIONS,
            'markets': MARKETS,
            'oddsFormat': ODDS_FORMAT,
            'dateFormat': DATE_FORMAT,
        }
    )
elif sportchoice == 9:
    odds_response = requests.get(
        f'https://api.the-odds-api.com/v4/sports/basketball_wnba/odds',
        params={
            'api_key': API_KEY,
            'regions': REGIONS,
            'markets': MARKETS,
            'oddsFormat': ODDS_FORMAT,
            'dateFormat': DATE_FORMAT,
        }
    )
elif sportchoice == 10:
    odds_response = requests.get(
        f'https://api.the-odds-api.com/v4/sports/cricket_international_t20/odds',
        params={
            'api_key': API_KEY,
            'regions': REGIONS,
            'markets': MARKETS,
            'oddsFormat': ODDS_FORMAT,
            'dateFormat': DATE_FORMAT,
        }
    )
elif sportchoice == 11:
    odds_response = requests.get(
        f'https://api.the-odds-api.com/v4/sports/soccer_epl/odds',
        params={
            'api_key': API_KEY,
            'regions': REGIONS,
            'markets': MARKETS,
            'oddsFormat': ODDS_FORMAT,
            'dateFormat': DATE_FORMAT,
        }
    )
elif sportchoice == 12:
    odds_response = requests.get(
        f'https://api.the-odds-api.com/v4/sports/soccer_uefa_nations_league1/odds',
        params={
            'api_key': API_KEY,
            'regions': REGIONS,
            'markets': MARKETS,
            'oddsFormat': ODDS_FORMAT,
            'dateFormat': DATE_FORMAT,
        }
    )
if odds_response.status_code != 200:
    print(f'Failed to get odds: status_code {odds_response.status_code}, response body {odds_response.text}')
    exit()
#collect odds data
bookies = []
oddsa = []
oddsb = []

odds = odds_response.json()
# The json containing the odds is a list of dictionaries that contain data on upcoming games.
# Each element in the list is an individual game
if len(odds) == 0:
    print("No matches coming up")
else:

    print('Number of events in the near future:', len(odds))

    nextgames = int(input(f"How many games do you want to view? | 1 -> {str(len(odds))}" + "\n"))

    for i in range(nextgames):

        # indent the json, making it easier to read and iterate through one game at a time
        oddsJson = json.dumps(odds[i], indent=4)
        odds_json = json.loads(oddsJson)

        # iterate through the different bookies and collect odds data
        # this is all the same game, so we dont need to store a list of team names
        for k in range(len(odds_json["bookmakers"])):
            bookie = odds_json["bookmakers"][k]["title"]

            bookies.append(bookie)

            odd1 = odds_json["bookmakers"][k]['markets'][0]['outcomes'][0]['price']
            oddsa.append(odd1)
            team1 = odds_json["bookmakers"][k]['markets'][0]['outcomes'][0]['name']

            odd2 = odds_json["bookmakers"][k]['markets'][0]['outcomes'][1]['price']
            oddsb.append(odd2)
            team2 = odds_json["bookmakers"][k]['markets'][0]['outcomes'][1]['name']

        # clear terminal
        os.system('cls' if os.name == 'nt' else 'clear')

        # convert odds and bookies to a pandas dataframe for looks and so everything lines up
        oddsdict = {'Bookies': bookies, team1: oddsa, team2: oddsb}
        df = pd.DataFrame.from_dict(data=oddsdict)
        print(f"{team1} vs. {team2}")
        print(df)

        # display expected win % chance
        avg_oddsa = round((1 / (sum(oddsa) / len(oddsa))) * 100, 2)
        avg_oddsb = round((1 / (sum(oddsb) / len(oddsb))) * 100, 2)

        print(f"\n{team1} expected win %: {avg_oddsa}")
        print(f"{team2} expected win %: {avg_oddsb}")

        # find surebet (formula from surebet calculator project)
        for j in range(len(oddsa)):
            for l in range(len(oddsb)):
                if (1 / oddsa[j]) + (1 / oddsb[l]) < 1:
                    stakeA = round((100 / oddsa[j]), 2)
                    stakeB = round((100 / oddsb[l]), 2)
                    print(
                        f"\nSurebet Found: Bet ${stakeA} on {team1} on {bookies[j]} and ${stakeB} on {team2} on {bookies[l]} to earn $100")
                    print(f"Expected Riskless Profit: {round((1 - ((1 / oddsa[j]) + (1 / oddsb[l]))) * 100, 2)}%\n")
        # print the date the game takes place
        date = odds_json["commence_time"]
        date = parser.isoparse(date)
        print("\nDate (UTC): " + str(date)[0:19] + "\n")

        user_next = None

        while user_next != "" and user_next != "q":
            user_next = input("Press Enter to view next or Q to exit\n")

        if user_next == "q":
            exit()

        bookies = []
        oddsa = []
        oddsb = []




print('Remaining requests', odds_response.headers['x-requests-remaining'])
print('Used requests', odds_response.headers['x-requests-used'])
