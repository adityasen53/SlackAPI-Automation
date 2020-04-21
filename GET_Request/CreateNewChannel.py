import requests
import json
import jsonpath
#1. Create a new Channel & Joining the new channel

CreateChannelURL = "https://slack.com/api/channels.create"
file = open("C:\\Users\\adsen\\PycharmProjects\\AdityaPython\\json_inputs\\CreateChannel.json","r")
json_input = file.read()
requests_json = json.loads(json_input)
response = requests.post(CreateChannelURL,requests_json)
response_obj = json.loads(response.text)
id = response_obj["channel"]["id"]
old_name = response_obj["channel"]["name"]
print("Channel name before using Rename API: ",old_name)

#2 Join the New Channel
#Channel gets already joined when a user creates a channel from the same auth-token.

#3. Rename the Channel

RenameURL = "https://slack.com/api/conversations.rename"
f = open("C:\\Users\\adsen\\PycharmProjects\\AdityaPython\\json_inputs\\RenameChannel.json","r")
requests_json1 = json.loads(f.read())
requests_json1["channel"]  = id
response2 = requests.post(RenameURL,requests_json1)
response_obj2 = json.loads(response2.text)
new_name = response_obj2["channel"]["name"]
print("Channel name after using Rename API: ",new_name)

#4. List all the channels

ChannelListURL = "https://slack.com/api/channels.list"
response3 =  requests.get(ChannelListURL,requests_json1)
channel_list = json.loads(response3.text)

#5 Archive the channel

ArchiveChannelURL = "https://slack.com/api/conversations.archive"
response4 = requests.post(ArchiveChannelURL,requests_json1)
print("Channel is archived", response4.text)

#6 Validate if the Channel is archived successfully

response4 = requests.post(ArchiveChannelURL,requests_json1)
print("Channel is already archived", response4.text)




