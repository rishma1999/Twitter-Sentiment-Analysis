#TWITTER SENTIMENT ANALYSIS PROJECT


import tweepy
from textblob import TextBlob
import csv
import matplotlib.pyplot as plt


#4 variables that authenticating with Twitter will require

consumer_key = 'kuGQ9xelr3aTj5ScYNEngMaJ1'
consumer_secret_key = 'GcfGGZo8FlFBtd40l6l2MBBQQv0zKbz2ZrHP9maUMoQYG8mFMx'

access_token = '4644206357-CqoRy7thnfFcOs3fyvzmZakjvi8P5bXRvZjdl3q'
access_token_secret = 'MuvY9HfHan5eFdKUvs4To2tf97YY9QZK9JPAgH87MzH4m'


#login via code along with the Oauth handler method for Tweepy, the method uses the arguments to perform its internal calculations
# auth is an authentication variable
auth = tweepy.OAuthHandler(consumer_key,consumer_secret_key)  #2 arguments

auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth) #api is a main variable


keyword = input('Enter the keyword you want to search tweets for: ')
l = input("Enter the language for tweets to be searched for: ")
cnt = input("Enter the number of tweets you wish to display: ")
choice = input('Do you wish to search for tweets in a specific location? (Enter y or n): ')

if choice == 'n':
	public_tweets = api.search(keyword, lang = l, count = cnt)   #public_tweets variable is going to store a LIST of tweets

else:
	c = input("Enter the latitude and longitude for the location you wish to search for: ")

	c = c + ",50000km"
	public_tweets = api.search(keyword, geocode = c, lang = l,count = cnt)


cp = 0
cn = 0
cne = 0

#search method will retrieve a bunch of tweets with the given keyword
with open('tweets.csv', 'w',encoding='utf-16') as file:
	writer = csv.writer(file)
	tweets = []
	for tweet in public_tweets:
		analysis = TextBlob(tweet.text)
		
		if(analysis.sentiment.polarity>0):
			cp = cp +1
			tone = "Sentiment: Positive"
		elif (analysis.sentiment.polarity<0):
			cn = cn + 1
			tone = "Sentiment: Negative"
		elif (analysis.sentiment.polarity == 0):
			cne = cne + 1
			tone = "Sentiment: Neutral"

		tweets.append([tweet.text])
		tweets.append([analysis.sentiment])
		tweets.append([tone])
		tweets.append(["______________________________________________________________________________________________________________"])

	for i in tweets:
		writer.writerow(i)    	


# CREATING A PIE CHART AND A BAR GRAPH

labels1 = ['Positive','Negative','Neutral']
colours = ['lightskyblue','lightcoral','gold']
sizes = [cp,cn,cne]
explode = (0.1,0,0)

left = [1,2,3]  # How many bars are needed


height = [cp,cn,cne] #OR sizes = [cp,cn,cne]

labels2 = ['Positive', 'Negative', 'Neutral']

colours = ['lightskyblue','lightcoral','gold']


plt.figure(1)
plt.pie(sizes, explode=explode, labels=labels1, colors=colours,autopct='%1.1f%%', shadow=True, startangle=140)

plt.figure(2)
plt.bar(left, height, tick_label = labels2, width = 0.8, color = colours)

plt.xlabel('Sentiments')
plt.ylabel('Count')

plt.title('Sentiment Analysis Bar Graph')

plt.show()
















 