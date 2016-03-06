import urllib2
import re
from BeautifulSoup import BeautifulSoup
#match = re.findall(r'href=[\"]?([^\'" >]+)', content)

html = open('List_of_United_States_cities_by_population', 'r')

#method # 2

soup = BeautifulSoup(html)
table = soup.find("table", {"class":"wikitable sortable"})
rows = list()
for i in table.findAll("tr"):
    rows.append(i)
#print len(rows)
match = BeautifulSoup()
cities = list()
for i in range(1, 100):
    match = rows[i].find("td", {"align":"left"})
    #print match.text
    cities.append(match.text)
city_to_areanames = {}
for i in range(len(cities)):
    city_name = ""
    city_name =  cities[i].split("[")[0]
    print city_name + ":" 
    url = 'http://www.geonames.org/postalcode-search.html?q=' + city_name + '&country=US'
    soup = BeautifulSoup(urllib2.urlopen(url).read())
    for i in range(1, 50, 2):
        print soup.findAll('table')[2].findAll('tr')[i].findAll('td')[2].contents,
        #soup.findAll('table')[2].
        #findAll('tr')[i].findAll('td')[1].contents,
    print


#fetching area names and postalcode from second dataset or link http://www.geonames.org/postalcode-search.html?q=Kansas+city&country=US

'''
url = 'http://www.geonames.org/postalcode-search.html?q=Kansas+city&country=US'
soup = BeautifulSoup(urllib2.urlopen(url).read())
for i in range(1, 50, 2):
    print soup.findAll('table')[2].findAll('tr')[i].findAll('td')[2].contents, soup.findAll('table')[2].    findAll('tr')[i].findAll('td')[1].contents
    print

'''

