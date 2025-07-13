import requests

url = "https://api.dexscreener.com/latest/dex/pairs/solana"
response = requests.get(url)
data = response.json()

# گرفتن توکن‌های تازه لیست شده
for i, token in enumerate(data["pairs"][:10]):
    print(f"{i+1}. {token['baseToken']['name']} ({token['baseToken']['symbol']}) - Price: {token['priceUsd']}")


added initial token fetcher
