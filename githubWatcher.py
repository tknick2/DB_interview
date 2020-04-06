###################################################################################################
# DrugBank Interview Assignment
# Tim Knickerbocker
# Created April 3, 2020
#
# This program will watch a supplied github repo for new issues and closed issues and reports 
# their title and id to the terminal. In addition, for each report, it will display the total number
# of issues in the repo and the number of closed issues. 
# 
# Note: Python is not my strongest language, so there are several cases in which I  
# used loops to manipulate data within collections. I am sure there are collection methods that 
# can do lots of these things, but I don't have enough experience with Python to be confident in 
# their use. That said, I am confident in the logic and functionality of the program.
####################################################################################################
import requests
import json
from time import sleep
from datetime import datetime

################################################################
# Description:  creates a string from a python object 
# Accepts:      issue (issue object)
# Returns:      void
################################################################
def jprint(issue):    
    
    print("Issue Title: " + issue['title']) 
    print("Issue ID: " + str(issue['id']))

################################################################
# Description:  prints a new issue, and the current number 
#               of existing open issues and closed issues 
#               to the terminal with appropriate label messages
# Accepts:      issue (issue object), issues (collection of issues)
# Returns:      void
################################################################
def ProcessIssue(issue, issues):
    
    if issue['state'] == "open":        
        print("New Issue!!!!")
        jprint(issue)
    elif issue['state'] == "closed":
        print('Closed Issue!!!!')
        jprint(issue)
    
    closedIssues = 0
    allIssues = 0

    # sum the total issues and closed issues
    for issue in issues:        
        if issue['state'] == "closed":
            closedIssues += 1
        allIssues += 1

    # display total issues and closed issues to the terminal
    print("Total Issues: " + str(allIssues))
    print("Closed Issues: " + str(closedIssues))


################################################################
# Description:  moves any new events into the eventsToProcess 
#               collection
# Accepts:      issue (issue object)
# Returns:      returnEvents (collection of events that require processing)
################################################################
def FindNewEvents(eventsAll, eventsHandled):
        
    eventsToProcess = []

    #add event objects that require processing to the return collection and return
    for event in eventsAll:
        
        handled = False

        # see if the event is present in both collections
        for eventHandled in eventsHandled:
            if event['id'] == eventHandled['id']:
                handled = True
                break

        # event not handled yet...add it to the return collection    
        if not handled:
            eventsToProcess.append(event)
    
    return eventsToProcess

# event management collections, chose collection for incoming events in case there is more than 1 at a time
eventsHandled = []
eventsToProcess = []

#git API URLs for the repo of interest
issuesURL = "https://api.github.com/repos/omxhealth/t-k-interview/issues"
eventsURL = "https://api.github.com/repos/omxhealth/t-k-interview/events"

# main loop
while True:
    
    # no need to retrive data more often than 2 seconds, sometimes the return is slow anyway
    sleep(2)

    # status update
    print("Checking for Issues...")

    # retrieve all current events and issues
    response = requests.get(eventsURL, auth=requests.auth.HTTPBasicAuth("tknick2", "GitIsGr8"))
    events = response.json()    
    response = requests.get(issuesURL, {"state": "all"}, auth=requests.auth.HTTPBasicAuth("tknick2", "GitIsGr8"))
    issues = response.json()

    # fill the processing buffer    
    eventsToProcess = FindNewEvents(events, eventsHandled)

    # process new events
    for event in eventsToProcess:        
        for issue in issues:            
            
            # ensures there is an issue with the appropriate state, then displays it, and adds it to the handled collection
            if 'action' in event['payload'] and event['type'] == "IssuesEvent" and (event['payload']['action'] == "closed" or event['payload']['action'] == "opened") and issue['id'] == event['payload']['issue']['id']:
                ProcessIssue(issue, issues)                
                eventsHandled.append(event)
                break
