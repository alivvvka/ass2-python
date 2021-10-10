import requests
from bs4 import BeautifulSoup

class CryptoScrapper:   

    def getTitles(self, cur, page):

        # in '&start = 0' you can change page of searching. '0' will show you 10 links from first page. '10' will show you 10 links from second page.
        r = requests.get('https://google.com/search?q=site%3Acoinmarketcap.com+' + cur + '&start=' + page) 

        soup = BeautifulSoup(r.content, 'html.parser')

        titles = soup.find_all('h3')

        for t in titles:
            print('\n Title name - ' + t.find("div").get_text())



scrapper = CryptoScrapper()

scrapper.getTitles('bitcoin', '0')
    

