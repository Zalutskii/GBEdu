from scrapy.settings import Settings
from scrapy.crawler import CrawlerProcess

from jobparser import settings
from jobparser.spiders.headhunter import HeadHunterSpider
from jobparser.spiders.superjob import SuperJobSpider

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(HeadHunterSpider)
    process.crawl(SuperJobSpider)
    process.start()
