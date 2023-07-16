import time
import requests
import json

tarih = "2023-07-16"
urlFootball = f"https://api.sofascore.com/api/v1/sport/football/scheduled-events/{tarih}"
urlBasketball = f"https://api.sofascore.com/api/v1/sport/basketball/scheduled-events/{tarih}"
urlVolleyball = f"https://api.sofascore.com/api/v1/sport/volleyball/scheduled-events/{tarih}"
urlHandball = f"https://api.sofascore.com/api/v1/sport/handball/scheduled-events/{tarih}"
urlTennis = f"https://api.sofascore.com/api/v1/sport/tennis/scheduled-events/{tarih}"

payload = ""
headers = {
    "authority": "api.sofascore.com",
    "accept": "*/*",
    "accept-language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "max-age=0",
    "if-none-match": "W/^\^11acc671d1^^",
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

    responseFootball = requests.request("GET", urlFootball, data=payload, headers=headers)
    responseBasketball = requests.request("GET", urlBasketball, data=payload, headers=headers)
    responseVolleyball = requests.request("GET", urlVolleyball, data=payload, headers=headers)
    responseHandball = requests.request("GET", urlHandball, data=payload, headers=headers)
    responseTennis = requests.request("GET", urlTennis, data=payload, headers=headers)
    jsondataFootball = json.loads(responseFootball.text)
    jsondataBasketball = json.loads(responseBasketball.text)
    jsondataVolleyball = json.loads(responseVolleyball.text)
    jsondataHandball = json.loads(responseHandball.text)
    jsondataTennis = json.loads(responseTennis.text)

    if(futbol):
        for game in jsondataFootball["events"]:
            if (game["status"]["type"] == "finished"):
                league = game["tournament"]["name"]
                hometeam = game["homeTeam"]["name"]
                awayteam = game["awayTeam"]["name"]
                homescore = game["homeScore"]["display"]
                awayscore = game["awayScore"]["display"]
                status = game["status"]["description"]
                print(league," | ",hometeam, homescore, " - ", awayscore, awayteam, " - ",status)
            elif (game["status"]["type"] == "inprogress"):
                league = game["tournament"]["name"]
                hometeam = game["homeTeam"]["name"]
                awayteam = game["awayTeam"]["name"]
                homescore = game["homeScore"]["current"]
                awayscore = game["awayScore"]["current"]
                status = game["status"]["description"]
                print(league, " | ", hometeam, homescore, " - ", awayscore, awayteam, " - ", status)

    if(basketbol):
        for game in jsondataBasketball["events"]:
            if (game["status"]["type"] == "finished"):
                league = game["tournament"]["name"]
                hometeam = game["homeTeam"]["name"]
                awayteam = game["awayTeam"]["name"]
                homescore = game["homeScore"]["display"]
                awayscore = game["awayScore"]["display"]
                status = game["status"]["description"]
                print(league," | ",hometeam, homescore, " - ", awayscore, awayteam, " - ",status)
            elif (game["status"]["type"] == "inprogress"):
                league = game["tournament"]["name"]
                hometeam = game["homeTeam"]["name"]
                awayteam = game["awayTeam"]["name"]
                homescore = game["homeScore"]["current"]
                awayscore = game["awayScore"]["current"]
                status = game["status"]["description"]
                print(league, " | ", hometeam, homescore, " - ", awayscore, awayteam, " - ", status)

    if(voleybol):
        for game in jsondataVolleyball["events"]:
            if (game["status"]["type"] == "finished"):
                league = game["tournament"]["name"]
                hometeam = game["homeTeam"]["name"]
                awayteam = game["awayTeam"]["name"]
                homescore = game["homeScore"]["display"]
                awayscore = game["awayScore"]["display"]
                status = game["status"]["description"]
                print(league," | ",hometeam, homescore, " - ", awayscore, awayteam, " - ",status)
            elif (game["status"]["type"] == "inprogress"):
                league = game["tournament"]["name"]
                hometeam = game["homeTeam"]["name"]
                awayteam = game["awayTeam"]["name"]
                homescore = game["homeScore"]["current"]
                awayscore = game["awayScore"]["current"]
                status = game["status"]["description"]
                print(league, " | ", hometeam, homescore, " - ", awayscore, awayteam, " - ", status)

    if(hentbol):
        for game in jsondataHandball["events"]:
            if (game["status"]["type"] == "finished"):
                league = game["tournament"]["name"]
                hometeam = game["homeTeam"]["name"]
                awayteam = game["awayTeam"]["name"]
                homescore = game["homeScore"]["display"]
                awayscore = game["awayScore"]["display"]
                status = game["status"]["description"]
                print(league," | ",hometeam, homescore, " - ", awayscore, awayteam, " - ",status)
            elif (game["status"]["type"] == "inprogress"):
                league = game["tournament"]["name"]
                hometeam = game["homeTeam"]["name"]
                awayteam = game["awayTeam"]["name"]
                homescore = game["homeScore"]["current"]
                awayscore = game["awayScore"]["current"]
                status = game["status"]["description"]
                print(league, " | ", hometeam, homescore, " - ", awayscore, awayteam, " - ", status)

    if(tenis):
        for game in jsondataTennis["events"]:
            if (game["status"]["type"] == "finished"):
                league = game["tournament"]["name"]
                hometeam = game["homeTeam"]["name"]
                awayteam = game["awayTeam"]["name"]
                homescore = game["homeScore"]["display"]
                awayscore = game["awayScore"]["display"]
                status = game["status"]["description"]
                print(league," | ",hometeam, homescore, " - ", awayscore, awayteam, " - ",status)
            elif (game["status"]["type"] == "inprogress"):
                league = game["tournament"]["name"]
                hometeam = game["homeTeam"]["name"]
                awayteam = game["awayTeam"]["name"]
                homescore = game["homeScore"]["current"]
                awayscore = game["awayScore"]["current"]
                status = game["status"]["description"]
                print(league, " | ", hometeam, homescore, " - ", awayscore, awayteam, " - ", status)
    time.sleep(60)