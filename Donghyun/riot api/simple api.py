# simple api.py

import requests
import json

# VARIABLES
api_key = "RGAPI-4c24c9f3-ed04-43a1-9048-7646968179d1"

# CONSTANT VALUES
https = "https://"
# Routing Values
# platform
ROUTING_NA1 = "na1.api.riotgames.com"
ROUTING_KR = "kr.api.riotgames.com"
# regional
ROUTING_americas = "americas.api.riotgames.com"
ROUTING_asia = "asia.api.riotgames.com"


if __name__ == "__main__":
    game_name = "Zenocider72"

    # puuid
    url_key = "/lol/summoner/v4/summoners/by-name/"
    url = https + ROUTING_NA1 + url_key + game_name + "?api_key=" + api_key
    req = requests.get(url)

    if req.status_code == 200:
        summoner = json.loads(req.text)
        print(type(summoner["puuid"]))
    else:
        print("req.status_code:", req.status_code)
