#!/bin/bash

query=$1
token=$2

curl -s -H "Authorization: token $token" GET https://api.github.com/search/repositories?q=org:DSACMS+$query >> apiJson.json
total_count=$(jq '.total_count' apiJson.json)
echo $total_count
if [ -z "$total_count" ]; then
    cat apiJson.json
    echo "error: Error fetching from github api" >&2; exit 1
fi
if [ "$total_count" -eq "0" ]; then
    cat apiJson.json
    echo "error: no repos found for topic" >&2; exit 1
fi

repoStr=$(jq '.items' apiJson.json | jq '.[0].full_name')
repoStr="$repoStr"
output=["$repoStr"]
for (( i=1; i<=$total_count-1; i++)); do
    repo=$(jq '.items' apiJson.json | jq '.['$i'].full_name')
    output=$(echo $output | jq --argjson r $repo '. + [$r]')
done

echo $output