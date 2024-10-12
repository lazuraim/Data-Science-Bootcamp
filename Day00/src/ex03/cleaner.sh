#!/bin/sh

if [ -z $1 ]; then
echo "Please enter path to json file"
exit 1
fi

output_file="hh_positions.csv"

find_match () {
    position="$1"
    if [[ $position =~ [Jj]unior ]]; then
        echo "\"Junior\""
    elif [[ $position =~ [Mm]iddle ]]; then
        echo "\"Middle\""
    elif [[ $position =~ [Ss]enior ]]; then
        echo "\"Senior\""
    else 
        echo "\"-\""
    fi
}

head -n 1 $1 > $output_file

tail -n 20 "$1" | while IFS=',' read -r id created_at name has_test alternate_url; 
do 
  new_position=$(find_match "$name")
  echo "$id,$created_at,$new_position,$has_test,$alternate_url" >> $output_file
done 
