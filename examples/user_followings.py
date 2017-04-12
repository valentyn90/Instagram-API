from InstagramAPI import InstagramAPI
import time
from datetime import datetime

username = ''
pwd      = ''
user_id  = '19343908'


API = InstagramAPI(username,pwd)
API.login()

following   = []
next_max_id = True
while next_max_id:
    print next_max_id
    #first iteration hack
    if next_max_id == True: next_max_id=''
    _ = API.getUserFollowings(user_id,maxid=next_max_id)
    following.extend ( API.LastJson.get('users',[]))
    next_max_id = API.LastJson.get('next_max_id','')

