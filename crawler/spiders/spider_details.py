import scrapy
from scrapy.loader import ItemLoader
from crawler.items import Litigation
import datetime
class SpiderDetails(scrapy.Spider):
    name = "spider_details"


    def start_requests(self):

        start_urls = ['https://www.sec.gov/litigation/litreleases.shtml']
        for i in range(2018, 2019):
            start_urls.append('https://www.sec.gov/litigation/litreleases/litrelarchive/litarchive{0}.shtml'.format(i))
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parseMaster)


    def parseMaster (self,response):
        codes=response.xpath('//tr[count(@id) = 0]/td[1]/a/text()').extract()
        date_as_string=response.xpath('//tr[count(@id) = 0]/td[2]/text()')[0].extract()
        actual_date=datetime.datetime.strptime(date_as_string, "%b. %d, %Y").date()
        year=actual_date.year
        for code in codes:
            if year > 2005:
                yield scrapy.Request(url='https://www.sec.gov/litigation/litreleases/{0}/lr{1}.htm'.format(year,code[3:]), callback=self.parse)
            else:
                yield scrapy.Request(
                    url='https://www.sec.gov/litigation/litreleases/lr{0}.htm'.format(year, code[3:]), callback=self.parse)

    def parse(self, response):
        itemLoader = ItemLoader(item=Litigation(), response=response)
        itemLoader.add_xpath('title', '//h1/text()')
        itemLoader.add_xpath('subtitle', '//h2/text()')
        itemLoader.add_xpath('content', '//div[@class="grid_7 alpha"]/p/text()')
        return itemLoader.load_item()