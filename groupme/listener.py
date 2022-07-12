from hashlib import new
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
    new_data = {}
    key = 0
    for info in first_form:
        new_data[info['id']] = info['text']
        key += 1   
    used_messages = {}
    old_messages ={}
    keytwo = 0
    for info in new_data:
        oldkey = str(new_data[info])

    return oldkey
       
       
       
        # if oldkey in old_messages[info]:
        # else:
        #     for data in new_data:
        #         text_data = str(new_data[data])
        #         if "nl central standings" in text_data:
        #             old_messages[data] = text_data
        #             print("NL central standings")
                

    # for info in new_data:
    #     text_data = str(new_data[info])
    #     if "nl central standings" in text_data.lower():
    #         used_messages[keytwo] = info
    #         print("nl standings")
    #     elif  old_messages in text_data.lower():
    #         old_messages[keytwo] = info
    #         print('old message added') 
    #     else:
    #         print("No messages added")   







