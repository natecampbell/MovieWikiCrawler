import scrapy

"""
Item attributes for Movie details
"""

class MovieWikiCrawlerItem(scrapy.Item):
    title = scrapy.Field()
    poster = scrapy.Field()
    directed_by = scrapy.Field()
    starring_cast = scrapy.Field()
    release_date = scrapy.Field()
    imdb_link = scrapy.Field()
    imdb_id = scrapy.Field()
