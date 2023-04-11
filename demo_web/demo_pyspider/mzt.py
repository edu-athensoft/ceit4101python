"""
project:
"""

from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('https://www.mzitu.com/', headers={'Referer': 'https://www.mzitu.com'}, callback=self.index_page,
                   validate_cert=False)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('.postlist li a').items():
            self.crawl(each.attr.href, headers={'Referer': 'https://www.mzitu.com'}, callback=self.detail_page,
                       validate_cert=False)
        next = response.doc('.next').attr.href
        self.crawl(next, headers={'Referer': 'https://www.mzitu.com'}, callback=self.index_page, validate_cert=False)

    @config(priority=2)
    def detail_page(self, response):
        for each in response.doc('p img').items():
            self.crawl(each.attr.src, headers={'Referer': 'https://www.mzitu.com'}, callback=self.detail_page2,
                       validate_cert=False)
        next_two = response.doc('.pagenavi').find('a').eq(-1).attr.href
        self.crawl(next_two, callback=self.detail_page, validate_cert=False)

    @config(priority=2)
    def detail_page2(self, response):
        with open(('E:/图片/{}'.format(response.url[-10:])), 'wb') as f:
            f.write(response.content)
        return 'OK'