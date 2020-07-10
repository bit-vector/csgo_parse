#!/usr/bin/python3 -i

from demoparser.demofile import DemoFile
from demoparser.entities import Team

event = input('Enter event: ')
filename = 'match_old.dem'
players = []

def print_event(event, msg):
	print(msg.keys)
	for idx, key in enumerate(event['event'].keys):
		if key.name == 'userid':
			userid = msg.keys[idx].val_short
			user = df.entities.get_by_user_id(userid)
			if user.name not in players:
				players.append(user.name)

print(f'Opening \'{filename}\' as DemoFile \'df\'')
data = open(filename, 'rb').read()
df = DemoFile(data)
print('done reading')
print(f'adding callback \'{event}\'')
df.add_callback(event, print_event)
print('    HEADER    \n--------------')
print(df.header)
print('starting \'df.parse()\'')
df.parse()
print('finished')
print(f'Players: {players}')
team_ct = Team(df)
