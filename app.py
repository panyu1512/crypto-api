from flask import Flask
from scraper.scraper import Scraper

app = Flask(__name__)
scraper = Scraper()


@app.route("/crypto-ranking", methods=["GET"])
def get_ranking():
    return scraper.get_top_10_crypto_by_market_cap()

@app.route("/exchange-ranking", methods=["GET"])
def get_exchanges():
    return scraper.get_top_10_exchanges()

@app.route("/dex-ranking", methods=["GET"])
def get_dex():
    return scraper.get_top_10_descentralized_exchanges()

@app.route("/nft-collections", methods=["GET"])
def get_nft():
    return scraper.get_nft_top_10_collections()

@app.route("/trending-cryptos", methods=["GET"])
def get_trending():
    return scraper.get_top_10_trending_coins()

@app.route("/gainers", methods=["GET"])
def get_gainers():
    return scraper.get_top_10_gainers()

if __name__ == "__main__":
    app.run(debug=True)
