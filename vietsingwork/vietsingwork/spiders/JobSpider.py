import scrapy
import json

class JobSpider(scrapy.Spider):
    name ='vietsingwork'

    start_urls = ['http://vietsingworks.com/job']

    numOfJobs = 0
    def parse(self, response):
        links = response.css('div.caption h4 a::attr("href")').getall()
        for link in links:
            # self.numOfJobs += 1
            yield scrapy.Request(url = link, callback = self.get_job_info)

    
    def get_job_info(self, response):
        self.numOfJobs += 1
        yield {
            'job_title':  response.css('div.tentin h2::text').get(),
            'salary': response.css('div.cottrai p.mucluong::text')[1].get(),
            'location':  response.css('p.diadiem::text')[1].get(),
            'position': response.css('p.vitri::text')[1].get(),
            'job_type':  response.css('p.hinhthuc::text')[1].get(),
            'age': response.css('p.yeucautuoi::text')[1].get(),
            'quantity': response.css('p.soluong::text')[1].get(),
            'expired_day':response.css('p.hannop span::text').get(),
            'education_request': response.css('p.yeucaubc::text')[1].get(),
            'mandarin_level': response.css('p.nltieng::text')[1].get(),
            'english_level': response.css('p.nltieng::text')[3].get(),
            'agent_fee': response.css('div.cotphai p.mucluong::text')[1].get(),
            'job_description': response.css('div.motacv div.cotphai p::text').getall() \
                            + response.css('div.motacv div.cotphai ul li::text').getall() \
                            + response.css('div.motacv div.cotphai h3::text').getall()
        }