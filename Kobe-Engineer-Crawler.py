import requests
import os

##########################################################################################################
#Get list of object_id from Kobe-Engineer.

token = 'EAACEdEose0cBAMuMvEEH17FuOLlxoSB4kBVCowY4NeEYZCgWbGUVkjOOHHRtZA4JKbQe98ekfZB8pI0LAMmNYZBGbP2TP8t4XFw6ojWsWI5RCkJ7ytRCXuxEBOPTYdYbhnVPZCZANzH1SbZAbSTMZCLUKQs9bw1roLZBnuOITbcnU6wZDZD'
num = 250

#Create a directory to restore the result.
result_dir = 'Result/'

if not os.path.exists(result_dir):
    os.makedirs(result_dir)

os.chdir(result_dir)

url = 'https://graph.facebook.com/v2.7/kobeengineer/?fields=feed%7Bobject_id%7D&limit=25&access_token=' + token

result = requests.get(url).json()

object_list = []

for post in result['feed']['data']:
    if 'object_id' in post:
        object_list.append(post['object_id'])


while num > 25:
    if 'feed'  in result:
        url = result['feed']['paging']['next']
    else:
        url = result['paging']['next']
    result = requests.get(url).json()

    for post in result['data']:
        if 'object_id' in post:
            object_list.append(post['object_id'])

    num -= 25


object_id_file = open('object_ids', 'w')

for id in object_list:
    object_id_file.write(id + '\n')

object_id_file.close()

##########################################################################################################
#Save picture from object.

for object_id in object_list:
    url = 'https://graph.facebook.com/' + object_id + '/picture'
    result = requests.get(url)
    picture = open(object_id + '.png', 'wb')
    picture.write(result.content)
    picture.close()
