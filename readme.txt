1) To add a new notifier, simply create a new spider in python
   that parses the output into the form
   episode_name:episode_number
   and add it to spiders folder

2) Also main.sh and notify_user.sh are executable files. So changed
   permission accordingly.(764 for both)

3) notify_user.sh would require changes depending on how the user
   wants to notify himself/herself.

4) main.sh should not be editted by user.(except for its permissions)
