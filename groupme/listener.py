import requests
import os

GroupMeapi = os.environ["GROUPMEAPI"]


url = f"https://api.groupme.com/v3/groups/55436013/messages?token={GroupMeapi}"


r= requests.get(url)

# # print(r.content)
# print(r.status_code)
data = r.json()
# # print(r.text)



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







