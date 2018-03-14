#-*- coding:utf-8 -*-
import scrapy
from mySpider.items import ItcastItem
#创建一个爬虫类
class ItcastSpider(scrapy.Spider):

    #爬虫名
    name = "itcast"

    #允许爬虫作用的范围

    allowd_domains = ["http://www.itcast.cn/"]

    #爬虫真实的url
    start_urls = ["http://www.itcast.cn/channel/teacher.shtml#"]





    def parse(self, response):


        teacher_list = response.xpath('//div[@class="li_txt"]')
        teacherItem = []

        for each in teacher_list:

            #extract()将取出来的结果转化成unicode字符串
            name = each.xpath('./h3/text()').extract()
            title = each.xpath('./h4/text()').extract()
            info = each.xpath('./p/text()').extract()


            #print(type[name])

            #print(len(name))

            # print(name[0])
            #
            # print(title[0])
            # print(info[0])

            item = ItcastItem()

            item['name'] = name[0]

            item['title'] = title[0]

            item['info'] = info[0]

            #teacherItem.append(item)

        #print(teacherItem)

        #return teacherItem
            #将获取的数据提交给pipeline
            yield item


        #
        # with open("teacher.html","w") as f:
        #
        #     f.write(str(response.body))



