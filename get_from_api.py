import requests

API = '82N6XECHCH9Z17R7'


def get_price(symbols: list):
    """
    :param symbols: List of names of securities
    :return: List like [('name', price, 'latest trading day'), ('name2', price2, 'latest trading day2'), ...]
    """
    prices = []
    for symbol in symbols:
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API}'
        r = requests.get(url)
        json = r.json()
        data = json['Global Quote']
        if len(data) > 0:
            prices.append((data['01. symbol'], data['05. price'], data['07. latest trading day']))
    return prices


print(get_price(['IBM', 'AAPL', 'DAX']))


def get_price_by_years(stock):
    """
    :param stock: name of securities
    :return: List like [(year, price), (year2, price2), ...]
    """
    res = []
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={stock}&outputsize=full&apikey={API}'
    r = requests.get(url)
    json = r.json()
    data = json['Monthly Time Series']
    keys = list(data.keys())
    for i in range(0, len(keys), 12):
        res.append((keys[i], data[keys[i]]['4. close']))
    return res


print(get_price_by_years('IBM'))
