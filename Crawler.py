#It is the module which is used to send HTTP request and can recieve data in different formates like encoding ,objects etc.
import requests
#Beautiful Soup is a Python library for getting data out of HTML, XML, and other markup languages
from bs4 import BeautifulSoup 

def crawler(max_page):
    page = 1
    while page <= max_page :
        url = "https://www.timeout.com/newyork/movies/best-movies-of-all-time" 
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text , features="lxml")
        for link in soup.findAll('a' , {'class': 'xs-text-charcoal decoration-none'}):
            href = 'https://www.timeout.com/newyork' + str(link.get('href'))
            title = link.string
            print(title)
            print(href)
        page += 1
crawler(1)

# this is a web crawler , which can collect data for you and in this programm it will collect links and names of top hundred movies from internet.
#special thanks to thenewboston .