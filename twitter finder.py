# Import the necessary libraries
import tweepy
import sqlite3

# Set the Twitter API credentials
consumer_key = "..."
consumer_secret = "..."
access_key = "..."
access_secret = "..."

# Authenticate with the Twitter API using the credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

# Prompt the user for the username of the account to analyze
username = input("Enter the username of the account to analyze: ")

# Get the user's followers
followers = api.followers(username)

# Loop through the followers and exclude those without profile pictures
# and those with accounts created between 2012 and 2016
filtered_followers = []
for follower in followers:
  if follower.profile_image_url and follower.created_at.year < 2012 or follower.created_at.year > 2016:
    filtered_followers.append(follower)

# Connect to a SQLite database
conn = sqlite3.connect("followers.db")

# Create a table in the database to store the filtered followers
conn.execute("CREATE TABLE IF NOT EXISTS followers (username TEXT, created_at TEXT)")

# Loop through the filtered followers and insert their usernames and creation dates
for follower in filtered_followers:
  conn.execute("INSERT INTO followers (username, created_at) VALUES (?, ?)", (follower.username, follower.created_at))

# Save the changes and close the connection to the database
conn.commit()
conn.close()

# Print the number of followers remaining after filtering
print(f"{len(filtered_followers)} followers remaining after filtering")
# Import the necessary libraries
import tweepy
import sqlite3

# Set the Twitter API credentials
consumer_key = "..."
consumer_secret = "..."
access_key = "..."
access_secret = "..."

# Authenticate with the Twitter API using the credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

# Prompt the user for the username of the account to analyze
username = input("Enter the username of the account to analyze: ")

# Get the user's followers
followers = api.followers(username)

# Loop through the followers and exclude those without profile pictures
# and those with accounts created between 2012 and 2016
filtered_followers = []
for follower in followers:
  if follower.profile_image_url and follower.created_at.year < 2012 or follower.created_at.year > 2016:
    filtered_followers.append(follower)

# Connect to a SQLite database
conn = sqlite3.connect("followers.db")

# Create a table in the database to store the filtered followers
conn.execute("CREATE TABLE IF NOT EXISTS followers (username TEXT, created_at TEXT)")

# Loop through the filtered followers and insert their usernames and creation dates
for follower in filtered_followers:
  conn.execute("INSERT INTO followers (username, created_at) VALUES (?, ?)", (follower.username, follower.created_at))

# Save the changes and close the connection to the database
conn.commit()
conn.close()

# Print the number of followers remaining after filtering
print(f"{len(filtered_followers)} followers remaining after filtering")
