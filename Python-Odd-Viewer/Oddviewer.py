import requests
import json
from dateutil import parser
import time
import pandas as pd

API_KEY = '81e0c976af3d0965966235cfed123347'
SPORT = 'upcoming'
REGIONS = 'us'
MARKETS = 'h2h'
ODDS_FORMAT = 'decimal'
DATE_FORMAT = 'iso'

sportchoice = 0
odds_response = 0

sports_response = requests.get(
    'https://api.the-odds-api.com/v4/sports',
    params={
        'api_key': API_KEY
    }
)

if sports_response.status_code != 200:
    print(f'Failed to get sports: status_code {sports_response.status_code}, response body {sports_response.text}')

print("Welcome to the Sportsbook!")
time.sleep(1)
print("Warning: There may be no odds available during sports off seasons.")
time.sleep(1)
print("Choose a sport: ")
time.sleep(0.5)

while sportchoice < 1 or sportchoice > 4:
    sportchoice = int(input("1: Basketball (NBA) | 2: Baseball (MLB) | 3: Ice Hockey (NHL) | 4: Football (NFL)" + "\n"))



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



if odds_response.status_code != 200:
    print(f'Failed to get odds: status_code {odds_response.status_code}, response body {odds_response.text}')

else:

    bookies = []
    oddsa = []
    oddsb = []

    odds = odds_response.json()
    if len(odds) == 0:
        print("No matches in next 24 hours")
    else:

        print('Number of events in the next 24 hours:', len(odds))

        nextgames = int(input(f"How many games do you want to view? | 1 -> {str(len(odds))}" + "\n"))


        for i in range(nextgames):
            oddsJson = json.dumps(odds[i], indent=4)
            odds_json = json.loads(oddsJson)
            for k in range(len(odds_json["bookmakers"])):


                bookie = odds_json["bookmakers"][k]["title"]

                bookies.append(bookie)

                odd1 = odds_json["bookmakers"][k]['markets'][0]['outcomes'][0]['price']
                oddsa.append(odd1)
                team1 = odds_json["bookmakers"][k]['markets'][0]['outcomes'][0]['name']

                odd2 = odds_json["bookmakers"][k]['markets'][0]['outcomes'][1]['price']
                oddsb.append(odd2)
                team2 = odds_json["bookmakers"][k]['markets'][0]['outcomes'][1]['name']



            oddsdict = {'Bookies': bookies, team1: oddsa, team2: oddsb}
            df = pd.DataFrame.from_dict(data=oddsdict)
            print(df)

            bookies = []
            oddsa = []
            oddsb = []





            date = odds_json["commence_time"]
            date = parser.isoparse(date)
            print("\nDate (UTC): " + str(date)[0:19] + "\n")



print('Remaining requests', odds_response.headers['x-requests-remaining'])
print('Used requests', odds_response.headers['x-requests-used'])






