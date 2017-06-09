1) To add a new notifier, simply create a new spider in python
   that parses the output into the form
   episode_name:episode_number
   and add it to spiders folder

2) Few changes are required in main.sh
   a) Change its permission to 764
   b) Modify the starting line of code to change your current directory to
      the one where it resides.
   c) Modify notify_user function as per your need. Also use full path for
      the commands used to notify users. Full path can be found by using
      whereis <your-command-to-notify>

3) crontab command
   0,15,30,45 <path-to-script>
