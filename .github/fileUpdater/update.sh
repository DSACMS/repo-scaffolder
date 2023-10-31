#!/bin/sh

filename=$3
search=$1
replace=$2

sed -i -e "s/$search/$replace/g" $filename