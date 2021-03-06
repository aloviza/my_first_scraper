# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful
# The next two lines import two libraries. Scraperwiki is a library of scrapers used for scraping webpages.
import scraperwiki
import lxml.html
#
print("Hello")
# # Read in a page
html = scraperwiki.scrape("http://foo.com")
# "https://www.catskillhiker.net/Catskill35/peak_list.shtml")
# 
print(html)
#This has scraped the full html code from that website.

# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
print(root.cssselect("a"))
print(root.cssselect("div#footer"))
print(root)
# This line always finds a list, even if there's nothing in the list.

record = {}

# Separate out the different items in the list:
listofmatches = root.cssselect("a")
for match in listofmatches:
  print(match)
  print(lxml.html.tostring(match))
  record["link"]=lxml.html.tostring(match)
  print(record)
  scraperwiki.sqlite.save(unique_keys=["link"],data=record)

secondrecord = {}
  
secondlistofmatches = root.cssselect("div#footer")
for matchtwo in secondlistofmatches:
  print(matchtwo)
  print(lxml.html.tostring(matchtwo))
  secondrecord["footer"]=lxml.html.tostring(matchtwo)
  print(secondrecord)
  scraperwiki.sqlite.save(unique_keys=["footer"],data=secondrecord)
  

# Make a dictionary of the items you've scraped - go back before the loop [for, in lists] begins

  
# # Write out to the sqlite database using scraperwiki library  -- inside the loop
# scraperwiki.sqlite.save(
# (unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
