# coding:utf8
import requests
from Mysql import MySQL
from lxml import etree
import re

def start():
	url='http://bjgy.chinacourt.org/article/index/id/MzAwMjAwNjAwMyACAAA%3D.shtml'
	try:
		val=requests.get(url,timeout=30).text
	except Exception as e:
		print(e)
	htm=etree.HTML(val)
	hrefs=htm.xpath('//*[@class="left"]/a/@href')
	title=htm.xpath('//*[@class="left"]/a/text()')
	for x in range(len(hrefs)):
		href='http://bjgy.chinacourt.org'+hrefs[x]

		try:
			val=requests.get(href,timeout=30).text
		except Exception as e:
			print(e)
		htm=etree.HTML(val)
		value=htm.xpath('//*[@class="b_title"]/text()')[0]
		fytime=htm.xpath('//*[@class="sth_a"]/span[1]/text()')[0]
		fytime=fytime.split('：')[0]


		fyname=re.findall(r'，([\w\W]*?)法院',value)[0]+"法院"


		sql='instert into carsearch_fygg(date,title,value,courtname)values("%s","%s","%s","%s")'%(fytime,title[x],value,fyname)
		mysql=MySQL()
		if mysql.query(sql):
			print('ok!')
		



start()