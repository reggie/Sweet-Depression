import twitter
import ordrin
from pymongo import MongoClient
from key import consumer_key, consumer_secret, access_token_key, access_token_secret, ordrin_secret

# schema
"""
    {
        twitter:
        email:
    }
"""

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
    ordrin_api = ordrin.APIs(ordrin_secret, ordrin.TEST) 
    address = ordrin_api.get_saved_addr(user["email"], "address", "password") 
    cc = ordrin_api.get_saved_cc(user["email"], "card", "password")
    print address
    print cc

user = {"email": "mannyjl625@aol.com", "twitter": "unordrin"}
send_order(user)
"""
client = MongoClient()
db = client['ordrin']
user_collection = db['users']

users = user_collection.find()
for user in users:
    get_tweets(user)
"""
