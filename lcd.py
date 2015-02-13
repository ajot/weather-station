##for this project i used tweepy Liberay 
##Import Libraries that will be used to make the code run

import tweepy
from tweepy import OAuthHandler
import serial
import time
import random # import randint

##authenticate yourself with twitter project

ckey = 'DEq4mc7eYWUIsATvBniIhg'
csecret = 'Jm7VBSt31xsZKqi7PWAtMEAwn91BtzbwttJoezRnDs'
atoken = '7236102-98zriKzMjy72XCxbdzdWp8RTZq8nmFZeVnojoVr8BE'
asecret = 'TX4HY6tLUUSSiygaxtiSvOEUTJ0QqZGJVnMSq7s'



auth = OAuthHandler(ckey, csecret) 
auth.set_access_token(atoken, asecret)
auth.secure = True
api = tweepy.API(auth)

##set to your serial port for the adurino 
ser = serial.Serial('/dev/tty.usbmodem1431', 9600)

## check serial port
def checkokay():
	ser.flushInput()
	time.sleep(3)
	line=ser.readline()
	time.sleep(3)

	if line == ' ':
		line=ser.readline()
	print 'here'
## Welcome message
print 'Welcome To Project Tweetn Switch!'

#create switch on funcrion 
def switchon():
    
    
    # display = str(randint(100,1000)) #Inclusive
    names = ["amit","deepti","niki","mom","dad"]
    display = random.choice(names)
    print display
    ser.write(str(display))
    
    # status = []
    # x = 0
    #
    # status = api.user_timeline('evil_amit') ##grab latest statuses from the user
    #
    # checkIt = [s.text for s in status] ##put status in an array
    #
    # drip = checkIt[0].split() ## this will split first tweet into words
    # print drip[0]
    # # ser.write(str(drip[0]))
    #
    # ## check for match and write to serial if match
    # if drip[0] == '#on':
    #     print 'Tweet Recieved, Switching On Light'
    #     ser.write('1')
    # elif drip[0] == '#off': ##break if done
    #     ser.write('0')
    #     print 'Switched Off Light, Awaiting for more instructions instructions.'
    # else:
    #     ser.write('0')
    #     print 'Awaiting Tweet instruction'
		
while 1:
	switchon() ## call switchon function
	time.sleep(10) ## sleep for 10 seconds to avoid rate limiting
	