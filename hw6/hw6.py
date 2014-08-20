import tweepy
import csv

# I got rid of my authentication information

# Matt is my target
md = api.get_user('mcdickenson')


'''
Task 1: The most followed user that follows my target
'''

# Get Matt's followers' IDs
md_followers = md.followers_ids(md.screen_name)

# Define a function that creates a list of the numbers of followers of Matt's followers
def grab_followers(num1, num2):
	followers_of_followers = []
	for i in range(num1, num2):
		follower = api.get_user(md_followers[i])
		followers_of_followers.append(follower.followers_count)

# Since 180 is the rate limit, calculate how many cycles of requests I should make
number_of_iterations = len(md_followers) / 180
leftover = len(md_followers) % 180

# In this case, since Matt has 313 followers, I first make one full cycle of 180 requests
grab_followers(0, 180)

# Store the list followers_of_followers in a csv file
number_of_followers = open('number_of_followers.csv', 'wb')
followers_writer = csv.writer(number_of_followers)
for i in range(len(followers_of_followers)):
	follower_of_follower = followers_of_followers[i]
	followers_writer.writerow([follower_of_follower])

# After 15 minutes, resume to make additional 133 requests	
grab_followers(180, 313)

# Make sure to append rather than writing the cvs file anew
number_of_followers = open('number_of_followers.csv', 'a')
followers_writer = csv.writer(number_of_followers)
for i in range(len(followers_of_followers)):
	follower_of_follower = followers_of_followers[i]
	followers_writer.writerow([follower_of_follower])

# Then read the csv file to get the full list of the numbers of followers of Matt's followers
with open('number_of_followers.csv', 'rb') as f:
  followers_reader = csv.reader(f)
  followers_of_followers = []
  for row in followers_reader:
    followers_of_followers.extend(row)

# Find the follower with the biggest number of followers
max_index = followers_of_followers.index(max(followers_of_followers))
print md_followers[max_index]


'''
Task 4: The most active user my target follows
(I define the most active to mean the largest number of status counts)
'''

# Get Matt's friends' IDs
md_friends = api.friends_ids(md.screen_name)

# Define a function that creates a list of the status counts of Matt's friends
def grab_friends(num1, num2):
	friends_status_counts = []
	for i in range(num1, num2):
		friend = api.get_user(md_friends[i])
		friends_status_counts.append(friend.statuses_count)

# Since 180 is the rate limit, calculate how many cycles of requests I should make
number_of_iterations = len(md_friends) / 180
leftover = len(md_friends) % 180

# In this case, since Matt has 216 friends, I first make one full cycle of 180 requests
grab_friends(0, 180)

# Store the list friends_status_counts in a csv file
status_count_friend = open('status_count_friend.csv', 'wb')
friends_writer = csv.writer(status_count_friend)
for i in range(len(friends_status_counts)):
	friend_status_count = friends_status_counts[i]
	friends_writer.writerow([friend_status_count])

# After 15 minutes, resume to make additional 36 requests.	
grab_friends(180, 216)

# Make sure to append rather than writing the cvs file anew
status_count_friend = open('status_count_friend.csv', 'a')
friends_writer = csv.writer(status_count_friend)
for i in range(len(friends_status_counts)):
	friend_status_count = friends_status_counts[i]
	friends_writer.writerow([friend_status_count])

# Then read the csv file to get the full list of the status counts of Matt's friends
with open('status_count_friend.csv', 'rb') as f:
  friends_reader = csv.reader(f)
  friends_status_counts = []
  for row in friends_reader:
    friends_status_counts.extend(row)

# Find the friend with the largest status count
max_index = friends_status_counts.index(max(friends_status_counts))
print md_friends[max_index]
	