'''
https://www.scrapethissite.com/pages/simple/
https://www.scrapethissite.com/pages/forms/
https://www.scrapethissite.com/pages/frames/

'''
import threading
import time
import requests
from bs4 import BeautifulSoup

url_list=[
    "https://www.scrapethissite.com/pages/simple/",
    "https://www.scrapethissite.com/pages/forms/",
    "https://www.scrapethissite.com/pages/frames/"
]

def fetch_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f'Fetched content length: {len(soup.text)}')

threads=[]

for url in url_list:
    thread=threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All the web pages fetched")