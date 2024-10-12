#!/bin/sh

if [ -z $1 ]; then
echo "Please enter path to csv file"
exit 1
fi

output_file='hh_uniq_positions.csv'
input_file="$1"

tail -n 20 $input_file | cut -d ',' -f3 | sort | uniq -c > $output_file
output=$(awk '/Junior|Middle|Senior/{print $2 "," $1}' $output_file)
echo "\"name\",\"count\"" > $output_file
echo $output >> $output_file
