import coinmarketcap_usd_history
import pandas as pd


df = coinmarketcap_usd_history.main(['airswap','2017-11-01','2018-01-10','--dataframe'])

# test it out
print df.head(10)

df.to_csv('output.csv', sep='\t', encoding='utf-8')
