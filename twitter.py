import tweepy
import pandas as pd

api_key = 'Yfu3srwb1mWRifoWZ945oaxjq'
access_token_secret = 'o3n6EjKEYga1Ane3OlNzxSeRCbKiOy9YAscGZL3c5xve9'

auth = tweepy.OAuthHandler(api_key, 'jB84T3vZoX8VYxGO76jfV9lI7fFFCY0hUuOw7I1udxj0DKuPIy')
auth.set_access_token('1536251385154785280-wS9O4mqu7vwVMdA1dYPNWLz5DoIqSS', access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

print(public_tweets)

data = []
col = ['Time', 'User', 'Tweet']

for tweet in public_tweets:
    print(tweet.text)
    print(tweet.created_at)
    print(tweet.user.name)

    data.append([tweet.created_at, tweet.user.name, tweet.text])

    print(data)

    df = pd.DataFrame(data, columns=col)
    df.to_csv('tweets.csv', index=False)
