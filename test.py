#!/usr/bin/env python
# -*- coding: utf-8 -*-

from InstagramAPI import InstagramAPI

InstagramAPI = InstagramAPI("login", "password")
InstagramAPI.login() # login
InstagramAPI.tagFeed("cat") # get media list by tag #cat
media_id = InstagramAPI.LastJson # last response JSON
InstagramAPI.like(media_id["ranked_items"][0]["pk"]) # like first media
InstagramAPI.getUserFollowers(media_id["ranked_items"][0]["user"]["pk"]) # get first media owner followers
