import requests
import json
import pandas as pd

class Scraper:
    """
    Scraper class to scrape data from coinmarketcap.com
    """
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        }
        self.baseurl = "https://www.coinmarketcap.com/"

    
    def get_top_10_crypto(self) -> json:
        """
        Get the top 10 cryptocurrencies by market cap
        returns: json
        """

        df = pd.read_html(self.baseurl)[0]

        return df[['Name', 'Price', '1h %', '24h %', '7d %', 'Market Cap', 'Volume(24h)']].head(10).to_json(orient='records')


Scraper = Scraper()
json = Scraper.get_top_10_crypto()

print(json)


        