import scrapy
import os

class TitleSpider(scrapy.Spider):
    name = "title_spider"
    start_urls = ['https://www.isna.ir',
                  'https://www.irna.ir'
                  ]
    No_pages = 50
    start_urls += ['https://www.isna.ir/page/archive.xhtml?mn=12&wide=0&dy=12&ms=0&pi={0}&yr=1400' for p in range(1, No_pages+1)]
    start_urls += ['https://www.irna.ir/page/archive.xhtml?mn=12&wide=0&dy=12&ms=0&pi={0}&yr=1400' for p in range(1, No_pages+1)]

    def parse(self, response):
        titles_list1 = response.css('section .items .desc > h3 > a::text').getall()
        titles_list2 = response.css('.news > .desc > h3 > a::text').getall()
        titles_list = titles_list1 + titles_list2
        titles = '\n'.join(titles_list)
        filename = 'titles.txt'    
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(titles)
        print("** number of title news: {0} **".format(len(titles_list)))   
