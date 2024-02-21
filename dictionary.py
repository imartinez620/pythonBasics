players = {
	"ss": "Correa",
	"2b": "Altuve",
	"3b": "Bregman",
	"DH": "Gattis",
	"OF": "Springer"
}

second_base = players['2b']
designated_hitter = players['DH']

print(players)
print(second_base)
print(designated_hitter)

teams = {
	"astros": ["Altuve","Correa","Bregman"],
	"angels": ["Trout","Pujols"],
	"yankees": ["Judge","Stanton"]
}

print(teams["astros"][:2]) #astros[:2]

astros = teams["astros"]
print(astros) 
print(teams["angels"]) 
print(teams["yankees"]) 

#add new pair key:valors
teams['red sox'] = ['Price','Betts']

print(teams)

#queries
#featured_team = teams.get('mets', 'No featured team')
featured_team = teams.get('yankees', 'No featured team')
print(featured_team)