import requests

url = "https://api.dexscreener.com/dex/pairs/solana"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    # گرفتن 10 توکن اول در لیست
    pairs = data.get("pairs", [])
    if not pairs:
        print("لیستی از توکن‌ها دریافت نشد.")
    else:
        for i, token in enumerate(pairs[:10]):
            base = token.get("baseToken", {})
            name = base.get("name", "Unknown")
            symbol = base.get("symbol", "N/A")
            price = token.get("priceUsd", "N/A")
            print(f"{i+1}. {name} ({symbol}) - Price: {price}")

except requests.RequestException as e:
    print("خطا در دریافت داده‌ها:", e)
except ValueError:
    print("خطا در تبدیل JSON")
