import requests


def get_price(symbols: list):
    """
    :param symbols: List of names of securities
    :return: List like [('name', price, 'latest trading day'), ('name2', price2, 'latest trading day2'), ...]
    """
    API = '82N6XECHCH9Z17R7'
    prices = []
    for symbol in symbols:
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API}'
        r = requests.get(url)
        json = r.json()
        data = json['Global Quote']
        if len(data) > 0:
            prices.append((data['01. symbol'], data['05. price'], data['07. latest trading day']))
    return prices


# print(get_price(['IBM', 'AAPL', 'DAX']))
