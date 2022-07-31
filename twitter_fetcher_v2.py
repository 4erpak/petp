"""
Script to get data from the tweets with hashtag #DevOps
"""

import tweepy
import config
import json

TOKEN = config.BEARER_TOKEN

client = tweepy.Client(bearer_token=TOKEN)

QUERY = '#DevOps -is:retweet -is:reply has:hashtags'

tweets = client.search_recent_tweets(query=QUERY,\
                                    user_fields=['username'],\
                                    tweet_fields=['id', 'entities'],\
                                    expansions=['author_id'] ,max_results=10)

# Get users list from the includes object
users = {u["id"]: u for u in tweets.includes['users']}

for tweet in tweets.data:
    tweet_id = tweet.id
    print(f'Tweet ID: {tweet_id}')
    if users[tweet.author_id]:
        user = users[tweet.author_id]
        user_name = user.username
        print(f'User Name: {user.username}')
        print('Hashtags:')
        # DEBUG. To navigate tweets easily:
        #print(f'Tweet URL: https://twitter.com/{user.username}/status/{tweet.id}')
        for i in tweet.entities['hashtags']:
            for k,v in i.items():
                if k == 'tag':
                    print(v)
