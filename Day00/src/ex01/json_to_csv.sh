#!/bin/sh

if [ -z $1 ]; then
echo "Please enter path to json file"
exit 1
fi

filter_file="filter.jq"
path_to_json=$1
csv_file="hh.csv"

echo "\"id\",\"created_at\",\"name\",\"has_test\",\"alternate_url\"" > $csv_file
jq -r -f $filter_file $path_to_json >> $csv_file