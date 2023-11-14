#!/bin/bash          
source="https://www.pgnmentor.com/"
format=".zip"
extension="files.html"

# all players of whom plays will be downloaded
declare -a allPlayers

# read players.txt file to get all player info
filename='players.txt'
n=1
while read line; do
    # reading each line
    #echo "Line No. $n : $line"
    allPlayers+=($line)
    n=$((n+1))
done < $filename


# create players directory
mkdir players/
cd players/

# download files
for i in "${allPlayers[@]}"; do
    tmp=$source
    fileToBeDownloaded=$i$format
    tmp+="players/"
    tmp+=$fileToBeDownloaded
    wget $tmp
    unzip $fileToBeDownloaded
    rm $fileToBeDownloaded
done

# Return to main directory
cd ..
