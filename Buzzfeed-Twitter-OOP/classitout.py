import tweepy
import csv
import collections 
import tweepyguide
from matplotlib.pyplot import *

'''Let's get into Twitter and grab some data!'''

class Twitter(object):

	def __init__(self, filename, number_tweets):
		'''These keys, secrets, and tokens help Twitter keep track of your usage on their API.
		It is a way to monitor and prevent wrong usage.'''

		self.consumer_key = '538LEWAOqt8hAMgTdfqoY2J1b'
		self.consumer_secret = 'xbSsONrS2mBhRn5ucU5XkKs6Mr4AK9FNKTsi07bDr4JJuEqHO5'
		self.access_token = '787933-ZQ0ljPUD2hja9ENwHqmH63nmqwHYXfMWWujkBAonNiu'
		self.access_token_secret = 'SfSeONIcOJ7DBuyOsoU5fN3NQTPqCYktC1bdwHWoLztR5'

		self.filename = filename
		self.number_tweets = number_tweets

		auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
		auth.set_access_token(self.access_token, self.access_token_secret)
		self.api = tweepy.API(auth)

		


	def get_and_save_tweets(self):
		'''We are going to open the file using csv module
		'''
		csvFile = open(self.filename, 'w')
		csvWriter = csv.writer(csvFile)

		for tweet in tweepy.Cursor(self.api.user_timeline, 
	                    screen_name="buzzfeed", 
	                    exclude_replies=True,
	                    include_rts=False).items(self.number_tweets): #items(determines your )
			csvWriter.writerow([tweet.text.encode('utf-8')])
			print tweet.created_at, tweet.text.encode('utf-8')
		csvFile.close()


	def clean_csv(self):
		'''Clean up csv data. Retrieve only numbers. 
		Return list of keys and values.'''
		csvFile = open(self.filename,'rb')
		reader = csv.reader(csvFile)

		x=''
		new_list = []
		for row in reader:
			x = row[0]
			#x = filter(str.isdigit,x[:2]) #Filter removes everything leaves what you determined in its parameters.
			if '.' not in x[:2] and str.isdigit(x[:2]) == True:
				new_list.append(x[:2])

		# Count the number of occurences
		current_count = 0
		my_dict = {}

		for number in sorted(new_list):
			current_count = my_dict.get(number,0) 
			current_count = current_count + 1
			my_dict[number] = current_count
			self.my_dict = my_dict	

		return my_dict


	def graph(self):
		'''Creates a graph from the dictionary by turning keys and 
		values into x and y graph values'''

		sort_xy = collections.OrderedDict(sorted(self.my_dict.items()))

		#declare x and y as list data types
		x_val=[]
		y_val=[]

		#append the lists
		for k, v in sort_xy.iteritems():
			x_val.append(int(k))
			y_val.append(int(v))

		#Let's draw a graph!

		title("Buzzfeed")
		ylabel('How many times was that number used?')
		xlabel('What number was used in the article title?')
		ax = gca()
		ax.tick_params(axis='x', colors='blue')
		ax.tick_params(axis='y', colors='purple')

		bar(x_val,y_val)
		show()


if __name__ == "__main__":
	x = Twitter('blahblah.csv', 300) 
	#x.get_and_save_tweets()
	x.clean_csv()
	x.graph()
	
print x.graph.__doc__

