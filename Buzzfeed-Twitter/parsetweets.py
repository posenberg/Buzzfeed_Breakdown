import csv 
import collections 
import tweepyguide
from matplotlib.pyplot import *
import numpy as np


def clean_csv(tweepy):
	'''Clean up csv data. Retrieve only numbers. 
	Return list of keys and values.'''

	reader = csv.reader(file1)

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

	return my_dict


def graph(list_values):
	'''Creates a graph from the dictionary by turning keys and 
	values into x and y graph values'''

	sort_xy = collections.OrderedDict(sorted(list_values.items()))

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
	file1 = open('new.csv', 'rb')
	filtered_list= clean_csv(file1)
	graph(filtered_list)
	file1.close() 
