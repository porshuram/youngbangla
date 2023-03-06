# all the telegram api has been disabled now. the only way is to check the terminal.
# anyone can implement telegram api. if you want i can further develop a brand new telegram api.


import requests
import time
#import urllib.request
#from telegram_api import *

TOKEN = ''      #token of telegram    #not required 
CHAT_ID = ''    #chat id of telegram  #not required
CHAT_ID2= ''    #another chat id      #not required
site='https://13.213.32.216'  #real ip of ticket.youngbangla.org

def connect(host='https://telegram.org'):
	try:
	#urllib.request.urlopen(host)
		x=requests.get(host) 
		x=x.text
		if "messaging" in x:
			return True
		else:
			print ("\nInternet error\n")
			return False
	except:
		print ("Internet error")
		return False

def checknet():
	while (not connect()):
		time.sleep(10)

def get_body(x):
	x=str(x)
	i=0
	r=''
	while (i<len(x)):
		if x[i]+x[i+1]+x[i+2]+x[i+3]=="body":
			i=i+5
			break
		i=i+1
	while not x[i]+x[i+1]+x[i+2]+x[i+3]+x[i+4]+x[i+5]=="</body":
		r=r+x[i]
		i=i+1
	return str(r)

def double_digit(x):
	x=int(x)
	if x<10:
		r="0"+str(x)
	else:
		r=str(x)
	return r

def now_date():
	s=""
	a=time.localtime()
	s=s+double_digit(a[2])+"/"
	s=s+double_digit(a[1])+"/"
	s=s+str(a[0])
	s=s+" "+double_digit(a[3])+":"+double_digit(a[4])+":"+double_digit(a[5])
	return s


checknet()
a=requests.get(site, verify=False)
a=a.text
a=get_body(a)
print (a)
#a='p'
i=0
has_changed="no change"
while (True):
	checknet()
	b=requests.get(site, verify=False)
	b=b.text
	b=get_body(b)
	if (not str(a)==str(b)):
		has_changed="changed"
		print (b)
		message=now_date()
		checknet()
		#telegram(text = "Site may be changed at "+message , token = TOKEN, chat_id = CHAT_ID)
		checknet()
		#telegram(text = "Site may be changed at "+message , token = TOKEN, chat_id = CHAT_ID2)
		print (time.localtime(),"Available now", end='\n')
    #exit ()    # if you want to terminate
		a=b
	time.sleep(60)
	print (i, " "+has_changed)
	i=i+1
