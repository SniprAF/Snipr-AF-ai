import requests

url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "category": "solana-ecosystem",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1,
    "sparkline": "false"
}

try:
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    for i, token in enumerate(data, 1):
        name = token.get("name", "Unknown")
        symbol = token.get("symbol", "").upper()
        price = token.get("current_price", "N/A")
        print(f"{i}. {name} ({symbol}) - Price: ${price}")

except requests.RequestException as e:
    print("خطا در دریافت داده‌ها:", e)
