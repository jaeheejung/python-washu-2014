'''
This script is a revision to the original hw6.py I submitted.
I made the revision because there were problems with the original script. I need it to work correctly to do homework 7.
'''

import csv
import tweepy

# Authentication information deleted

# Specify the target
pt = api.get_user('senecadoane')

'''
Task 1: The most followed user that follows my target
'''

# Get the target's followers' IDs
pt_followers = pt.followers_ids(pt.screen_name)

# Define a function that creates a list of the numbers of followers of the target's followers
def grab_followers(num1, num2):
	followers_of_followers = []
	for i in range(num1, num2):
		follower = api.get_user(pt_followers[i])
		followers_of_followers.append(follower.followers_count)
	return followers_of_followers

# Since 180 is the rate limit, calculate how many cycles of requests I should make
number_of_iterations = len(pt_followers) / 180
leftover = len(pt_followers) % 180

# In this case, since the target has 90 followers, no need to worry
followers_of_followers = grab_followers(0, 90)

# Store the list followers_of_followers, along with followers' IDs, in a csv file
with open('number_of_followers.csv', 'wb') as number_of_followers:
	followers_writer = csv.DictWriter(number_of_followers, fieldnames = ("follower's ID", "number of followers"))
	followers_writer.writeheader()
	for i in range(len(followers_of_followers)):
		followers_writer.writerow({"follower's ID": pt_followers[i], "number of followers": followers_of_followers[i]})

# Find the follower with the largest number of followers
max_index = followers_of_followers.index(max(followers_of_followers))
print pt_followers[max_index]


'''
Task 4: The most active user my target follows
(I define the most active to mean the largest number of status counts)
'''

# Get target's friends' IDs
pt_friends = api.friends_ids(pt.screen_name)

# Define a function that creates a list of the status counts of target's friends
def grab_friends(num1, num2):
	friends_status_counts = []
	for i in range(num1, num2):
		friend = api.get_user(pt_friends[i])
		friends_status_counts.append(friend.statuses_count)
	return friends_status_counts

# Since 180 is the rate limit, calculate how many cycles of requests I should make
number_of_iterations = len(pt_friends) / 180
leftover = len(pt_friends) % 180

# In this case, the target has 123 friends.
friends_status_counts = grab_friends(0, 123)

# Store the list friends_status_counts, along with friends' IDs, in a csv file
with open('status_count_friend.csv', 'wb') as status_count_friend:
	friends_writer = csv.DictWriter(status_count_friend, fieldnames = ("friend's ID", "status count"))
	friends_writer.writeheader()
	for i in range(len(friends_status_counts)):
		friends_writer.writerow({"friend's ID": pt_friends[i], "status count": friends_status_counts[i]})

# Find the friend with the largest status count
max_index = friends_status_counts.index(max(friends_status_counts))
print pt_friends[max_index]