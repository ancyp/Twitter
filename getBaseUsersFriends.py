#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv
import json

#Twitter API credentials
consumer_key = "cTYuLStEWxMh5xMQPlDE7WJy7"
consumer_secret = "YNwlxRgBofZ6pIoIURFcF4guKGdrJT4ijMoqtoiB5s9ZhX299s"
access_key = "443560601-TkQz9q8JkeZpYgqna64w6nUJyvTuhrRWHICzfGS1"
access_secret = "3RYVi2zDD0cm3Z3s4d5brhhsinxKTBgSrPPFPzaVTdC95"


def get_friends_ids(screen_name):
	
    	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	ids = api.friends_ids(screen_name = screen_name)
	resultFile = open('followee/%s_followees.csv' % screen_name,'wb')
	wr = csv.writer(resultFile,dialect = 'excel')
	wr.writerow(ids)
	print ids
	
	for idt in ids:
	    try:
		new_tweets = api.user_timeline(user_id = idt,count=200)
		with open('CharlesBatte/%s_friends_tweets.txt' % idt, 'wb') as f:
			f.write(repr(new_tweets))
		outtweets = [[tweet.id_str,tweet.created_at,tweet.user.screen_name,tweet.text.encode("utf-8")] for tweet in new_tweets]
		#write the csv	
		with open('CharlesBatte/%s_friends_tweets.csv' % idt, 'wb') as f:
			writer = csv.writer(f)
			writer.writerow(["id","created_at","text"])
			writer.writerows(outtweets)
		print 'done'
	    except:
		pass
	
if __name__ == '__main__':
	#pass in the username of the account you want to download
	get_friends_ids("CharlesBatte")
