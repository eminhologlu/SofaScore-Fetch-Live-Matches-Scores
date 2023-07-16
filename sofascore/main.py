import time
import requests
import json

urlBasketball = "https://api.sofascore.com/api/v1/sport/basketball/events/live"
urlFootball = "https://api.sofascore.com/api/v1/sport/football/events/live"
urlTennis = "https://api.sofascore.com/api/v1/sport/tennis/events/live"
urlVolleyball = "https://api.sofascore.com/api/v1/sport/volleyball/events/live"
urlHandball = "https://api.sofascore.com/api/v1/sport/handball/events/live"
payload = ""
headers = {
    "authority": "api.sofascore.com",
    "accept": "*/*",
    "accept-language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "max-age=0",
    "if-none-match": "W/^\^542990ed1e^^",
    "origin": "https://www.sofascore.com",
    "referer": "https://www.sofascore.com/",
    "sec-ch-ua": "^\^Not.A/Brand^^;v=^\^8^^, ^\^Chromium^^;v=^\^114^^, ^\^Google",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "^\^Windows^^",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

#ayarlar
#True / False
futbol = True
basketbol = False
voleybol = False
tenis = False
hentbol = False

while True:

    responseBasketball = requests.request("GET", urlBasketball, data=payload, headers=headers)
    responseFootball = requests.request("GET", urlFootball, data=payload, headers=headers)
    responseTennis = requests.request("GET", urlTennis, data=payload, headers=headers)
    responseVolleyball = requests.request("GET", urlVolleyball, data=payload, headers=headers)
    responseHandball = requests.request("GET", urlHandball, data=payload, headers=headers)
    jsondataBasketball = json.loads(responseBasketball.text)
    jsondataFootball = json.loads(responseFootball.text)
    jsondataTennis = json.loads(responseTennis.text)
    jsondataVolleyball = json.loads(responseVolleyball.text)
    jsondataHandball = json.loads(responseHandball.text)

    if(basketbol):
        for game in jsondataBasketball["events"]:
            league = game["tournament"]["name"]
            hometeam = game["homeTeam"]["name"]
            awayteam = game["awayTeam"]["name"]
            homescore = game["homeScore"]["current"]
            awayscore = game["awayScore"]["current"]
            text = "{0} | {1} {2}  -  {3} {4}"
            print(text.format(league,hometeam,homescore,awayscore,awayteam))
    time.sleep(10)
    if(futbol):
        for game in jsondataFootball["events"]:
            league = game["tournament"]["name"]
            hometeam = game["homeTeam"]["name"]
            awayteam = game["awayTeam"]["name"]
            homescore = game["homeScore"]["current"]
            awayscore = game["awayScore"]["current"]
            text = "{0} | {1} {2}  -  {3} {4}"
            print(text.format(league,hometeam,homescore,awayscore,awayteam))
    time.sleep(10)
    if(tenis):
        for game in jsondataTennis["events"]:
            league = game["tournament"]["name"]
            hometeam = game["homeTeam"]["name"]
            awayteam = game["awayTeam"]["name"]
            homescore = game["homeScore"]["current"]
            awayscore = game["awayScore"]["current"]
            text = "{0} | {1} {2}  -  {3} {4}"
            print(text.format(league,hometeam,homescore,awayscore,awayteam))
    time.sleep(10)
    if(voleybol):
        for game in jsondataVolleyball["events"]:
            league = game["tournament"]["name"]
            hometeam = game["homeTeam"]["name"]
            awayteam = game["awayTeam"]["name"]
            homescore = game["homeScore"]["current"]
            awayscore = game["awayScore"]["current"]
            text = "{0} | {1} {2}  -  {3} {4}"
            print(text.format(league,hometeam,homescore,awayscore,awayteam))
    time.sleep(10)
    if(hentbol):
        for game in jsondataHandball["events"]:
            league = game["tournament"]["name"]
            hometeam = game["homeTeam"]["name"]
            awayteam = game["awayTeam"]["name"]
            homescore = game["homeScore"]["current"]
            awayscore = game["awayScore"]["current"]
            text = "{0} | {1} {2}  -  {3} {4}"
            print(text.format(league,hometeam,homescore,awayscore,awayteam))
    time.sleep(10)
