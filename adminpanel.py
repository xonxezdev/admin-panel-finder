##hargai pembuat!! jangan copas!
from urllib2 import Request, urlopen, URLError, HTTPError
import sys
import random 
import datetime


H = '\033[95m'
B = '\033[94m'
G = '\033[92m'
W = '\033[93m'
F = '\033[91m'
E = '\033[0m'
U = '\033[4m'
O = '\033[33m'


def on():
	word = open("link.txt","r");
	print U+"ex. google.com or www.google.com"+E
	link = raw_input(G+"Site_> "+E)
	if link == '':
		print "exiting"
		sys.exit(1)
	print G+"\n\nAvailable links : \n"+E
	while True:
		exploit = word.readline()
		if not exploit:
			break
		vuln = "http://"+link+"/"+exploit
		req = Request(vuln)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		except KeyboardInterrupt:
			print F+"exiting from program..."+E
			sys.exit(1)
		else:
			print G+"OK => "+E,G+vuln+E
			
			
def credit():
	print B+U+'''                                                                      '''+E
	print O+'''[X] Author : '''+G+'''N0p3'''+E                                         
	print O+'''[X] Thanks to :'''+G+''' God - all member xonxez.'''+E      
	print F+'''[X] Us3 Y0u sk1ll Dud3!'''+E                                            
	print B+U+'''                                                                      '''+E
	
	
credit()
on()