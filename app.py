from flask import Flask
from scraper.scraper import Scraper
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
scraper = Scraper()

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["2 per minute", "1 per second"],
    strategy="fixed-window"
)

@app.route("/api", methods=["GET"])
def info_endpoints():
    return {
        "crypto-ranking": "Get the top 10 cryptocurrencies by market cap",
        "exchange-ranking": "Get the top 10 exchanges by volume",
        "dex-ranking": "Get the top 10 decentralized exchanges by volume",
        "nft-collections": "Get the top 10 NFT collections",
        "trending-cryptos": "Get the top 10 trending cryptocurrencies",
        "gainers": "Get the top 10 gainers cryptocurrencies"
    }

@app.route("/api/crypto-ranking", methods=["GET"])
def get_ranking():
    return scraper.get_top_10_crypto_by_market_cap()

@app.route("/api/exchange-ranking", methods=["GET"])
def get_exchanges():
    return scraper.get_top_10_exchanges()

@app.route("/api/dex-ranking", methods=["GET"])
def get_dex():
    return scraper.get_top_10_descentralized_exchanges()

@app.route("/api/nft-collections", methods=["GET"])
def get_nft():
    return scraper.get_nft_top_10_collections()

@app.route("/api/trending-cryptos", methods=["GET"])
def get_trending():
    return scraper.get_top_10_trending_coins()

@app.route("/api/gainers", methods=["GET"])
def get_gainers():
    return scraper.get_top_10_gainers()

if __name__ == "__main__":
    app.run(debug=True)
