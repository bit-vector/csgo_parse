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

players = dict()
for player in df.entities.players:
	teamname = df.entities.teams[player.team_num].clan
	if teamname == '':
		continue
	if teamname not in players:
		players[teamname] = [player]
	else:
		players[teamname].append(player)

#Stat calculations
print(f"Map name: {df.header.map_name.decode('utf-8')}")
seperate()
match_winner = ''
for team in df.entities.teams[2:]:
	print(f'{team.clan}: {team.score}')
	for player in players[team.clan]:
		print(f'\t{player.name}')
	if team.score == 16:
		match_winner = team.clan
seperate()

print(f'Winner: {match_winner}')
