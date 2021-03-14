# import scrapy
# import json

# pages = int((input('how many page crawl: ')))

# class ExampleSpider(scrapy.Spider):
#     name = 'example'

#     start_urls = ['https://mywork.com.vn/tuyen-dung/63/tu-van-cham-soc-khach-hang.html/trang/{}?categories=63'.format(i+1) for i in range(pages)]

#     def parse(self, response):
#         data = {}
#         works = response.css('div.box-body')
#         for work in works:
#             for a in work.css('div.row'):
#                 # data['Position'] = i.css('a::attr(title)').getall()
#                 data['Position'] = str(a.css('p.j_title.text_ellipsis strong::text').getall()).replace("['","").replace("']","")
#                 data['Company'] = str(a.css('div.j_company.text_ellipsis span::text').getall()).replace("['","").replace("']","")
#                 data['Salary'] = str(a.css('div.col-sm-5 span.dollar::text').getall()).replace("\\xa0","").replace("['","").replace("']","")
#                 data['Location'] = str(a.css('div.col-sm-5 span.location.ml-20::text').getall()).replace("\\n          ","").replace("\\xa0","").replace("['","").replace("']","")

#                 if not data['Position']=="[]":
#                     # f = open('filename.txt', 'a')
#                     # f.write("{},{},{},{}".format(data['Position'],data['Company'] ,data['Salary'], data['Location']))
#                     # f.close()
#                     yield data


#         # f = open('filename.txt', 'a')
#         # f.write("{},{},{},{}".format(data['Position'],data['Company'] ,data['Salary'], data['Location']))
#         # f.close()
