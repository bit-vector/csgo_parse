#!/usr/bin/python3 -i

from demoparser.demofile import DemoFile

#File for writing
out_file = 'stats.txt'

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
print('finished\n--------\n')

#Stat calculations
players = dict()
scores = dict()
match_winner = ''
for team in df.entities.teams[2:]:
	scores[team.clan] = team.score
	if team.score == 16:
		match_winner = team.clan

	print(team.clan)
	userids = team.get_prop('DT_Team', '\"player_array\"')
	for userid in userids:
		print('\t', df.entities.get_by_user_id(userid).name)

print(f'players: {players}')
print(f'scores: {scores}')

for team in scores:
		print(f'{team}: {scores[team]}')
print(f'Winner: {match_winner}')

fp = open(out_file, 'w')
fp.close()
