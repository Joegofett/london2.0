import requests
import os
import time

GroupMeapi = os.environ["GROUPMEAPI"]

def getandgrab():
    url = f"https://api.groupme.com/v3/groups/55436013/messages?token={GroupMeapi}"
    r= requests.get(url)
    data = r.json()
    testing=    data['response']
    first_form = testing['messages']
    checking = {}
    key = 0
    for info in first_form:
        checking[info['id']] = info['text']
        key += 1   
        
    for info in checking:
        text_data = str(checking[info])
        if "nl central standings" in text_data.lower():
            print('success')
    time.sleep(5)


    return checking






