import requests
import json

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

    tokens_info = []

    for i, token in enumerate(data, 1):
        name = token.get("name", "Unknown")
        symbol = token.get("symbol", "").upper()
        price = token.get("current_price", "N/A")
        market_cap = token.get("market_cap", "N/A")
        volume = token.get("total_volume", "N/A")
        change_24h = token.get("price_change_percentage_24h", "N/A")

        print(f"{i}. {name} ({symbol}) - Price: ${price}, Market Cap: ${market_cap}, 24h Change: {change_24h}%")

        tokens_info.append({
            "rank": i,
            "name": name,
            "symbol": symbol,
            "price": price,
            "market_cap": market_cap,
            "volume_24h": volume,
            "change_24h_percent": change_24h
        })

    # ذخیره در فایل JSON
    with open("solana_top_tokens.json", "w", encoding="utf-8") as f:
        json.dump(tokens_info, f, ensure_ascii=False, indent=4)

    print("\n✅ اطلاعات توکن‌ها در فایل solana_top_tokens.json ذخیره شد.")

except requests.RequestException as e:
    print("خطا در دریافت داده‌ها:", e)
