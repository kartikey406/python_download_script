from BeautifulSoup import BeautifulSoup
import requests
import pafy
import re

z=[]
m=[]
r=requests.get("https://www.youtube.com/playlist?list=PL2F07DBCDCC01493A") # enter the youtube playist url....
soup=BeautifulSoup(r.content)
for links in soup.findAll('a'):
	z.append(links.get('href'))
for element in z:
	a=re.search(r'watch.*',element,re.M|re.I)
	if a:
		m.append(a.group())
for address in m:
#while i<=200:
	url=address	
	vedio=pafy.new(url)
	best=vedio.getbest()
	best.download(quiet=False) #showing progress of download on console
#i=i+1

