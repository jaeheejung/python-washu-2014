import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, and_, or_
from sqlalchemy.orm import relationship, backref, sessionmaker
import csv

# Connect to the local database
engine = sqlalchemy.create_engine('sqlite:////Users/jaeheejung/hw7MonkeyCage.db', echo=True)
Base = declarative_base()

# Define a schema
class Scrape(Base):
	__tablename__ = "scrapes"
	
	id = Column(Integer, primary_key = True)
	post_title = Column(String)
	author = Column(String)
	publish_date = Column(String)
	is_post = Column(Integer)
	url = Column(String)
	comment_count = Column(Integer)
	
	def __init__(self, post_title, author, publish_date, is_post, url, comment_count):
		self.post_title = post_title
		self.author = self.author
		self.publish_date = self.publish_date
		self.is_post = is_post
		self.url = url
		self.comment_count = comment_count
		
	def __repr__(self):
		return "<Scrape('%s', '%s', '%s', '%s', '%s', '%s')>" % (self.post_title, self.author, self.publish_date, self.is_post, self.url, self.comment_count)

# Create the table
Base.metadata.create_all(engine)

# Create a session to store the information from the csv file
Session = sessionmaker(bind=engine)
session = Session()

# Read the csv file and create a list of the information
with open('monkeyCage.csv','rb') as f:
	read_monkeyCage = csv.DictReader(f)
	monkeyCage_info = []
	for row in read_monkeyCage:
		monkeyCage_info.append([row["post_title"], row["author"], row["publish_date"], int(row["is_post"]), row["url"], int(row["comment_count"])])

# Add the information to the session
for i in monkeyCage_info:
	session.add(Scrape(i[0], i[1], i[2], i[3], i[4], i[5]))

# Commit
session.commit()


'''
There is one problem.
I cannot commit the session because I get an error like this in line 52: 
	'(ProgrammingError) You must not use 8-bit bytestrings unless you use a text_factory that can interpret 8-bit bytestrings (like text_factory = str). It is highly recommended that you instead just switch your application to Unicode strings.'
After surfing the Internet and trying out many things, it seems that the problem is coming from the conversion of apostrophes and hyphens to weird symbols that I had for Homework 5 when writing the csv file.
When I print monkeyCage_info, the weird symbols from the csv file are changed to different symbols, something like \xe2\x80\x98.
I could not fix this problem, and was thus unable to do some querying.
''' 
