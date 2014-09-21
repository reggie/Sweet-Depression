import twitter
import ordrin
import requests

import simplejson
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

def find_restaurant(user):    

    ordrin_api = ordrin.APIs(ordrin_secret, ordrin.TEST) 
    print user["email"]
    address = ordrin_api.get_saved_addr(user["email"], "address", "password") 
    print 'sqisdfasdf'
    cc = ordrin_api.get_saved_cc(user["email"], "card", "password")

    delivery_list = ordrin_api.delivery_list("ASAP", 
                                            address["addr"], 
                                            address["city"], 
                                            address["zip"])

    for restaurant in delivery_list:
        rid = str(restaurant["id"])
        args = {"rid": rid, "target": "cake", "size": "3"}
        details = requests.get('http://foodbot.ordr.in:8000/TextSearch', 
                                params=args)
        tray = find_dessert(details)
        if tray:
            order_food(tray, rid, user, ordrin_api)
    return False

def find_dessert(details):
    if details:
        print details.text
        details_list = simplejson.loads(details.text)
        tray = details_list[0]['tray']
        return tray 
    return False

def order_food(tray, rid, user, ordrin_api):
    order = ordrin_api.order_user(rid, tray, 1.00, "Zerxsis", "the accusser", user['email'], "password", "address", "card", "ASAP") 
    print order

user = {"email": "mannyjl625@aol.com", "twitter": "unordrin"}
find_restaurant(user)

client = MongoClient()
db = client['ordrin']
user_collection = db['users']

users = user_collection.find()
for user in users:
    get_tweets(user)
