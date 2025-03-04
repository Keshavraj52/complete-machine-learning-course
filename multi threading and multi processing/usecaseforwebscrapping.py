# https://python.langchain.com/v0.2/docs/introduction/

# https://python.langchain.com/v0.2/docs/tutorials/

# https://python.langchain.com/v0.2/docs/concepts/


import threading
import requests  

from bs4 import BeautifulSoup

urls=[
'https://python.langchain.com/v0.2/docs/introduction/',
'https://python.langchain.com/v0.2/docs/tutorials/',
'https://python.langchain.com/v0.2/docs/concepts/' 
]


def fetch_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f'fetched {len(soup.text)} character from {url}')


threads=[]

for url in urls:
    thread=threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("all web pages fetched")