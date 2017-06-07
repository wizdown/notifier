#!/bin/bash
info=$1
episode_name=`echo $info | sed 's/\(.*\):.*/\1/'`
episode_no=`echo $info | sed 's/.*:\(.*\)/\1/'`

message="${episode_no} : ${episode_name} is now available online!"
notify-send Notifier-Alert "$message"
