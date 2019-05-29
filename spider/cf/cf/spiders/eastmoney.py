# -*- coding: utf-8 -*-
import scrapy
import requests
import json

def create_file(filename, md):
    return open(filename, mode=md)


def close_file(fo):
    fo.close()


def write_file(fo, str_list):
    fo.write(str_list)

class EastmoneySpider(scrapy.Spider):
    name = 'eastmoney'
    allowed_domains = ['eastmoney.com']
    start_urls = ['http://data.eastmoney.com/zlsj/sb.html']

    def parse(self, response):
        first_url ='http://data.eastmoney.com/zlsj/zlsj_list.aspx?type=ajax&st=2&sr=-1&p={page_index}&ps=50&jsObj=ZMSSMKIi&stat=3&cmd=1&date=2019-03-31&rt=51967171' 
        fo = create_file('fh.txt','w')
        for index in range(1,12):
            next_url=first_url.replace('{page_index}', str(index))
            r = requests.get(next_url)
            data=r.text.split("=",1)[1]
            json_data=json.loads("["+data.split("[")[1].split("]")[0]+"]")
            for dt in json_data:
                print(dt['SCode'])
                second_url = 'http://dcfm.eastmoney.com/EM_MutiSvcExpandInterface/api/js/get?type=DCSOBS&token=70f12f2f4f091e459a279469fe49eca5&p=1&ps=50&sr=-1&st=ReportingPeriod&filter=&cmd={SCode}&js=var%20DbrlQBnc={pages:(tp),data:(x)}&rt=51968139'
                nx_url = second_url.replace('{SCode}',str(dt['SCode']))
                fh = requests.get(nx_url)
                fh_data = fh.text.split("=",1)[1]
                fh_json = json.loads("["+fh_data.split("[")[1].split("]")[0]+"]")
                print(fh_json)
                write_file(fo,str("["+fh_data.split("[")[1].split("]")[0]+"]\n"))
        close_file(fo)        
    def parse_detail(self, response):
        print(response.xpath('//h1[@class="main-title"]/text()').extract())
