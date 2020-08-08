#!/bin/bash

#pattern="122\\.160\\.153"

#for pattern in $(cat Airtel_Raj_for_VM)
#do

options=$(cat Airtel_Raj_for_VM | tr -s '\n' ' ')
for pattern in $options
do

echo -n "$pattern =  " #>> results.txt


for j in $(ls)
do
	if [ -d $j ]
	then
	cd $j

	out=0

	for i in $(ls)
	do

		if [ -f $i ]
		then

		result=$(grep "$pattern" "$i" | wc -l)
		out=$(($out + $result))
		fi

	done

	echo -n "$out " #>> results.txt

	cd ..
	
	fi
done

echo "" # >> results.txt

done



