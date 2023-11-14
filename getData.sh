# get all player information from a remote site


# source information
#source="https://www.pgnmentor.com/"
#extension="files.html"


source=$1
extension=$2

echo $source
echo $extension


# save the data to src/ directory
mkdir src/
cd src
wget $source$extension
mv $extension data.html
cd ..


# echo the data to console
# datas=$(cat $extension)
# echo "${datas}"