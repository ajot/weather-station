##Import Libraries that will be used to make the code run

#import library to do http requests:
import urllib2, simplejson

#import pyserial - a Python library that encapsulates the access for the serial port
import serial
#import time library for delays
import time
#Importing the API Config from the file api_config.py
import api_config


##set to your serial port for the adurino 
ser = serial.Serial('/dev/tty.usbmodem1431', 9600)

## Welcome message
print 'Getting Started'

#create find_weather function 
def find_weather():
    
    print "Making call now"    
    #Setting the API call URL for Wunderground API to get current temperature for the zip code 10016
    url ='http://api.wunderground.com/api/%s/conditions/q/NY/10016.json' % (api_config.WEATHER_API_KEY)
    # Making the request
    req = urllib2.urlopen(url).read()
    raw = simplejson.loads(req)

    #Grabbing the temperature in Fahrenheit and Celsius 
    temp_f = int(round(raw['current_observation']['temp_f']))
    temp_c = int(round(raw['current_observation']['temp_c']))
    display = "%s F, %s C" % (str(temp_f),str(temp_c))
    
    print str(temp_f) + " F"
    print str(temp_c) + " C"
    print "Last Updated: " + time.strftime("%c")
    
    ser.write(display) #Writing the variable "display" to the serial port, which is then ready by our code running on the Arduino and is then displayed on the LCD.
            		
while 1: #update the weather on the LCD every 60 seconds. 
	find_weather() ## call find_weather function
	time.sleep(60) ## sleep for 60 seconds to avoid rate limiting