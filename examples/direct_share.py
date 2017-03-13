from InstagramAPI import InstagramAPI
user,pwd = '', ''                           #your credentials
InstagramAPI = InstagramAPI(user,pwd)       
InstagramAPI.login()                        # login
mediaId='1469246128528859784_1520706701'    #a media_id
recipients = []                             #array of user_ids. They can be strings or ints
InstagramAPI.direct_share(mediaId, recipients,text='aquest es es darrer')