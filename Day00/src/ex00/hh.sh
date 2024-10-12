#!/bin/sh

if [ -z $1 ]; then
echo "Please enter name of the vacancy"
exit 1
fi

vacancy_name=$(echo $1 | sed 's/ /%20/g')
url="https://api.hh.ru/vacancies?text=$vacancy_name"
user_agent="default"
file="hh.json"
curl -X GET $url -H "User-Agent: $user_agent" | jq '.' > $file