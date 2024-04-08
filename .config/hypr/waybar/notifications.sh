#! /bin/bash

# noti=$( cat waybar/noti.jsonc | jq ".data[]" )
noti=$( dunstctl history | jq ".data[] | reverse" )
# echo $noti

count=$(echo $noti | jq  ". | length" )
# echo $count
for ((var = 0; var < $count; var++)); do
    header=$(echo $noti | jq ". [$var] .summary.data" | tr -d '"')
    content=$(echo $noti | jq ". [$var] .body.data" | tr -d '"')
    timeout=$(echo $noti | jq ". [$var] .timeout.data" | tr -d '"')
    if [[ $timeout == 8000000 ]]; then
        echo -e "\e[91m$header\e[39m"
    fi
    if [[ $timeout == 6000000 ]]; then
        echo -e "\e[35m$header\e[39m"
    fi
    if [[ $timeout == 4000000 ]]; then
        echo -e "\e[96m$header\e[39m"
    fi
    echo -e "$content\n"
done

