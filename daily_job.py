import twitter
from key import consumer_key, consumer_secret, access_token_key, access_token_secret

api = twitter.Api(consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token_key=access_token_key,
        access_token_secret=access_token_secret)

statuses = api.GetUserTimeline(screen_name='unordrin')

print [s.text for s in statuses]
