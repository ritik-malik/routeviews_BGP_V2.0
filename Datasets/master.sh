#!/bin/bash

DATE=1

for i in {1..30}
do

if [ $i -gt 16 ]
then



    if [ $((${DATE} % 2)) -eq 1 ]
    then

        if [ ${DATE} -lt 10 ]
        then
            mkdir 2019120${DATE}
            cp maalik_routeviews.py 2019120${DATE}
            cp -r zebra-dump-parser 2019120${DATE}
            cd 2019120${DATE}

            nohup python3 maalik_routeviews.py 2019120${DATE}.1000 &
            id_1=$!
            nohup python3 maalik_routeviews.py 2019120${DATE}.1200 &
            id_2=$!
            nohup python3 maalik_routeviews.py 2019120${DATE}.1400 &
            id_3=$!
            nohup python3 maalik_routeviews.py 2019120${DATE}.1600 &
            id_4=$!
            nohup python3 maalik_routeviews.py 2019120${DATE}.1800 &
            id_5=$!

        else
            mkdir 201912${DATE}
            cp maalik_routeviews.py 201912${DATE}
            cp -r zebra-dump-parser 201912${DATE}
            cd 201912${DATE}
            
            nohup python3 maalik_routeviews.py 201912${DATE}.1000 &
            id_1=$!
            nohup python3 maalik_routeviews.py 201912${DATE}.1200 &
            id_2=$!
            nohup python3 maalik_routeviews.py 201912${DATE}.1400 &
            id_3=$!
            nohup python3 maalik_routeviews.py 201912${DATE}.1600 &
            id_4=$!
            nohup python3 maalik_routeviews.py 201912${DATE}.1800 &
            id_5=$!

        fi
    
        cd ..
        ((DATE++))

        ##################################### 2nd time

        if [ ${DATE} -lt 10 ]
        then
            mkdir 2019120${DATE}
            cp maalik_routeviews.py 2019120${DATE}
            cp -r zebra-dump-parser 2019120${DATE}
            cd 2019120${DATE}

            nohup python3 maalik_routeviews.py 2019120${DATE}.1000 &
            id_6=$!
            nohup python3 maalik_routeviews.py 2019120${DATE}.1200 &
            id_7=$!
            nohup python3 maalik_routeviews.py 2019120${DATE}.1400 &
            id_8=$!
            nohup python3 maalik_routeviews.py 2019120${DATE}.1600 &
            id_9=$!
            nohup python3 maalik_routeviews.py 2019120${DATE}.1800 &
            id_10=$!

        else
            mkdir 201912${DATE}
            cp maalik_routeviews.py 201912${DATE}
            cp -r zebra-dump-parser 201912${DATE}
            cd 201912${DATE}
            
            nohup python3 maalik_routeviews.py 201912${DATE}.1000 &
            id_6=$!
            nohup python3 maalik_routeviews.py 201912${DATE}.1200 &
            id_7=$!
            nohup python3 maalik_routeviews.py 201912${DATE}.1400 &
            id_8=$!
            nohup python3 maalik_routeviews.py 201912${DATE}.1600 &
            id_9=$!
            nohup python3 maalik_routeviews.py 201912${DATE}.1800 &
            id_10=$!
    
        fi
        cd ..

    else
        wait ${id_1}; wait ${id_2}; wait ${id_3}; wait ${id_4}; wait ${id_5};
        wait ${id_6}; wait ${id_7}; wait ${id_8}; wait ${id_9}; wait ${id_10};
        ((DATE++))
    fi

fi
done

################################### now cleanup

rm nohup.out
rm -rf zebra-dump-parser

for i in $(ls)
do

    if [ -d $i ]
    then
        cd $i
        rm dump_errors
        rm maalik_routeviews.py
        rm -rf zebra-dump-parser
        cd ..
    fi
done
