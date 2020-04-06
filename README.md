# DB_interview
Instructions
1. Run script in a Python 3 shell
2. Make sure you have the requests library installed
3. Output will be displayed in the terminal

Technologies Used
1. Python 3.6.9 
2. Requests library https://requests.readthedocs.io/en/master/
3. JSON library https://docs.python.org/3/library/json.html
4. time library 
5. datetime library

Requirements

The task is to use the github API to watch for new issues. The documentation of the github API can be found here: https://developer.github.com/v3/. The deliverable is a program in a language of your choice (preferably ruby/python/node) that:

1. watches for new issues and reports them (with title, id, other info if you like, but fairly compact)
    * the script runs in a loop and reports the title and id of any issue that is added in, continuation of the loop is indicated by "Checking for issues..." being displayed to the terminal
2. reports issues being closed (with same info as above)
    * the same loop will display the title and id for issues that have been closed
3. whenever an issue is added/closed, reports the number of total existing/closed issues, but does not show details of the other issues
    * after each issue title and id are displayed, the total number of existing issues and the number of closed issues will be displayed
4. does not need to use a database/persistence
    * in its current state the script will display all current issues at runtime, then begin to monitor for future issues
5. you may use libraries (eg. npm/rubygems/pypi), but not a github client library
    * installed "requests" library
6. Is delivered as a github repo or a zip file of code
    * This repo, zip file will be sent by email

The script will be tested against a repository we have created: https://github.com/omxhealth/t-k-interview. You may create/close issues as needed on this repository while you’re working on the program. Once we have finished evaluating your program, we will delete the repository.
