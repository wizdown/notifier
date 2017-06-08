1) To add a new notifier, simply create a new spider in python
   that parses the output into the form
   episode_name:episode_number
   and add it to spiders folder

2) Also main.sh and notify_user.sh are executable files. So changed
   permission accordingly.(764 for both)

3) notify_user.sh would require changes depending on how the user
   wants to notify himself/herself.

4) A small change is required in main.sh (apart from changing its permissions)
   Modify the starting line of code to change your current directory to
   the one where it resides. This is done only for the ease of adding main.sh
   to crontab.
