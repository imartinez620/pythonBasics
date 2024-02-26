players = ['Altuve', 'Bregman', 'Correa', 'Gattis']

for player in players:
	print(player)

players = {
	'2b' : 'Altuve',
	'3b' : 'Bregman',
	'ss' : 'Corea',
	'dh' : 'Gattis'
}
print('##########')

for player in players:
	print(players[player])

print('##########')

for position,player in players.items():
	print('Position', position)
	print('Player', player)