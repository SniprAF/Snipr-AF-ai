import requests

# دریافت داده‌های جدیدترین توکن‌ها در شبکه سولانا از DEX Screener
def get_latest_tokens():
    url = "https://api.dexscreener.com/latest/dex/pairs/solana"
    response = requests.get(url)
    return response.json().get("pairs", [])

# تابع فیلتر: فقط توکن‌هایی که LP قفل شده و mint/freeze غیرقابل تغییر هستند
def filter_safe_tokens(tokens):
    safe = []
    for token in tokens:
        try:
            info = token.get("info", {})
            if (
                info.get("lpLocked", False) and
                info.get("ownerRenounced", False) and
                not info.get("canMint", True) and
                not info.get("canFreeze", True)
            ):
                safe.append({
                    "name": token["baseToken"]["name"],
                    "symbol": token["baseToken"]["symbol"],
                    "price": token["priceUsd"],
                    "url": f'https://dexscreener.com/solana/{token["pairAddress"]}'
                })
        except Exception as e:
            print(f"خطا در بررسی توکن: {e}")
    return safe

if __name__ == "__main__":
    print("در حال بررسی توکن‌های جدید...")
    tokens = get_latest_tokens()
    filtered = filter_safe_tokens(tokens)

    if filtered:
        print(f"\n✅ {len(filtered)} توکن امن پیدا شد:\n")
        for t in filtered:
            print(f"{t['name']} ({t['symbol']}) - ${t['price']} | 🔗 {t['url']}")
    else:
        print("\n⛔ توکن امنی پیدا نشد. صبر کن و دوباره تلاش کن.")

