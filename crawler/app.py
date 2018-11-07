import twitter_crawl 
import datetime
import sys
input = sys.argv
print(datetime.datetime.now())
if input[1] == 'stream':
    twitter_crawl.stream()
elif input[1] == 'trends':
    twitter_crawl.trends_location()
elif input[1] == 'test':
    import json
    # d = {
    #         "id" : "1057260677331439624",
    #         "user": {
    #             "screen_name" : "hendraIG"
    #         },
    #     }

    # dt = json.dumps(d)
    # # dt = json.loads(dt)
    # te = twitter_crawl.get_tweets(dt)
    # twitter_crawl.get_replies(te)
    # for reply in twitter_crawl.get_replies(te):
    #     print(reply)
    print('Anda belum input pilihan stream atau trends')