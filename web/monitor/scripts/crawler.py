from bs4 import BeautifulSoup
import requests
import re
from datetime import datetime, timedelta
from monitor.models import Monitor


def run():
  try: 
    response = requests.get("https://www.naver.com/")
    soup = BeautifulSoup(response.text, "html.parser")
    url = soup.select_one('#da_iframe_time').get('data-iframe-src')

    page_source = requests.get(url).text
    soup2 = BeautifulSoup(page_source, "html.parser")

    matched = re.search('var daHtml = (.+)>";', page_source, re.S)
    info_list = list(matched.group(0).split('"'))

    img_url = info_list[4]
    title = info_list[-7]
    landing_url = soup2.select_one('#addiv > a').get('href')

    total = img_url+ title + landing_url
    total_list = total.split("\\")

    img_url = total_list[0]
    title = total_list[1]
    landing_url = total_list[2]

    Monitor(img_url=img_url, title=title, landing_url=landing_url).save()
    
  except Exception as e:
    response = requests.get("https://www.naver.com/")
    soup = BeautifulSoup(response.text, "html.parser")
    url = soup.select_one('#da_iframe_time').get('data-iframe-src')

    page_source = requests.get(url).text
    soup2 = BeautifulSoup(page_source, "html.parser")
    matched = re.search('var info = (.+)",', page_source, re.S)
    info_list = list(matched.group(0).split('"'))

    img_url = info_list[-4]
    title = info_list[7]
    landing_url = info_list[9]

    Monitor(img_url=img_url, title=title, landing_url=landing_url).save()