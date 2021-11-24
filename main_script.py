import get_from_api

# tikers = [i.upper() for i in input('Enter tikers you want, enter separated by a space').split()]
#
# prices_now = get_from_api.get_price(tikers)
#
# prices_hist = {}
# for tiker in tikers:
#     prices_hist[tiker] = get_from_api.get_price_by_years(tiker)

prices_now = [('IBM', '116.7900', '2021-11-23')]
prices_hist = {'IBM': [('2021-11-23', '116.7900'), ('2020-11-30', '123.5200'), ('2019-11-29', '134.4500'), ('2018-11-30', '124.2700'), ('2017-11-30', '153.9700'), ('2016-11-30', '162.2200'), ('2015-11-30', '139.4200'), ('2014-11-28', '162.1700'), ('2013-11-29', '179.6800'), ('2012-11-30', '190.0700'), ('2011-11-30', '188.0000'), ('2010-11-30', '141.4600'), ('2009-11-30', '126.3500'), ('2008-11-28', '81.6000'), ('2007-11-30', '105.1800'), ('2006-11-30', '91.9200'), ('2005-11-30', '88.9000'), ('2004-11-30', '94.2400'), ('2003-11-28', '90.5400'), ('2002-11-29', '86.9200'), ('2001-11-30', '115.5900'), ('2000-11-30', '93.5000')]}

profit = {}
for tiker in prices_hist:
    ln = len(prices_hist[tiker])
    tkprof = []
    npr = prices_hist[tiker][::-1]
    for date in npr:
        if npr.index(date) < ln - 1:
            dpr = float(npr[npr.index(date) + 1][1]) - float(date[1])
            tkprof += [dpr / float(date[1])]
        else:
            break
    midprof = list(map(lambda x: x * 100 + 1, tkprof))
    a = 1
    for i in range(len(midprof)):
        a *= midprof[i]
    a = a ** (1 / len(midprof))
    profit[tiker] = [a - 1]

print(profit)