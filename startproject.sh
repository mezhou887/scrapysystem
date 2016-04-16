#!/bin/bash
set -e

usage() {
    echo "usage:     ./startproject.sh <project name> <sprider name >"
}

if [ -z "$2" ]; then
    usage
    exit
fi



echo "Starting project $1."
echo "Starting spider $2."
cp -r template $1
if [ "$(uname)" == "Darwin" ]; then
    #alias sed='sed -i'
    find $1 -type f | xargs sed -i '' "s/template/$1/g"
    find $1 -type f | grep spiders | xargs sed -i '' "s/class $1/class $2/g"
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    find $1 -type f | xargs sed -i "s/template/$1/g"
    find $1 -type f | grep spiders | xargs sed -i "s/class $1/class $2/g"
elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW32_NT" ]; then
    find $1 -type f | xargs sed -i "s/template/$1/g"
fi
mv $1/template $1/$1

echo "Create $1 succeed!"
