
    # TWITTER_CONSUMER_KEY = "2xlFQWsDhXfaQHXr0VmKrLAeT"
    # TWITTER_CONSUMER_SECRET = "7AvCRx9mbFmJl41CC7EkPjCMqhS1ZCvRnIXUQaVKrGf0owmVcq"
    # # TWITTER_ACCESS_TOKEN = "1094960355384745985-y0jBDRVhFqutGIglWbu0DDcZ6ijmiS"
    # # TWITTER_ACCESS_TOKEN_SECRET = "9XFd2R1qSWVBKLTSVvnG72bcjfSF01QOfrmsmsxmO5qeZ"

	# # setup Twitter API connection details
	# twitter_auth = OAuthHandler( TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET )
	# # twitter_auth.set_access_token( TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET )
    # api = tweepy.API(twitter_auth)
	
	# # connect to Twitter Streaming API
	# twitter_stream = Stream( twitter_auth, output )

	# # filter tweets using track, follow and/or location parameters
	# # https://dev.twitter.com/streaming/reference/post/statuses/filter
	# twitter_stream.filter(track=[ TWITTER_HASHTAG ])


# def cleanup():
	# twitter_stream.disconnect() 

import tweepy
#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
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

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
print(myStream)

myStream.filter(follow=["1314575666130694144", "1329697243524444160"])
# myStream.filter(track=["rtx3060", "rtx", "3060", "3070"])



# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)