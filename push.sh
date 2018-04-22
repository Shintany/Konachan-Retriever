#!/bin/sh

# THE GOAL OF THIS SCRIPT IS TO PUSH A COMMIT INTO A REPOSITORY

read -p "Do you wanna commit? (Y/n)" -n 1 -r
if [[ $REPLY =~ ^[Yy]$ ]]
then
    username='Shintany'
    repository=$1
    comment=$2
    echo 'This script will push in the following repository :' $repository 

    git add *.py *.txt

    echo 'Added succesfully!'

    git commit -m "$1"

    echo 'Committed succesfully!'

    # If repository doesn't exist
    # git remote add origin https://github.com/Shintany/$1

    git push

    echo 'Pushed succesfully!'
else
    echo 
    echo 'Be sure next time!'
fi

