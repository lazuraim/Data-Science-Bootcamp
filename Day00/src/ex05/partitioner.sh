#!/bin/sh

if [ -z $1 ]; then
echo "Please enter path to csv file"
exit 1
fi

input_file="$1"

tail -n 20 "$1" | while IFS=',' read -r id created_at name has_test alternate_url; 
do
  date=$(echo ${created_at:1} | cut -d 'T' -f 1)
  if [[ ! -f "$date.csv" ]]; then
    echo "\"id\",\"created_at\",\"name\",\"has_test\",\"alternate_url\"" > $date.csv
  fi
  echo "$id,$created_at,$name,$has_test,$alternate_url" >> $date.csv
done 
