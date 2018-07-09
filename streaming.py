import twitter
from decouple import config

consumer_key = config('CONSUMER_KEY')
consumer_secret = config('CONSUMER_SECRET')
access_token = config('ACCESS_TOKEN')
acesss_secret = config('ACCESS_SECRET')

twitter = Twitter(auth = OAuth(access_token,access_secret,consumer_key,consumer_secret))

# source from https://github.com/ideoforms/

# User Timeline
user = "ideoforms"

#-----------------------------------------------------------------------
# query the user timeline.
# twitter API docs:
# https://dev.twitter.com/rest/reference/get/statuses/user_timeline
#-----------------------------------------------------------------------
results = twitter.statuses.user_timeline(screen_name = user)

#-----------------------------------------------------------------------
# loop through each status item, and print its content.
#-----------------------------------------------------------------------
for status in results:
    print("(%s) %s" % (status["created_at"], status["text"].encode("ascii", "ignore")))

#-----------------------------------------------------------------------
# retrieve global trends.
# other localised trends can be specified by looking up WOE IDs:
#   http://developer.yahoo.com/geo/geoplanet/
# twitter API docs: https://dev.twitter.com/rest/reference/get/trends/place
#-----------------------------------------------------------------------
results = twitter.trends.place(_id = 23424975)

print("UK Trends")

for location in results:
    for trend in location["trends"]:
        print(" - %s" % trend["name"])

#-----------------------------------------------------------------------
# perform a basic search 
# twitter API docs: https://dev.twitter.com/rest/reference/get/statuses/user_timeline
#-----------------------------------------------------------------------
results = twitter.statuses.user_timeline(screen_name = user)

#-----------------------------------------------------------------------
# loop through each of my statuses, and print its content
#-----------------------------------------------------------------------
for status in results:
    print("@%s %s" % (user, status["text"]))

            #-----------------------------------------------------------------------
# do a new query: who has RT'd this tweet?
                    #-----------------------------------------------------------------------
retweets = twitter.statuses.retweets._id(_id = status["id"])
for retweet in retweets:
    print(" - retweeted by %s" % (retweet["user"]["screen_name"]))


#-----------------------------------------------------------------------
# request my home timeline
# twitter API docs: https://dev.twitter.com/rest/reference/get/statuses/home_timeline
#-----------------------------------------------------------------------
statuses = twitter.statuses.home_timeline(count = 50)
print(statuses)

#-----------------------------------------------------------------------
# loop through each of my statuses, and print its content
#-----------------------------------------------------------------------
for status in statuses:
    print("(%s) @%s %s" % (status["created_at"], status["user"]["screen_name"], status["text"]))


#-----------------------------------------------------------------------
# perform a user search 
# twitter API docs: https://dev.twitter.com/rest/reference/get/users/search
#-----------------------------------------------------------------------
results = twitter.users.search(q = '"New Cross"')

#-----------------------------------------------------------------------
# loop through each of the users, and print their details
#-----------------------------------------------------------------------
for user in results:
    print("@%s (%s): %s" % (user["screen_name"], user["name"], user["location"]))



#-----------------------------------------------------------------------
# perform a basic search 
# twitter API docs: https://dev.twitter.com/rest/reference/get/search/tweets
#-----------------------------------------------------------------------
terms = "pink elephants"
query = twitter.search.tweets(q = terms)
results = query["statuses"]

                  #-----------------------------------------------------------------------
                  # take the timestamp of the first and last tweets in these results,
                  # and calculate the average time between tweets.
                  #-----------------------------------------------------------------------
first_timestamp = datetime.strptime(results[0]["created_at"], created_at_format)
last_timestamp = datetime.strptime(results[-1]["created_at"], created_at_format)
total_dt = (first_timestamp - last_timestamp).total_seconds()
mean_dt = total_dt / len(results)

                  #-----------------------------------------------------------------------
                  # print the average of the differences
                  #-----------------------------------------------------------------------
print("Average tweeting rate for '%s' between %s and %s: %.3fs" % (terms,
results[-1]["created_at"], results[ 0]["created_at"], mean_dt))
