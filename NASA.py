import urllib
import datetime
import time
import urllib2
from datetime import date, timedelta

i=4000     #this will upload 4000 pics in the current directory
page=''
image_line=''
opener=urllib2.build_opener()
nasa_img='nasa'

while i<0:
	today=date.today()-datetime.timedelta(days=(i+1))  #although it starts on today, if runned for a long time
	#the program will have some duplicates,  if it passes the 11:59PM-12:00AM sector
	today=today.strftime('%y%m%d')
	print today
	script=urllib.urlopen('http://apod.nasa.gov/apod/ap'+str(today)+'.html')
	source=script.read()
	start=source.find('C="image')
	end=source.find('"',start+3)
	image_line=source[start+3:end]
	try:
		image='http://apod.nasa.gov/apod/'+str(image_line)
		image_page=opener.open(image)
		picture=image_page.read()
		filename=nasa_img+str(i)+image_line[-4:]      #I believe there is something wrong with the photo extends
		#i could make a note to fix it......
		print filename                                #tells us we have a pic
		image_file=open(filename,"wb")
		image_file.write(picture)
		image_file.close
	except:
		print "Did not print"		#like I care for 1 pic,  oh there are some videos for some reason
	i+=1
