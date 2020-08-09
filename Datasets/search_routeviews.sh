#!/bin/bash

#pattern="122\.160\.153\."

list=$(cat verified_IP_UP | tr -s '\n' ' ')
for pattern in ${list}
do

echo -n "$pattern =  "

for DATES in $(ls)
do
	if [ -d ${DATES} ]
	then
	cd ${DATES}

	total=0

	for DUMPS in $(ls)
	do

		if [ -f ${DUMPS} ]
		then

		result=$(grep "${pattern}" "${DUMPS}" | wc -l)
		total=$((${total} + ${result}))
		fi

	done

	echo -n "${total} "

	cd ..
	
	fi
done

echo ""

done

