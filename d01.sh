#!/bin/bash
# data file
INPUT=$1
TARGET=$2
 
floor=0
count=0

# while loop
while IFS= read -r -n1 char
do
  if [[ "$char" == "(" ]]; then
    ((floor++))
  elif [[ "$char" == ")" ]]; then
    ((floor--))
  fi

  ((count++))

  if [[ $floor == $TARGET ]]; then
    echo "(part2) Entered $TARGET at position $count"
  fi
  #echo  "$char $floor"
done < "$INPUT"

echo "Final floor (part1) $floor"

