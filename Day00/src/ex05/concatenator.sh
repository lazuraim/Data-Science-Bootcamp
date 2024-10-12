#!/bin/sh

if [ -z $1 ]; then
echo "Please enter path to csv file"
exit 1
fi

output_file="all.csv"
echo "\"id\",\"created_at\",\"name\",\"has_test\",\"alternate_url\"" > $output_file

for val in $*; do
    tail -n +2 $val | cat  >> $output_file
done