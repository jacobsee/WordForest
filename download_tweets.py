import tweepy
import os
import csv
import sys
import re

def get_all_tweets(screen_name):

	consumer_key = ""
	consumer_secret = ""
	access_key = ""
	access_secret = ""

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	alltweets = []
	textoutput = []

	new_tweets = api.user_timeline(screen_name = screen_name,count=500)

	alltweets.extend(new_tweets)

	oldest = alltweets[-1].id - 1

	while len(new_tweets) > 0:
		print("getting tweets before %s" % (oldest))

		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)

		alltweets.extend(new_tweets)

		oldest = alltweets[-1].id - 1

		print("...%s tweets downloaded so far" % (len(alltweets)))

	outtweets = []

	for tweet in alltweets:
		line = re.sub("b('|\")", "BEGIN NOW ", str(tweet.text.encode("utf-16"))[:-1] + " END")
		line = re.sub("\\n", " ", line)
		line = re.sub("\\\\x..", "", line)
		line = re.sub("\\\\", "", line)
		line = re.sub("@\\S+", "", line)
		line = re.sub("http\\S+", "", line)
		line = re.sub("www\\S+", "", line)
		outtweets.append([tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")])
		textoutput.append(line)

	if not os.path.exists('downloaded/%s' % screen_name):
	    os.makedirs('downloaded/%s' % screen_name)

	with open('downloaded/%s/tweets.csv' % screen_name, 'w') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text"])
		writer.writerows(outtweets)

	with open('downloaded/%s/tweets.txt' % screen_name, 'w') as f:
		for item in textoutput:

			f.write("%s\n" % item)

	pass


if __name__ == '__main__':
	get_all_tweets(sys.argv[1])
