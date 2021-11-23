import get_from_api

tikers = [i.upper() for i in input('Enter tikers you want, enter separated by a space').split()]

prices_now = get_from_api.get_price(tikers)

prices_hist = {}
for tiker in tikers:
    prices_hist[tiker] = get_from_api.get_price_by_years(tiker)

print(prices_now)
print(prices_hist)