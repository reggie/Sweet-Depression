import twitter
from pymongo import MongoClient
from key import consumer_key, consumer_secret, access_token_key, access_token_secret

client = MongoClient()
db = client['ordrin']
user_collection = db['users']

users = user_collection.find()
for user in users:
    get_tweets(user)

def get_tweets(user):

    api = twitter.Api(consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            access_token_key=access_token_key,
            access_token_secret=access_token_secret)

    statuses = api.GetUserTimeline(screen_name=user.twitter)
    print [s.text for s in statuses]

def analyze_tweet(tweet):


def send_order(user):

