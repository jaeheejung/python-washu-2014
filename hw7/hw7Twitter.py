import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, and_, or_
from sqlalchemy.orm import relationship, backref, sessionmaker
import csv

# Connect to the local database
engine = sqlalchemy.create_engine('sqlite:////Users/jaeheejung/hw7Twitter.db', echo=True)
Base = declarative_base()

# Define schema
class Follower(Base):
	__tablename__ = "followers"
	
	id = Column(Integer, primary_key = True)
	follower_id = Column(String)
	number_of_followers = Column(Integer)
	
	def __init__(self, follower_id, number_of_followers):
		self.follower_id = follower_id
		self.number_of_followers = self.number_of_followers

class Friend(Base):
	__tablename__  = "friends"
	
	id = Column(Integer, primary_key = True)
	friend_id = Column(String)
	status_count = Column(Integer)
	
	def __init__(self, friend_id, status_count):
		self.friend_id = friend_id
		self.status_count = status_count
	
# Create the table
Base.metadata.create_all(engine)

# Create a sessionfol to store information from the csv files
Session = sessionmaker(bind=engine)
session = Session()

# Read number_of_followers.csv and create a list of the information
with open('number_of_followers.csv','rb') as f:
	read_followers = csv.DictReader(f)
	followers_info = []
	for row in read_followers:
		followers_info.append([row["follower's ID"], int(row["number of followers"])])

# Add the information to the session
for i in followers_info:
	session.add(Follower(i[0], i[1]))

# Commit
session.commit()

# Read status_count_friend.csv and create a list of the information
with open('status_count_friend.csv','rb') as f:
	read_friends = csv.DictReader(f)
	friends_info = []
	for row in read_friends:
		friends_info.append([row["friend's ID"], int(row["status count"])])

# Add the information to the session
for i in friends_info:
	session.add(Friend(i[0], i[1]))

# Commit
session.commit()


# Query
for follower in session.query(Follower).order_by(Follower.number_of_followers):
	print follower.follower_id, follower.number_of_followers

for friend in session.query(Friend).order_by(Friend.status_count):
	print friend.friend_id, friend.status_count
	
	
'''
There is one problem with the implementation.
For some reason, number of followers, which is an integer, is converted to None in the for loop in line 55.
That is, i[1] in line 56, which is the number of followers, becomes None when it is used as an argument to Follower.
I do not understand why. Follower's ID, indicated by i[0], is a string and has no problem.
It is even more puzzling because status count in the class Friend does not have such a problem.
Status count is also an integer, as number of followers is in the class Follower.
Yet, in the for loop in line 70, i[1] is not turned into None.
'''