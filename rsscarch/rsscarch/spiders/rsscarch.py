from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from pyquery import PyQuery as pq

class RsscarchSpider(CrawlSpider):
    
    name = 'rsscarch'
    
    allowed_domains = ['www.rsscarch.com']
    
    start_urls = [
                  'https://www.rsscarch.com/portfolio/lauri-ann-west-community-center/',
                  'https://www.rsscarch.com/portfolio/impact-church-the-landing-community-center/',
                  'https://www.rsscarch.com/portfolio/clayton-community-youth-center/',
                  'https://www.rsscarch.com/portfolio/baierl-kia/',
                  'https://www.rsscarch.com/portfolio/golden-triangle-construction/',
                  'https://www.rsscarch.com/portfolio/holy-family-parish/',
                  'https://www.rsscarch.com/portfolio/monroeville-municipal-center911-police-facility/',
                  'https://www.rsscarch.com/portfolio/three-rivers-rowing-association/',
                  'https://www.rsscarch.com/portfolio/camp-kon-o-kwee-spencer/',
                  'https://www.rsscarch.com/portfolio/200-north-meadows-office-building/',
                  'https://www.rsscarch.com/portfolio/peters-township-library/',
                  'https://www.rsscarch.com/portfolio/holy-sepulcher-parish/',
                  'https://www.rsscarch.com/portfolio/the-firepit-wood-fired-grill-restaurant/',
                  'https://www.rsscarch.com/portfolio/karndean-designflooring/',
                  'https://www.rsscarch.com/portfolio/park-classic-diner/',
                  'https://www.rsscarch.com/portfolio/baierl-family-ymca/',
                  'https://www.rsscarch.com/portfolio/carmeuse-north-american-headquarters/',
                  'https://www.rsscarch.com/portfolio/cleantown-usa/',
                  'https://www.rsscarch.com/portfolio/cranberry-township-municipal-public-safety-center/',
                  'https://www.rsscarch.com/portfolio/western-pennsylvania-humane-society/',
                  'https://www.rsscarch.com/portfolio/city-mission/',
                  'https://www.rsscarch.com/portfolio/first-presbyterian-church-of-beaver/',
                  'https://www.rsscarch.com/portfolio/mccandless-history-center/',
                  'https://www.rsscarch.com/portfolio/pittsburgh-veterinary-specialty-emergency-center/',
                  'https://www.rsscarch.com/portfolio/st-ferdinand-parish/',
                  'https://www.rsscarch.com/portfolio/the-salvation-army-pittsburgh-temple-corps/',
                  'https://www.rsscarch.com/portfolio/yerecic-label-company/',
                  'https://www.rsscarch.com/portfolio/bobby-rahal-mercedes-benz/',
                  'https://www.rsscarch.com/portfolio/sampson-family-ymca/',
                  'https://www.rsscarch.com/portfolio/wexford-vol-fire-company/',
                  'https://www.rsscarch.com/portfolio/baierl-ford/',
                  'https://www.rsscarch.com/portfolio/charter-oak-united-methodist-church/',
                  'https://www.rsscarch.com/portfolio/st-catherine-of-sweden/',
                  'https://www.rsscarch.com/portfolio/christ-church-fox-chapel/',
                  'https://www.rsscarch.com/portfolio/cranberry-township-vfc-ems/',
                  'https://www.rsscarch.com/portfolio/greenville-area-library/',
                  'https://www.rsscarch.com/portfolio/pennsylvania-state-police-jonestown/',
                  'https://www.rsscarch.com/portfolio/avonworth-community-park/',
                ]              
                   
   # Defining the rules for the page

    rules = [   

             Rule(LinkExtractor(restrict_css='_pagination')),

             Rule(LinkExtractor(restrict_css='.listitem')),  

             ]
    
    # We are getting the response object and returning the dictionary comprises of dedicated methods title, location & description
    
    # PyQuery library that allows us to use css selectors in python    

    def parse(self, response):
        
         pyquery_obj = pq(response.body)
         
         title = self.get_title(pyquery_obj)
         
         location = self.get_location(pyquery_obj)
         
         description = self.get_description(pyquery_obj)
         
         return {
                 
                 'title' : title,
                 
                 'location' : location,
                 
                 'description' : description,

                }
    # Calling each function using the pyqery 
     
    def get_title(self, pyquery_obj):
         
        return pyquery_obj('h1').text()

    def get_location(self, pyquery_obj):

        return pyquery_obj('p:first').contents()[5]

    def get_description(self, pyquery_obj):

        return pyquery_obj('p').contents()[10]
     
