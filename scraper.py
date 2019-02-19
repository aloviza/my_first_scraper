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

# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
