# webcrawler-rsscarch
The goal is to crawl http://www.rsscarch.com and scrape all projects that are listed on the website. Projects returned from the spider should have three properties present: title, location, and description



# Pre-requisites

To start working on your first assignment, you should have installed the following on your computer:
Python (https://www.python.org/)
Scrapy (https://scrapy.org/)
PyQuery (https://pythonhosted.org/pyquery/)

# Create your first Scrapy project

Go to the folder where you want your scrapy project to be located
1. Run scrapy startproject rsscarch (this task is about crawling http://www.rsscarch.com)
2. Create rsscarch.py in rsscarch/rsscarch/spiders 
3. You have now set up the environment and the Scrapy project. You're ready to start writing code! 

# Task & result

The goal is to crawl http://www.rsscarch.com and scrape all projects that are listed on the website. Projects returned from the spider should have three properties present: title, location, and description. Workflow
So that we can reviewed your code fastly, we've set up few guidelines you should consider:

## 1. Structure of a spider

A spider should be extended from CrawlSpider (scrapy.spiders.CrawlSpider)
The crawling part of a spider should be based on crawling rules that use CSS selectors (see https://doc.scrapy.org/en/latest/topics/spiders.html#scrapy.spiders.Rule) 
The parsing part should utilize PyQuery (i.e. you extract project field values using PyQuery)
The extraction of every field should have it's own method (e.g. title should be extracted using get_title method)

## 2. Running and debugging a spider

You can run a spider with scrapy crawl <your_spider_name>. 
