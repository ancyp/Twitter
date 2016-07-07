#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv
import json
import time
import ast

#Twitter API credentials


consumer_key = "cSZWonJEd6Jhgf1bNlWqUYTLR"
consumer_secret="7mFyMhkapCCuu1QR4XTasGKBzzc9bUkRegqTrepzxejqh1yVfS"
access_key="1683267092-XjHQtg7tSHBCakZJvFPcqEGWFUb2uAc98LzJoJy"
access_secret="q1xMi2zaDPkJ2b4SlQSO1Q0s2Dm3GCq8lkP71D8iUJZol"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


#get the followees of followers

def tweets(screen_name):
	
				
			    try:
					new_tweets = api.user_timeline(screen_name = screen_name,count=200)
					with open('%s_user_detail.txt'% screen_name , 'a+') as f:
						f.write(repr(new_tweets[0].user))
							
					outtweets = [[tweet.id_str,tweet.created_at,tweet.user.screen_name,tweet.text.encode("utf-8"),tweet.entities,tweet.favorite_count,tweet.lang,tweet.retweet_count] for tweet in new_tweets]
						#write the csv	
					with open('tweets.csv', 'a+') as f:
						writer = csv.writer(f)
						writer.writerow(["id","created_at","screen name","text","entities","fav count","lang","retweet count"])
						writer.writerows(outtweets)
					print 'done'
			    except Exception,e:
                                        print e
					
				



if __name__ == '__main__':
	#pass in the username of the account you want to download

	tweets("GlennCosby")
	tweets("Elli_Eats")

