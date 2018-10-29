from decouple import config
from datetime import datetime
from model import mongo_add
import twitter
import logging
import time
import urllib
from urllib.parse import quote
import json
import datetime

consumer_key = config('CONSUMER_KEY')
consumer_secret = config('CONSUMER_SECRET')
access_token = config('ACCESS_TOKEN')
access_secret = config('ACCESS_SECRET')

api = twitter.Api(consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token_key=access_token,
    access_token_secret=access_secret,
    tweet_mode= 'extended',
    sleep_on_rate_limit=True)

def tweet_url(t):
    return "https://twitter.com/%s/status/%s" % (t.user.screen_name, t.id)

def get_tweets(filename):
    for line in open(filename):
        yield twitter.Status.NewFromJsonDict(json.loads(line))

def get_replies(tweet):
    logging.basicConfig(filename="./logs/replies.log", level=logging.INFO)
    user = tweet.user.screen_name
    tweet_id = tweet.id
    max_id = None
    logging.info("looking for replies to: %s" % tweet_url(tweet))
    while True:
        q = urllib.parse.urlencode({"q": "to:%s" % user})
        try:
            replies = api.GetSearch(raw_query=q, since_id=tweet_id, max_id=max_id, count=100)
        except twitter.error.TwitterError as e:
            logging.error("caught twitter api error: %s", e)
            time.sleep(60)
            continue
        for reply in replies:
            logging.info("examining: %s" % tweet_url(reply))
            if reply.in_reply_to_status_id == tweet_id:
                logging.info("found reply: %s" % tweet_url(reply))
                yield reply
                # recursive magic to also get the replies to this reply
                for reply_to_reply in get_replies(reply):
                    yield reply_to_reply
            max_id = reply.id
        if len(replies) != 100:
            break

def get_search(text):
    raw_query='q=%s&result_type=recent&since=2018-08-10&count=1000' % (quote(text))
    results = api.GetSearch(raw_query=raw_query)
    for result in results:
        data = {}
        data['id_tweet'] = result.id_str
        data['user_name'] = result.user.name
        data['user_username'] = result.user.screen_name
        data['text'] = result.full_text
        data['user_id'] = result.user.id
        # change twitter format to YYYY-MM-DD HH:MM:SS
        data['created_at'] = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(result.created_at,'%a %b %d %H:%M:%S +0000 %Y'))
        if result.retweeted_status:
            data['retweet_count'] = result.retweet_count
            data['retweeted_username'] = result.retweeted_status.user.screen_name
            data['retweeted_id_tweet'] = result.retweeted_status.id_str
            data['tweet_created'] = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(result.retweeted_status.created_at,'%a %b %d %H:%M:%S +0000 %Y'))
            # get_replies(result)
            mongo_add(data)
            replies = {}
            for reply in get_replies(result.retweeted_status):
                replies['id_tweet'] = reply.id_str
                replies['user_name'] = reply.user.name
                replies['user_username'] = reply.user.screen_name
                replies['text'] = reply.full_text
                replies['user_id'] = reply.user.id
                replies['in_reply_to_user_id'] = reply.in_reply_to_user_id
                replies['in_reply_to_screen_name'] = reply.in_reply_to_screen_name
                replies['from'] = 'search'
            mongo_add(replies)

def stream():
    logging.basicConfig(filename="./logs/stream.log", level=logging.INFO)
    text = ['Pembakaran Bendara', 'Banser', 'MUI', 'Tauhid', 'Laskar Tauhid']
    logging.info("crawling on: %s" % datetime.datetime.now())
    output = './../data-twitter/%s.txt' % datetime.datetime.now().timestamp()

    with open(output, 'a') as f:
        # api.GetStreamFilter will return a generator that yields one status
        # message (i.e., Tweet) at a time as a JSON dictionary.
        for line in api.GetStreamFilter(track=text, filter_level='low'):
            f.write(json.dumps(line))
            f.write('\n')

def trends_location(woeid =  None):
    if woeid == None:
        woeid = config('Indonesia')
        
    output = './../data-twitter/trends-%s-%s.txt' % (woeid, datetime.datetime.now().timestamp())   
    
    with open(output, 'a') as f:
        for line in api.GetTrendsWoeid(woeid):
            # class dict object to json
            f.write(json.dumps(line.__dict__))
            f.write('\n')
