import urllib2
from bs4 import BeautifulSoup as bs
import re
import sys 
from prettytable import PrettyTable

response = urllib2.urlopen('http://www.espncricinfo.com/ci/engine/match/index.html?view=live')
html = response.read()
soup = bs(html, "html.parser")

if len(sys.argv) < 3:
	print "Usage: python ipl.py team1 team2"
	exit(1)

if sys.argv[1]=="rcb":
	team1="royal challengers bangalore"
elif sys.argv[1]=="srh":
	team1="sunrisers hyderabad"	
elif sys.argv[1]=="kkr":
	team1="kolkata knight riders"	
elif sys.argv[1]=="mi":
	team1="mumbai indians"	
elif sys.argv[1]=="dd":
	team1="delhi daredevils"	
elif sys.argv[1]=="gl":
	team1="gujarat lions"	
elif sys.argv[1]=="rps":
	team1="rising pune supergiants"	
elif sys.argv[1]=="kxip":
	team1="kings XI punjab"							


if sys.argv[2]=="rcb":
	team2="royal challengers bangalore"
elif sys.argv[2]=="srh":
	team2="sunrisers hyderabad"	
elif sys.argv[2]=="kkr":
	team2="kolkata knight riders"	
elif sys.argv[2]=="mi":
	team2="mumbai indians"	
elif sys.argv[2]=="dd":
	team2="delhi daredevils"	
elif sys.argv[2]=="gl":
	team2="gujarat lions"	
elif sys.argv[2]=="rps":
	team2="rising pune supergiants"	
elif sys.argv[2]=="kxip":
	team2="kings XI punjab"


team1.replace(" ", "_")
team1.replace(" ", "_")
ing = 0
team1 = team1.replace("_", " ")
ing1team1 = False
team2 = team2.replace("_", " ")

table = PrettyTable(['Innings', 'Team', 'Runs/Wickets', 'Overs'])

mydivs = soup.findAll("div", { "class" : "innings-info-1" })
for div in mydivs:
	if re.search('^[^a-zA-Z]*'+team1+'[^a-zA-Z]*', div.text,re.IGNORECASE):
		x = div.text
		if(len(team1.split()) > 1):
			x = div.text.replace(team1, team1.replace(" ", "_"))
		ing1team1 = True
		s = x.split()
		break
	if re.search('^[^a-zA-Z]*'+team2+'[^a-zA-Z]*', div.text,re.IGNORECASE):
		x = div.text
		if(len(team2.split()) > 1):
			x = div.text.replace(team2, team2.replace(" ", "_"))
		ing1team1 = False
		s = x.split()
		break

try:
	if s[1] == "oh no":
		pass
except NameError:
	print "No Match Found"
	sys.exit()
else:
	pass

if ing1team1:
	table.add_row(['I', team1, s-[3], s[-1][1:].split('/')[0]])
else:
	table.add_row(['I', team2, s[-3], s[-1][1:].split('/')[0]])

mydivs = soup.findAll("div", { "class" : "innings-info-2" })
for div in mydivs:
	if ing1team1:
		if re.search('^[^a-zA-Z]*'+team2+'[^a-zA-Z]*', div.text):
			x = div.text
			if(len(team2.split()) > 1):
				x = div.text.replace(team2, team2.replace(" ", "_"))
			s = x.split()
			break
	else:
		if re.search('^[^a-zA-Z]*'+team1+'[^a-zA-Z]*', div.text):
			x = div.text
			if(len(team1.split()) > 1):
				x = div.text.replace(team1, team1.replace(" ", "_"))
			s = x.split()
			break

if len(s) < 3:
	if ing1team1:
		table.add_row(['II', team2, "NA", "NA"])
	else:
		table.add_row(['II', team1, "NA", "NA"])

else:
	if ing1team1:
		table.add_row(['II', team2, s[-3], s[-1][1:].split('/')[0]])
	else:
		table.add_row(['II', team1, s[-3], s[-1][1:].split('/')[0]])	

print table