import twitter
from pymongo import MongoClient
from key import consumer_key, consumer_secret, access_token_key, access_token_secret

def get_tweets(user):
    api = twitter.Api(consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            access_token_key=access_token_key,
            access_token_secret=access_token_secret)

    statuses = api.GetUserTimeline(screen_name=user["twitter"])
    for s in statuses[:3]:
        print s.text
        if sad_tweet(s.text):
            send_order(user)

def sad_tweet(tweet):
    sadness = [":(", "):", ":'(",")':", "hack"]
    for s in sadness:
        if s in tweet:
            return True
    return False

def send_order(user):
    
    print 'sending order'    

client = MongoClient()
db = client['ordrin']
user_collection = db['users']

users = user_collection.find()
for user in users:
    get_tweets(user)
