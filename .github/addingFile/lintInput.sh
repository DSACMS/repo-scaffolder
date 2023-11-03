#!/bin/sh

location=$1

if test -f $location; then
  echo "File exists."
elif test -d $location; then
  echo "Directory exists."
else
    echo "error: file or direcoty not found: " $1 >&2; exit 1
fi
