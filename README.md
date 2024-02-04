# Flask Web Scraper API

This is a simple Flask application that uses a web scraper to retrieve information related to cryptocurrencies, exchanges, DEX, NFTs, trending cryptocurrencies, and gainers.

## Installation

1. Make sure you have Python and pipenv installed.
2. Install dependencies by running:

    ```bash
    pipenv install -r requirements.txt
    ```

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Access the following endpoints in your browser or through tools like curl or Postman:

    - `/crypto-ranking`: Get the top 10 cryptocurrencies by market cap.
    - `/exchange-ranking`: Get the top 10 exchanges.
    - `/dex-rankings`: Get the top 10 decentralized exchanges (DEX).
    - `/nft-collections`: Get the top 10 NFT collections.
    - `/trending-cryptos`: Get the top 10 trending cryptocurrencies.
    - `/gainers`: Get the top 10 gainers.