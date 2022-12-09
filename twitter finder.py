# Import the necessary libraries
import tweepy
from datetime import datetime

# Authenticate with Twitter using your API keys
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Get a list of your followers
followers = api.followers()

# Filter out followers without profile pictures and whose accounts were created between 2012 and 2016
filtered_followers = []
for follower in followers:
  if follower.profile_image_url and 2012 <= follower.created_at.year <= 2016:
    filtered_followers.append(follower)

# Print the remaining followers
for follower in filtered_followers:
  print(follower.screen_name)
