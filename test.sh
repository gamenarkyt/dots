#! /bin/bash
search=$(cat /etc/pacman.conf | grep -e "^\[chaotic-aur\]")

if [ -v $search ]; then
    echo "yes"
else 
    echo "no"
fi