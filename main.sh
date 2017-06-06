#!/bin/bash

#This file's permission has been changed to make it executable

function check_connection {
  echo -e "GET http://google.com HTTP/1.0\n\n" | nc google.com 80 > /dev/null 2>&1

  if [ $? -eq 0 ]
  then
      echo "0"  # Online
  else
      echo "1"  # Offline
  fi
  ################################################
  #    ALTERNATE METHOD IS MENTIONED BELOW
  #################################################
  # wget -q --spider http://google.com
  #
  # if [ $? -eq 0 ]; then
  #     echo "0" # Success meaning Internet access available
  # else
  #     echo "1" # failure meaning Internet access isnt available
  # fi
}

if [ -f logs.txt ]
then
  rm logs.txt
fi

if [ -f new_info.txt ]
then
  rm new_info.txt
fi

echo `date` >> logs.txt
echo "Checking internet connection!" >> logs.txt
# check_connection
internet_status=`check_connection` >> logs.txt

if [ $internet_status -eq 0 ]
then
  echo "Internet connection found!" >> logs.txt
  FILES=`ls spiders`
  cd spiders
  for spider_name in $FILES
  do
    echo "Executing $spider_name" >> ../logs.txt
    python $spider_name
  done
  cd ..



  echo "New information retrieved successfully!"

else
  echo "Internet connection not found!" >> logs.txt
fi
