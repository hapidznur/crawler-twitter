import twitter_crawl 
import datetime
import sys
input = sys.argv
print(datetime.datetime.now())
if input[1] == 'stream':
    twitter_crawl.stream()
elif input[1] == 'trends':
    twitter_crawl.trends_location()
else:
    print('Anda belum input pilihan stream atau trends')