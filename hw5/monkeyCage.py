## Scraper to collect Monkey Cage Blogs

from bs4 import BeautifulSoup
import csv 
from nltk.util import clean_html
import urllib2 
import re
import time

# I will scrape articles from July, since August articles continue to update
page_to_scrape = 'http://www.washingtonpost.com/blog/monkey-cage/Archive/201407'

# Column names
headers = ["post_title", "author", "publish_date", "is_post", "url", "comment_count"]

# Create the csv file to write into
writeFile = open("monkeyCage.csv", "wb")
csvwriter = csv.writer(writeFile)
csvwriter.writerow(headers)

# Open webpage
webpage = urllib2.urlopen(page_to_scrape)

# Parse it
soup = BeautifulSoup(webpage.read())
soup.prettify()
		
# Extract article title
titles = soup.findAll("h2", attrs={'class':'entry-title'})

time.sleep(2)

# Extract the author
authors = soup.findAll("div", attrs={'class':'blog-byline'})

time.sleep(2)

# Extract the time and the date 
dates = soup.findAll("span", attrs={'class':'updated'})

# Indicate that the page is a post if articles are listed in reverse chronological order
dates_list = []
for i in range(95):
	date = dates[i]
	date = clean_html(str(date))  # Clean up the markup
	date = date.split(", ")[1::]  # Get rid of the time part
	date = ''.join(date)  # Join month, day, and year as a string
	date = date.replace('/','')  # Get rid of the forward slashes
	date = int(date)  # Make it an integer, which should be bigger for later dates in July 2014
	dates_list.append(date)
posts_list = []
for i in range(94):
	if dates_list[i] >= dates_list[i+1]:  # Compare two contiguous dates
		posts_list.append(True)
		if i + 1 == 94:  # Add True to the last article if the previous article got True
			posts_list.append(True)
	else:
		posts_list.append(False)
		if i + 1 == 94:  # Add False to the last article if the previous article got False
			posts_list.append(False)

# Extract url
urls = soup.findAll("a", attrs = {"href": re.compile("^http://www.washingtonpost.com/blogs/monkey-cage/wp/2014/07")})
urls = urls[::3]  # Get only the every third urls because there are duplicates

time.sleep(2)

# Extract the number of comments
comments = soup.findAll("span", attrs={"class": "count-bubble"})

# Get the information into the csv file
for i in range(95)[::-1]:  # Reverse the loop to sort the file chronologically
	title = titles[i]
	post_title = clean_html(str(title.find("a")))
	author = authors[i]
	author = "".join(clean_html(str(author)).split("By ")[1::])  # Get rid of "By" in front of author
	date = dates[i]
	publish_date = clean_html(str(date))
	post = posts_list[i]
	is_post = int(post)  # Represent True and False as integer
	link = urls[i]
	url = link['href']  # Get the href part
	comment = comments[i]
	comment_count = clean_html(str(comment))
	csvwriter.writerow([post_title, author, publish_date, is_post, url, comment_count])

writeFile.close()


'''
There are two things to note about my implementation.
First, although there is no problem with the source code, in the csv file, all apostrophes are turned into weird symbols. Matt told us to leave them for now.
Second, I tried a different way to get the number of comments.
I tried to pass through the comments link for every article and count the comments from there, because there was mismatch between the actual number of comments and the number of comments presented in the original url.
However, the source code from the different url did not indicate anything about the comments. I talked about this with Matt, and was told to just get the "incorrect" number of comments for now.
The problem is probably because Javascript that creates the comments section runs only after the html prints.
'''