from BeautifulSoup import BeautifulSoup
import requests
import pafy
import re
z=[]
m=[]
r=requests.get("https://www.youtube.com/playlist?list=PL2F07DBCDCC01493A")
soup=BeautifulSoup(r.content)
for links in soup.findAll('a'):
	z.append(links.get('href'))
for element in z:
	a=re.search(r'watch.*',element,re.M|re.I)
	if a:
		m.append(a.group())
#print m[32]
for address in m:
#i=18
#print m[19]
#while i<=200:
	url=address	
	vedio=pafy.new(url)
	best=vedio.getbest()
	best.download()
#i=i+1

