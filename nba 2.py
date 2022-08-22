lis=[]
intocsv=[]
abc="{} score= {},blocks= {},steals= {},defend rebound= {} \n"
import requests
import json

def getData(game_id):
    link='https://tw.global.nba.com/stats2/game/snapshot.json?countryCode=TW&gameId='+game_id+'&locale=zh_TW&tz=%2B8'
    r = requests.get(link)
    data={}
    if r.status_code == requests.codes.ok:
        print("OK")
        data = json.loads(r.text)
    else:
        file = open ('NBAGAME .json', "r" ,encoding="utf-8")
        data = json.loads(file.read())
        file.close()
    return data  

def parseData(input_data):
    data=input_data
    awayteam={
        "name":data["payload"]["awayTeam"]["profile"]["name"],
        "score":data["payload"]["boxscore"]["awayScore"],
        "steals":data["payload"]["awayTeam"]["score"]["steals"],
        "blocks":data["payload"]["awayTeam"]["score"]["blocks"],
        "defRebs":data["payload"]["awayTeam"]["score"]["defRebs"]
        }
    hometeam={
        "name":data["payload"]["homeTeam"]["profile"]["name"],
        "score":data["payload"]["boxscore"]["homeScore"],
        "steals":data["payload"]["homeTeam"]["score"]["steals"],
        "blocks":data["payload"]["homeTeam"]["score"]["blocks"],
        "defRebs":data["payload"]["homeTeam"]["score"]["defRebs"],
        }
    lead_changes = data["payload"]["boxscore"]["leadChanges"]

    lis.append(awayteam['name'])
    lis.append(hometeam['name'])
    lis.append('領先替換次數為'+str(lead_changes)+'\n')
    home_players = data["payload"]["homeTeam"]["gamePlayers"]
    away_players = data["payload"]["awayTeam"]["gamePlayers"]


    print('球員                                        ','score   '  ,'blocks   '  ,'steals   '   ,'defRebs   ')
    tmp=['球員','score'  ,'blocks '  ,'steals '   ,'defRebs']
    intocsv.append(tmp)
    for player in home_players:
        player_data = {
                "name":player["profile"]["displayNameEn"],
                "score":player["statTotal"]["points"],
                "steals":player["statTotal"]["steals"],
                "blocks":player["statTotal"]["blocks"],
                "defRebs":player["statTotal"]["defRebs"],
            }
        lis.append(abc.format(player_data["name"] ,player_data["score"] ,player_data["blocks"] ,player_data["steals"] ,player_data["defRebs"]))
        print(player_data["name"] ,player_data["score"] ,player_data["blocks"] ,player_data["steals"],player_data["defRebs"])
        intocsv.append([player_data["name"] ,player_data["score"] ,player_data["blocks"] ,player_data["steals"] ,player_data["defRebs"]])

    for player in away_players:
        player_data = {
                "name":player["profile"]["displayNameEn"],
                "score":player["statTotal"]["points"],
                "steals":player["statTotal"]["steals"],
                "blocks":player["statTotal"]["blocks"],
                "defRebs":player["statTotal"]["defRebs"],
            }
     #   tmp=[]
        lis.append(abc.format(player_data["name"],player_data["score"] ,player_data["blocks"] ,player_data["steals"] ,player_data["defRebs"]))
        print(player_data["name"] ,player_data["score"] ,player_data["blocks"] ,player_data["steals"],player_data["defRebs"])
        intocsv.append([player_data["name"] ,player_data["score"] ,player_data["blocks"] ,player_data["steals"] ,player_data["defRebs"]])
def writeFile():
    f = open("demo.txt", "wt")
    f.writelines(lis)

    f.close()
def writeCvs(name):
     
    import csv
    with open(name+'.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        for row in intocsv:
            
            writer.writerow(row)
    

gameid='0022100908'
nba_data=getData(gameid)

parseData(nba_data)
writeFile()
writeCvs(gameid)
