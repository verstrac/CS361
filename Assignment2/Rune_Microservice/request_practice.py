# Caleb Verstraete
# trying requests to see what happens
import requests

r = requests.get('https://secure.runescape.com/m=itemdb_rs/Spirit+shards/viewitem?obj=12183')
print(r.text)
