import tweepy
import json
from aylienapiclient import textapi

consumer_key = "I6FeiBAfaab1hgjYZQEHQOdTZ"
consumer_secret = "rOYbpoYnMtP30Dyva9DO9vTQDjkFIf6fqkmSkO3Rnbkx1lmChS"

access_token = "610493776-egqp8tplvSDqhYZCyvv1kkPseNYFCr1T6apUFLlJ"
access_token_secret = "p1YoFpxLQ88OqzOh2mgHjymQYqpgydUCrgmK9hFJVuTYV"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#data = api.me()
#print(json.dumps(data._json, indent=2))

search_results = api.search(q="@ceres_tag", count=3200)
#search_results = api.search(q="@Apple", count=3200)
#search_results = api.search(q="#agribusiness", count=3200)

csv = ""
for i in search_results:
    result = i._json
    #print(json.dumps(i._json, indent=2))
    #print(i["user"]["description"])
    try:
        description = result["user"]["description"].replace("\n","")
        #if(description.strip() != ''):
        followers_count = result["user"]["followers_count"]
        name = result["user"]["name"]
        created_at = result["user"]["created_at"]
        favourites_count = result["user"]["favourites_count"]
        retweet_count = result["retweet_count"]
        location = result["user"]["location"]

        print(description + "," + str(followers_count))
        csv += description + ',' 
        csv += str(followers_count) + ',' 
        csv += name + ','
        csv += created_at + ','
        csv += str(favourites_count) + ',' 
        csv += str(retweet_count) + ','
        csv += location
        csv += "\n"
        #print(json.dumps(i._json, indent=2))
        #break
    except Exception as identifier:
        pass
    
    #csv += json.dumps(i._json, indent=2)

with open('twee.csv', 'wb') as archivo:
    archivo.write(csv.encode())
    archivo.close()

client = textapi.Client("1fe73851", "e6655d7f5e51072533a66890a80e4e14")