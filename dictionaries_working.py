players = {
	"ss": "Correa",
	"2b": "Altuve",
	"3b": "Bregman",
	"DH": "Gattis",
	"OF": "Springer"
}

#print(players.keys())
#print(players.values())
#print(players.items())

player_names = list(players.copy().values())
print(player_names)

teams = {
	"astros": ["Altuve","Correa","Bregman"],
	"angels": ["Trout","Pujols"],
	"yankees": ["Judge","Stanton"],
	"red sox": ["Price", "Betts"]
}

team_groupings = teams.items()
print(list(team_groupings)[0][1][0])

#delete items
#del teams['astros']
removed_team = teams.pop('astros', 'No team found by that name')


print(removed_team)

