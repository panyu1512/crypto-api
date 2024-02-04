import json
import pandas as pd

from utils import obtain_crypto_abbreviation

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
        

    def _abbreviate_crypto_names(self, df):
        df['Name'] = df['Name'].apply(lambda x: obtain_crypto_abbreviation(x))
        return df


    def _get_dataframe_from_url(self, url):
        try:
            df = pd.read_html(url)[0]
            return df
        except Exception as e:
            print(f"Error scraping data from {url}: {e}")
            return pd.DataFrame()

    
    def get_top_10_crypto_by_market_cap(self) -> json:
        """
        Get the top 10 cryptocurrencies by market cap
        returns: json
        """

        df = self._get_dataframe_from_url(self.baseurl)
        
        if not df.empty:
            df = self._abbreviate_crypto_names(df)
            return df[['Name', 'Price', '1h %', '24h %', '7d %', 'Market Cap', 'Volume(24h)']].head(10).to_json(orient='records')

        return json.dumps([])
    
    def get_top_10_exchanges(self) -> json:
        """
        Get the top 10 exchanges by volume
        returns: json
        """

        df = self._get_dataframe_from_url(self.baseurl + "rankings/exchanges/")

        if not df.empty:
            return df[['Exchange', 'Score', 'Trading volume(24h)', 'Avg. Liquidity', 'Weekly Visits', '# Markets', '# Coins', 'Fiat Supported']].head(10).to_json(orient='records')
        
        return json.dumps([])
    
    def get_top_10_descentralized_exchanges(self) -> json:
        """
        Get the top 10 decentralized exchanges by volume
        returns: json
        """

        df = self._get_dataframe_from_url(self.baseurl + "rankings/exchanges/dex/")

        if not df.empty:
            return df[['Name', 'Trading volume(24h)', '% Mkt Share', 'No. Markets', 'Type', 'Launched']].head(10).to_json(orient='records')
        
        return json.dumps([])
    
    def get_nft_top_10_collections(self) -> json:
        """
        Get the NFT top 10 collections
        returns: json
        """

        df = self._get_dataframe_from_url(self.baseurl + "nft/collections/")

        if not df.empty:
            return df[['Name', 'Chain', 'Volume (24h)', 'Floor Price', 'Avg. Price (24h)']].head(10).to_json(orient='records')
        
        return json.dumps([])
    
    
    def get_top_10_trending_coins(self) -> json:
        """
        Get the top 10 trending coins
        returns: json
        """
        
        df = self._get_dataframe_from_url(self.baseurl + "trending-cryptocurrencies/")

        if not df.empty:
            df = self._abbreviate_crypto_names(df)
            return df[['Name', 'Price', '24h', '7d', '30d','Market Cap', 'Volume(24h)']].head(10).to_json(orient='records')
        
        return json.dumps([])


    def get_top_10_gainers(self) -> json:
        """
        Get the top 10 gainers
        returns: json
        """

        df = self._get_dataframe_from_url(self.baseurl + "gainers-losers/")

        if not df.empty:
            df = self._abbreviate_crypto_names(df)
            return df[['Name', 'Price', '24h', 'Volume(24h)']].head(10).to_json(orient='records')
        
        return json.dumps([])
        