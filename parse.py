#!/usr/bin/python3
#Reference: https://developer.valvesoftware.com/wiki/DEM_Format#:~:text=DEM%20(short%20for%20demo)%20is,play%20music%2C%20and%20other%20functions

from codecs import decode
from struct import unpack

def parseHeader(filename):
	fp = open(filename, 'rb')
	header = fp.readline()
	fp.close()

	out = []

	#File header, 8 char string
	filestamp = decode(header[:8])
	if filestamp != 'HL2DEMO\0':
		print('File not valid')
		return None
	out.append(filestamp)

	#Demo protocol, signed int
	protocol_dem = int.from_bytes(header[8:12], byteorder='little', signed=True)
	out.append(protocol_dem)

	#Network protocol, signed int
	protocol_net = int.from_bytes(header[12:16], byteorder='little', signed=True)
	out.append(protocol_net)

	#Server name, 260 char string
	svr_name = decode(header[16:276])
	out.append(svr_name)

	#Client name, 260 char string
	client = decode(header[276:536])
	out.append(client)

	#Map name, 260 char string
	mp = decode(header[536:796])
	out.append(mp)

	#Game directory, 260 char string
	gdir = decode(header[796:1056])
	out.append(gdir)

	#Playback time, float
	pbt = unpack('f', header[1056:1060])
	out.append(pbt[0])

	#Ticks, signed int
	ticks = int.from_bytes(header[1060:1064], byteorder='little', signed=True)
	out.append(ticks)

	#Frames, signed int
	frames = int.from_bytes(header[1064:1068], byteorder='little', signed=True)
	out.append(frames)

	#Sign-on length, signed int
	length = int.from_bytes(header[1068:1072], byteorder='little', signed=True)
	out.append(length)

	#print(header[1072:])

	return out

def printHeader(header_parsed):
	header_key = ['Filestamp', 'Demo Protocol', 'Network Protocol', 'Server Name', 'Client Name', 'Map Name', 'Game Directory', 'Playback Time', 'Ticks', 'Frames', 'Sign-on length']

	for i in range(len(header_parsed)):
		print(f'{header_key[i]}: {header_parsed[i]}')

	return None

def parseLine(line):
	return None
