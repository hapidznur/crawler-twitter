from __future__ import unicode_literals, print_function
import unittest
import json
import twitter

def test_streaming_extended_tweet():
    with open('testdata/get_replies.json') as f:
        tweets = f.readlines()
    
    for tweet in tweets:
        twitter.Status.NewFromJsonDict(json.loads(tweet))


    assert isinstance(tweet, twitter.Status)
    assert tweet.text == "HIV_AIDS_BiojQuery Mobile Web Development Essentials, Second Edition: https://t.co/r78h6xfAby Quantum AI Big/Small/… https://t.co/ZPJrpMvcZG"
    assert tweet.truncated
    assert tweet.full_text == 'HIV_AIDS_BiojQuery Mobile Web Development Essentials, Second Edition: https://t.co/r78h6xfAby Quantum AI Big/Small/0 Data Cloud/Fog Computing OutLook from ClouData &amp; Multiverse -  https://t.co/cnCBNJvu6T'


def test_streaming_extended_tweet_media():
    with open('testdata/streaming/lines.json') as f:
        tweets = f.readlines()

    for tweet in tweets:
        status = twitter.Status.NewFromJsonDict(json.loads(tweet))
        assert isinstance(status, twitter.Status)
        assert status.full_text
