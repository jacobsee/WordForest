import tweepy
from download_tweets import get_all_tweets
from generate_chains import generate_chain
from generate_sentence import generate_sen

consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

print("Subscribed to streaming updates for '@WordForest'")

class MyStreamListener(tweepy.StreamListener):

	def on_status(self, status):

	    print('Received request for user: ' + status.user.screen_name)

	    print('Downloading tweets now')
	    get_all_tweets(status.user.screen_name)
	    print('Generating chains now')
	    generate_chain(status.user.screen_name, False)
	    for i in range(0,3):
	    	reply = ('@' + status.user.screen_name + " " + generate_sen(status.user.screen_name))[:140]
	    	print('Replying: ' + reply)
	    	api.update_status(reply)


	def on_error(self, status_code):
		if status_code == 420:
			return False

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=['@wordforest'])
