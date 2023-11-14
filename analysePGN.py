#!/usr/bin/python3
import sys
import re

# Reads the first argument if it exists 
if (sys.argv.__len__()>1):
	file = sys.argv[1]

countGames = 0
games = []
game = []

countLineInGame = 0
event = []

# Reads a file and prints all the lines 
with open(file,"r") as dataFile:
    for line in dataFile:
        lineToBeRead = line
        print("lineToBeRead: ", lineToBeRead, end='')
        if(lineToBeRead == ''):
            print("all empty line go continue")
            continue
        print("countInGame+"+  str(countLineInGame))
        if (countLineInGame == 1):
            eventToBeAppended = re.search('Event \"(.*)\"', lineToBeRead)
            if(eventToBeAppended):
                game.append(eventToBeAppended.group(1))
            else:
                print("Event name cant be read in game")
        game.append(line.strip())
        endOfGame = re.search('(1-0|1/2-1/2|0-1)$', line)
        countLineInGame += 1
        if(endOfGame):
            print("end of game")
            print()
            countGames+=1
            games.append(game)
            game = []
            countLineInGame = 0
            continue

print(games[1][1])
