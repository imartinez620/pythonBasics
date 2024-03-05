import fnmatch
from fnmatch import fnmatchcase
import os

def list_files():
	for file in os.listdir('.'):
		if fnmatch.fnmatch(file, '*.txt'):
			print("Text files: ", file)

		if fnmatch.fnmatch(file, '*.py'):
			print("Python files: ", file)

#list_files()

players = [
		"Jugador Uno J1",
		"Jugador Dos J2",
		"Jugador Tres J3",
		"Jugador Cuatro J1"
]


second_base_players = [player for player in players if fnmatchcase(player, '* J1')]

print(second_base_players)