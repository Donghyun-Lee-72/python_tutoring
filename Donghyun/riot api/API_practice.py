# API_practice.py

import error
import requests
import json


# VARIABLES
api_key = "RGAPI-4f62a69a-8850-435b-8590-41e02010a457"


# CONSTANT VALUES
https = "https://"
# Routing Values
# platform
ROUTING_NA1 = "na1.api.riotgames.com"
ROUTING_KR = "kr.api.riotgames.com"
# regional
ROUTING_americas = "americas.api.riotgames.com"
ROUTING_asia = "asia.api.riotgames.com"


def name2puuid(game_name):
    """
    For the given name, summoner's puuid will be returned.
    Also stores so far searched information.            // NOT IMPLEMENTED YET

    :param game_name: string; name of player in League of Legneds
    :return: string; puuid of the player
    """
    try:
        # search existing data
        with open("puuid.txt", "r") as f:
            for line in f.readlines():
                if line.split(",")[0] == game_name:
                    return line.split(",")[1]   # puuid
    except FileNotFoundError:
        pass

    # search from API
    url_key = "/lol/summoner/v4/summoners/by-name/"
    url = https + ROUTING_NA1 + url_key + game_name + "?api_key=" + api_key
    req = requests.get(url)

    if req.status_code == 200:
        puuid = req.json()["puuid"]
        with open("puuid.txt", "a") as f:
            text = game_name + "," + puuid + '\n'
            f.write(text)
        return puuid
    else:
        raise error.StatusError(req.status_code)


def puuid2account(puuid):
    pass


if __name__ == "__main__":
    # name2puuid
    # print(name2puuid("Blue City"))
    # print(name2puuid("davidfather"))

    url1 = https + ROUTING_NA1 + "/lol/summoner/v4/summoners/by-name/" + "Zenocider72" + "?api_key=" + api_key
    req1 = requests.get(url1)
    print(req1.text)

    # url2 = https + ROUTING_americas + "/riot/account/v1/accounts/by-puuid/" + "d1oDsj3pnN5B2MaN1veU1hrMHTz4O2FyiiAsitUpiE_9jq-gUGswt8dEYH5PiPJ7H8P8uelGnDcBig" + "?api_key=" + api_key
    # req2 = requests.get(url2)
    # print(req2.text)

