import requests
import json

# Not for production use
# Ask user for IP and creds
# No error checking or input sanitizing 
ip = input('Hey, Pal. What is your IP?')
user = input('Alright, Pal. What is yor user?')
password = input('Great Pal. What is your password?')

#Format the request
url = f"https://{ip}/api/oauth/token?grant_type=password&username={user}&password={password}"

headers = {}
payload = {}

#Send the request
r = requests.post(url, verify=False, headers=headers, data=payload)

#Format and save token
jsondata = r.json()
token = jsondata.get('access_token')

# Read info about the loads
# This does NOT display to user
# I used it as a check that auth was working while figuring out loads

# Add the token to the request headers
headers= {'Authorization': 'Bearer {}' .format(token),}

payload = "{}"

#Format URL
url = f'https://{ip}/api/loads?load_id=1'
#Get for load data
r = requests.get(url, verify=False, headers=headers, data = payload)

# use it for load control

#Format URL note the load number 
url = f"https://{ip}/api/loads_execute/1?load_id=1"
# Set up headers
headers= {'Content-type': 'application/json', 'Authorization': 'Bearer {}' .format(token),}
# Set up data with the load command
payload = "{\"data\":{\"attributes\":{\"load_action\":\"LOAD_ACTION_OFF\",\"device_id\":1},\"type\":\"loads_execute\"}}"
# Send the request
r = requests.patch(url, verify=False, headers=headers, data=payload)
