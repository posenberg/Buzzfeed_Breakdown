import tweepy
import csv

'''Let's get into Twitter and grab some data!'''


def auth():

	'''These keys, secrets, and tokens help Twitter keep track of your usage on their API.
	It is a way to monitor and prevent wrong usage.'''

	consumer_key = '538LEWAOqt8hAMgTdfqoY2J1b'
	consumer_secret = 'xbSsONrS2mBhRn5ucU5XkKs6Mr4AK9FNKTsi07bDr4JJuEqHO5'
	access_token = '787933-ZQ0ljPUD2hja9ENwHqmH63nmqwHYXfMWWujkBAonNiu'
	access_token_secret = 'SfSeONIcOJ7DBuyOsoU5fN3NQTPqCYktC1bdwHWoLztR5'

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	api = tweepy.API(auth)

	return api

def get_and_save_tweets(api, filename):
	
	'''We are going to open the file using csv module
	'''
	
	csvFile = open(filename, 'w')
	csvWriter = csv.writer(csvFile)

	for tweet in tweepy.Cursor(api.user_timeline, 
                    screen_name="buzzfeed", 
                    exclude_replies=True,
                    include_rts=False).items(100): 
		csvWriter.writerow([tweet.text.encode('utf-8')])
		print tweet.created_at, tweet.text.encode('utf-8')

	csvFile.close()

if __name__ == "__main__":
	access_keys = auth()
	get_and_save_tweets(access_keys, 'new.csv')
