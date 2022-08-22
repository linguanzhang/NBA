lis=[]
abc="{}score={},blocks={},steals={},defend rebound={}\n"
import json
file = open ('NBAGAME .json', "r" ,encoding="utf-8")
data = json.loads(file.read())
file.close()

awayteam_name = data["payload"]["awayTeam"]["profile"]["name"]
awayteam_score = data["payload"]["boxscore"]["awayScore"]
hometeam_name = data["payload"]["homeTeam"]["profile"]["name"]
hometeam_score = data["payload"]["boxscore"]["homeScore"]


lead_changes = data["payload"]["boxscore"]["leadChanges"]

#print (awayteam_name,"得分為",awayteam_score)
lis.append(awayteam_name+"得分為"+str(awayteam_score)+'\n')
lis.append(hometeam_name+"得分為"+str(hometeam_score)+'\n')
lis.append('領先替換次數為'+str(lead_changes)+'\n')
home_players = data["payload"]["homeTeam"]["gamePlayers"]
away_players = data["payload"]["awayTeam"]["gamePlayers"]
hometeam_defRebs = data["payload"]["homeTeam"]["score"]["defRebs"]
awayteam_defRebs = data["payload"]["awayTeam"]["score"]["defRebs"]
hometeam_blocks = data["payload"]["homeTeam"]["score"]["blocks"]
awayteam_blocks = data["payload"]["homeTeam"]["score"]["blocks"]
hometeam_steals = data["payload"]["homeTeam"]["score"]["steals"]
awayteam_steals = data["payload"]["awayTeam"]["score"]["steals"]
lis.append('溜馬球員得分:'+'\n')
for player in home_players:
    player_name=player["profile"]["displayNameEn"]
    player_points=player["statTotal"]["points"]
    player_defRebs=player["statTotal"]["defRebs"]
    player_blocks=player["statTotal"]["blocks"]
    player_steals=player["statTotal"]["steals"]
 #lis.append(player_name+"score"+str(player_points)+'\n')
   # lis.append(str(player_defRebs)+"defRebs"+'\n')
  #  lis.append(str(player_blocks)+"blocks"+'\n')
  #  lis.append(str(player_steals)+"steals"+'\n')
    lis.append(abc.format(player_name,player_points,player_blocks,player_steals,player_defRebs,))

lis.append('魔術球員得分:')
for player in away_players:
    player_name=player["profile"]["displayNameEn"]
    player_points=player["statTotal"]["points"]
    player_defRebs=player["statTotal"]["defRebs"]
    player_blocks=player["statTotal"]["blocks"]
    player_steals=player["statTotal"]["steals"]
   # lis.append(player_name+"score"+str(player_points)+'\n')
   # lis.append(str(player_defRebs)+"defRebs"+'\n')
    #lis.append(str(player_blocks)+"blocks"+'\n')
    #lis.append(str(player_steals)+"steals"+'\n')
    lis.append(abc.format(player_name,player_points,player_blocks,player_steals,player_defRebs,))
print(lis)
f = open("dem.txt", "wt")
f.writelines(lis)
f.close()
