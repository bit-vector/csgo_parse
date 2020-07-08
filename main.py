#!/usr/bin/python3

from parse import parseHeader, printHeader

filename = 'match.dem'
parsed_header = parseHeader(filename)
printHeader(parsed_header)
