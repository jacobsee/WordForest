# Getting Started 

Word Forest was written for Python 3.5.2. If you're on a Mac and you have [Homebrew](http://brew.sh/) installed, you can install Python 3 by running `brew install python3` in a terminal. After ensuring that you have Python 3, you'll need the dependencies `pygraphml` and `tweepy`, which can be installed with `pip install pygraphml tweepy`. 

You will also need a Twitter API key, which you can get by creating a new app [on this page](https://apps.twitter.com/). These API keys will need to be filled into `download_tweets.py` and `run_wordforest.py`. I will probably move these to one single location in the future.

# Running the Word Forest Bot

Once your keys are filled in, you can run the Word Forest bot with `python3 run_wordforest.py`. You will probably want to edit the stream filter away from listening for mentions of `@wordforest`, since you don't own that account.

# Testing Word Forest

If you don't want to set up an account for your instance to listen and respond on, you can simply use Word Forest through commands on the terminal; `download_tweets.py` will still need API keys, however.

First, you will need to download the tweets for a certain account by running 

`python3 download_tweets.py <username>`. 

For instance, 

`python3 download_tweets.py taylorswift13`.

The downloader will tell you how many tweets it was able to grab. 1000 is good, 2000 or more is great. You will then need to generate your Markov chains based on this tweet data as follows:

`python3 generate_chains.py taylorswift13`

You only need to generate chains once per account. Finally, run the following as many times as you wish to repeatedly generate sentences based on these Markov chains:

	python3 generate_sentence.py taylorswift13
	> Happy 22nd birthday to someone who is SUPPOSED TO BE ON MY SIDE! Smh.

Also, if you're on a Mac, you can add the `-say` directive to have the Text to Speech system read the output!

`python3 generate_sentence.py -say taylorswift13`

# Inspecting The Chain

Word Forest outputs a `graph.graphml` file alongside some others in `downloaded\<username>`. This file can easily be inspected if you download [yEd](https://www.yworks.com/products/yed). Have yEd open the `graph.graphml` file and go to Layout > Organic for a cool graph visualization of the Markov chain!