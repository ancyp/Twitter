#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv
import json
import time
#Twitter API credentials
consumer_key = "6uVOqNbitF3iaLTvolXp3RRhW"
consumer_secret = "ezbjUtyaSvrOQbg7zwLi7aELFfwMjVh1J6TpLQnuTLHMXiyQLC"
access_key = "443560601-WRmPXHqJVZa50a6sZi55RwuC5unZF8UOCvj02zyI"
access_secret = "O9p47u8xdch96ES3C8oST4GS07DlVlPqITqc9FsompN9b"


def get_friends_ids(reader):
	
    	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	for row in reader:	
		try:
			print 'in for'
			ids = api.friends_ids(screen_name = row[0])
			resultFile = open('followee_all/%s_followee.csv' % row[0],'wb')
			wr = csv.writer(resultFile,dialect = 'excel')
			wr.writerow(ids)
			print 'wrote %s'% row[0]
		except tweepy.TweepError,e:
			print e
			if 'Not authorized.' in e:
					print 'in that'
					continue
			time.sleep(60*15)
			pass
	
if __name__ == '__main__':
	#pass in the username of the account you want to download
	with open('dataset_users.csv', 'rb') as f:
	    reader = csv.reader(f)
	    get_friends_ids(reader)
