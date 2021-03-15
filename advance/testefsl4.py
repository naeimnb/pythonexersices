import requests

r = requests.get('https://api.coinpaprika.com/v1/global')
myJason=r.json()

market_cap_usd=myJason['market_cap_usd']
print('market_cap_usd:',market_cap_usd)

volume_24h_usd=myJason['volume_24h_usd']
print('volume_24h_usd:',volume_24h_usd)

bitcoin_dominance_percentage=myJason['bitcoin_dominance_percentage']
print('bitcoin_dominance_percentage:',bitcoin_dominance_percentage)

market_cap_ath_value=myJason['market_cap_ath_value']
print('market_cap_ath_value:',market_cap_ath_value)

market_cap_ath_date=myJason['market_cap_ath_date']
print('market_cap_ath_date:',market_cap_ath_date)

volume_24h_ath_value=myJason['volume_24h_ath_value']
print('volume_24h_ath_value:',volume_24h_ath_value)

volume_24h_percent_from_ath=myJason['volume_24h_percent_from_ath']
print('volume_24h_percent_from_ath:',volume_24h_percent_from_ath)

volume_24h_percent_to_ath=myJason['volume_24h_percent_to_ath']
print('volume_24h_percent_to_ath:',volume_24h_percent_to_ath)

market_cap_change_24h=myJason['market_cap_change_24h']
print('market_cap_change_24h:',market_cap_change_24h)

volume_24h_change_24h=myJason['volume_24h_change_24h']
print('volume_24h_change_24h:',volume_24h_change_24h)

last_updated=myJason['last_updated']
print('last_updated:',last_updated)
