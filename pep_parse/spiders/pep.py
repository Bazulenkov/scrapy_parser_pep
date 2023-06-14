import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import NUMBER, NAME, STATUS


class PepSpider(scrapy.Spider):
    name = "pep"
    allowed_domains = ["peps.python.org"]
    start_urls = ["https://peps.python.org/"]

    def parse(self, response):
        table = response.xpath('//section[@id="numerical-index"]').css("tbody")
        anchors = table.css("tr a")
        yield from response.follow_all(anchors, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.css("h1.page-title::text").get().split(" – ")

        data = {
            NUMBER: title[0].split()[-1],
            NAME: title[-1],
            STATUS: response.css('dt:contains("Status") + dd').css("abbr::text").get(),
        }
        yield PepParseItem(data)
