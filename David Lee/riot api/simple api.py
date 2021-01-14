# simple api.py

import requests
import json

# VARIABLES
api_key = "RGAPI-5c856f87-4ece-453b-823d-05ec5cbf6fdc"

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
        print(json.dumps(summoner, indent="    "))
    else:
        print("req.status_code:", req.status_code)
