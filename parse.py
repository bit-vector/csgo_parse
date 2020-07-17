#!/usr/bin/env python3

from demoparser.demofile import DemoFile

num_dashes = 20
def seperate(n=num_dashes):
	for count in range(n):
		print('-', end='')
	print()

#Open and parse .dem file
filename = input('Filename(default=\'match.dem\'): ')
if filename == '':
	filename = 'match.dem'
print(f'opening \'{filename}\' as DemoFile \'df\'')
data = open(filename, 'rb').read()
df = DemoFile(data)
print('done reading')
print('parsing \'df\'...')
df.parse()
print('finished')
seperate()
print()

#Stat calculations
print(f"Map name: {df.header.map_name.decode('utf-8')}")
seperate();
match_winner = ''
for team in df.entities.teams[2:]:
	print(f'{team.clan}: {team.score}')
	if team.score == 16:
		match_winner = team.clan
seperate()

print('Players')
seperate(7)
players = df.entities.players[2:12]
for i in range(len(players)):
	players[i] = players[i].name
for player in players:
	print(player)
seperate()
print(f'Winner: {match_winner}')
