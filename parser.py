import re
import csv
import requests
from bs4 import BeautifulSoup



def get_html(url):

	r = requests.get(url)
	return r.text

def get_total_pages(html):

	soup = BeautifulSoup(html, 'lxml')
	pages = soup.find('div', class_='pagination')
	all_links = pages.find_all('a')[-2]
	get_href = all_links.get('href')
	total_pages = get_href.split('/')[-2]
	return int (total_pages)
	

def get_page(html):
	soup = BeautifulSoup(html, 'lxml')
	base_url_pd = "http://www.avery-zweckform.ru/product/"
	products = soup.find('div', id='productlist').find_all('h2')
	
	for product in products:
		articul = str(product).split('"')[3]
		pages = base_url_pd + articul
		get_page_data (pages)

def get_page_data(pages)
	

	reg = re.compile('[^a-zA-Zа-яА-Я.,!?  ]')
	#reg = re.compile('[-\w]+')

	soup = BeautifulSoup (pages, lxml)

	descriptions = soup.find('div', id='product')

		for description in descriptions:
			try:
				name = description.find ('div', class_='c75r').find('h1').text
			except:
				name = ""

			try:
				code = description.find ('span', class_='productcode').find('strong').text
			except:
				code = ""

			try:
				SWcode = description.find ('span', class_='softwarecode').find('strong').text
			except:
				SWcode = ""

			try:
				desc1_row = description.find ('div', class_='c66l').find('p').text.strip()
				desc1 = reg.sub('', desc1_row)
			except:
				desc1 = ""

			try:
				desc2 = description.find ('div', id='fandb').find('ul').find_all('li')
				#desc2_row = description.find ('div', id='fandb').find('ul').find_all('li')
				#desc2 = reg.sub('', desc2_row)
			except:
				desc2 = ""

			try:
				char = description.find ('div', id='fandb').find('ul').find_all('li')
			except:
				char = ""

def main():
	url = "http://www.avery-zweckform.ru/products/labels/multipurpose/page/1/"
	base_url = "http://www.avery-zweckform.ru/"
	page_part = "/products/labels/multipurpose/page/"


	total_pages = get_total_pages(get_html(url))

	for i in range (1, total_pages+1):
		url_gen = base_url + page_part + str(i)
		html = get_html(url_gen)
		get_page(html)
		



if __name__ == '__main__': 
	main()