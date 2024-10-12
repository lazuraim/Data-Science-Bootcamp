#!/bin/sh

if [ -z $1 ]; then
echo "Please enter path to json file"
exit 1
fi

file_to_sort="$1"
headers=$(head -n 1 $file_to_sort)
sorted_file="hh_sorted.csv"

echo $headers > "$sorted_file"
tail -n 20 $file_to_sort | sort -t "," -k2 -k1n  >> "$sorted_file"
