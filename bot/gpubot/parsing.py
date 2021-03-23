import tweepy
import re
import csv
import sys
import time
#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print("new status!")
        print(status.text)

    def on_error(self, status_code):
        if status_code == 420:
            return False
    
TWITTER_CONSUMER_KEY = "2xlFQWsDhXfaQHXr0VmKrLAeT"
TWITTER_CONSUMER_SECRET = "7AvCRx9mbFmJl41CC7EkPjCMqhS1ZCvRnIXUQaVKrGf0owmVcq"
TWITTER_ACCESS_TOKEN = "1094960355384745985-y0jBDRVhFqutGIglWbu0DDcZ6ijmiS"
TWITTER_ACCESS_TOKEN_SECRET = "9XFd2R1qSWVBKLTSVvnG72bcjfSF01QOfrmsmsxmO5qeZ"
# setup Twitter API connection details
twitter_auth = tweepy.OAuthHandler( TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET )
twitter_auth.set_access_token( TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET )
api = tweepy.API(twitter_auth)

# part_name_match = re.compile('((?<=#pa_)\w+)')


# myStreamListener = MyStreamListener()
# myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
# print(myStream)

# myStream.filter(follow=["1314575666130694144"])
# # myStream.filter(track=["covid", "vaccine", "google", "Google", "nft", "bitcoin", "BTC", "ETC", "NFT"])

parsable_tweets = open("previous_gpus.csv", "w")
errored = open("errored.txt", "w")

header = "Date,Part,Price,Description,URL\n"
parsable_tweets.write(header)


tweets = api.user_timeline(screen_name = 'PartAlert', count = 200, include_rts = False, tweet_mode='extended')
oldest_tweet = tweets[-1].id

while tweets:
    tweets = api.user_timeline(screen_name = 'PartAlert', count = 200, max_id = oldest_tweet, include_rts = False, tweet_mode='extended')
    print(oldest_tweet)
# print(tweets[0].full_text)
# print(tweets[0].entities['urls'][1]['expanded_url'])
# for status in tweets:
#     # print(status.full_text)
#     # print(f"Part: {status.entities['hashtags']['text']}")
#     part = re.findall('((?<=#pa_)\w+)', status.full_text)
#     price = re.findall('((?<=€|£)\d+)[.](\d+)', status.full_text)
#     print(f"Date: {status.created_at}")
#     print(f"Part: {part[0]}")
#     print(f"Price: {price[0][0]}.{price[0][1]}")
#     print(f"URL: {status.entities['urls'][1]['expanded_url']}")
#     print("-------------------------------")


    for status in tweets:
         try:
             part = re.findall('((?<=#pa_)\w+)', status.full_text)
             price = re.findall('((?<=€|£)\d+)[.](\d+)', status.full_text)
             description = re.findall('(?<=: )[\s\S]+(?=https)', status.full_text)[0].replace("\n", "").replace(",", ".")
             url = status.entities['urls'][1]['expanded_url'].replace(",", ".")
             parsable_tweets.write(f"{status.created_at},{part[0]},{price[0][0]}.{price[0][1]},{description},{url}\n")
         except:
            errored.write(status.full_text) 
            errored.write("\n------------------------------------------------\n")
    tweets = api.user_timeline(screen_name = 'PartAlert', max_id = oldest_tweet, count = 200, include_rts = False, tweet_mode='extended')
    oldest_tweet = tweets[-1].id
    time.sleep(3)


parsable_tweets.close()
errored.close()