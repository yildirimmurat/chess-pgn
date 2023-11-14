#!/usr/bin/python3
import sys
import re

# Reads the first argument if it exists 
if (sys.argv.__len__()>1):
	file = sys.argv[1]

players = []

# Reads a file and prints all the lines 
with open(file,"r") as dataFile:
    for line in dataFile:
        player = re.search('<a href=\"players/(.*)\.zip\">', line)
        if(player):
            players.append(player.group(1))

for player in players:
    print(player)        
