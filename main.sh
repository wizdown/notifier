#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:home/abhishek/android-studio/bin:/snap/bin:/home/abhishek/android-studio/bin:/opt/idea-IC-163.12024.16/bin::/home/abhishek/android-studio/bin:/opt/idea-IC-163.12024.16/bin:/home/abhishek/Desktop/noti/main.sh
SHELL=/bin/bash

#The line just below enables us to use notify-send from cron
eval "export $(egrep -z DBUS_SESSION_BUS_ADDRESS /proc/$(pgrep -u $LOGNAME gnome-session)/environ)";


#This file's permission has been changed to make it executable

################################################################################
# This part needs to be changed accordingly to execute it
cd /home/abhishek/Desktop/noti

################################################################################

function notify_user {
  info=$1
  episode_name=`echo $info | sed 's/\(.*\):.*/\1/'`
  episode_no=`echo $info | sed 's/.*:\(.*\)/\1/'`

  message="${episode_no} : ${episode_name} is now available online!"
  # Use full path for notify-send(since its needed for cron)
  /usr/bin/notify-send Notifier-Alert "$message"
}

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

function match {
  key=$1
  grep $key old_info.txt 1> /dev/null 2> /dev/null
  if [ $? -eq 0 ]
  then
    echo "0" # found
  else
    echo "1" # not found
  fi
}

function update_new_info {
  info=$1
  episode_name=`echo $info | sed 's/\(.*\):.*/\1/'`
  # episode_no=`echo $info | sed 's/.*:\(.*\)/\1/'`

  #updating new info in old_info.txt
  grep $episode_name old_info.txt 1> /dev/null 2> /dev/null
  if [ $? -eq 0 ]
  then
    #Old data exists!
    sed -i "s/$episode_name.*/$info/" old_info.txt
  else
    #Old data does not exist!
    echo "$info" >> old_info.txt
  fi

  #removing redundant info from new_info.txt
  sed -i "/$episode_name.*/d" new_info.txt
}

function delete_redundant_info {
  info=$1
  sed -i "/$info/d" new_info.txt
}



if [ -f logs.txt ]
then
  rm logs.txt
fi

if [ -f new_info.txt ]
then
  rm new_info.txt
fi

if [ ! -f old_info.txt ]
then
  touch old_info.txt
fi

echo `date` >> logs.txt
echo "" >>logs.txt

echo "Checking internet connection!" >> logs.txt

# check_connection
internet_status=`check_connection` >> logs.txt

if [ $internet_status -eq 0 ]
then
  echo "Internet connection found!" >> logs.txt
  echo "" >>logs.txt

  FILES=`ls spiders`

  echo "Runnings Spiders Now!" >> logs.txt
  echo "" >>logs.txt

  cd spiders
  for spider_name in $FILES
  do
    echo "Executing $spider_name" >> ../logs.txt
    python $spider_name
  done
  cd ..

  echo "" >>logs.txt
  echo "Now parsing new info!" >> logs.txt
  echo "" >>logs.txt

  while read line
  do
    result=`match $line`
    if [ $result -eq 0 ]
    then

      echo "Deleting redundant info(shown in next line)!" >> logs.txt
      echo "$line" >> logs.txt
      echo "" >>logs.txt

      delete_redundant_info $line

    else

      echo "Updating new info(shown in next line)!" >> logs.txt
      echo "$line" >> logs.txt
      echo "" >>logs.txt

      update_new_info $line

      notify_user $line

    fi

  done < new_info.txt

  echo "New information retrieved successfully!" >> logs.txt
  echo "" >>logs.txt

else
  echo "Internet connection not found!" >> logs.txt
  echo "" >>logs.txt

fi

if [ -f new_info.txt ]
then
  rm new_info.txt
fi
