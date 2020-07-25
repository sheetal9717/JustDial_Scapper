#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 12:31:04 2020

@author: sheetal
"""

from bs4 import BeautifulSoup
import json
import time
from selenium import webdriver
browser = webdriver.Chrome('/home/sheetal/Downloads/chromedriver_linux64/chromedriver')
dict_list = []
def get_soup(link):
    browser.get(link)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(25)
    html = browser.page_source
    soup = BeautifulSoup(html)
    services = soup.find_all('li', {'class': 'cntanr'})

    for service_html in services:
        dict_service = {}
        name = get_name(service_html)
        print(name);
        phone = get_phone_number(service_html)
        rating = get_rating(service_html)
        address = get_address(service_html)
        location = get_location(service_html)
        if name != None:
            dict_service['Name'] = name
        if rating != None:
            dict_service['Rating'] = rating
        if phone != None:
            dict_service['Phone'] = phone
        if address != None:
            dict_service['Address'] = address
        if location != None:
            dict_service['Address'] = location
        dict_list.append(dict_service)
    json_object = json.dumps(dict_list, indent = 4)
    with open("/home/sheetal/using_selenium/data.json", "w") as outfile: 
        outfile.write(json_object)
    

def innerHTML(element):
    return element.decode_contents(formatter="html")

def get_name(body):
	return body.find('span', {'class':'jcn'}).a.string

def which_digit(html):
    mappingDict={'icon-ji':9,
                'icon-dc':'+',
                'icon-fe':'(',
                'icon-hg':')',
                'icon-ba':'-',
                'icon-lk':8,
                'icon-nm':7,
                'icon-po':6,
                'icon-rq':5,
                'icon-ts':4,
                'icon-vu':3,
                'icon-wx':2,
                'icon-yz':1,
                'icon-acb':0,
                }
    return mappingDict.get(html,'')

def get_phone_number(body):
    i=0
    phoneNo = "No Number!"
    try:
            
        for item in body.find('p',{'class':'contact-info'}):
            i+=1
            if(i==2):
                phoneNo=''
                try:
                    for element in item.find_all(class_=True):
                        classes = []
                        classes.extend(element["class"])
                        phoneNo+=str((which_digit(classes[1])))
                except:
                    pass
    except:
        pass
    body = body['data-href']
    soup = BeautifulSoup(body, 'html.parser')
    for a in soup.find_all('a', {"id":"whatsapptriggeer"} ):
        # print (a)
        phoneNo = str(a['href'][-10:])


    return phoneNo


def get_rating(body):
	rating = 0.0
	text = body.find('span', {'class':'star_m'})
	if text is not None:
		for item in text:
			rating += float(item['class'][0][1:])/10

	return rating

def get_rating_count(body):
	text = body.find('span', {'class':'rt_count'}).string
	rating_count =''.join(i for i in text if i.isdigit())
	return rating_count

def get_address(body):
	return body.find('span', {'class':'mrehover'}).text.strip()

def get_location(body):
	text = body.find('a', {'class':'rsmap'})
	if text == None:
		return
	text_list = text['onclick'].split(",")
	
	latitutde = text_list[3].strip().replace("'", "")
	longitude = text_list[4].strip().replace("'", "")
	
	return latitutde + ", " + longitude

url="https://www.justdial.com/Delhi/House-On-Rent/nct-10192844"
soup = get_soup(url)




