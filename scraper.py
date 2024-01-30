import requests
from bs4 import BeautifulSoup

def get_citations_needed_count(url):
    
    response = requests.get(url)

    html = response.content

    soup = BeautifulSoup(html, 'html.parser')

    a = soup.find_all("a")

    citations = 0

    for i in a:
        if i.text == 'citation needed':
            citations += 1
        
    return print(citations)

def get_citations_needed_report(url):
    
    response = requests.get(url)

    html = response.content

    soup = BeautifulSoup(html, 'html.parser')

    a = soup.find_all("a")

    p = ""

    for i in a:
        if i.text == 'citation needed':
            p += i.parent.parent.parent.text
            
    print(p)




get_citations_needed_count("https://en.wikipedia.org/wiki/History_of_the_United_States")
get_citations_needed_report("https://en.wikipedia.org/wiki/History_of_the_United_States")