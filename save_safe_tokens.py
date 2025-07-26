import asyncio
import aiohttp
import json
import os

COINGECKO_LIST_URL = "https://api.coingecko.com/api/v3/coins/list"
COINGECKO_COIN_URL = "https://api.coingecko.com/api/v3/coins/{}"
SAFE_TOKENS_FILE = "safe_tokens.json"
MAX_TOKENS = 30  # فقط 30 توکن اول بررسی می‌شود برای تست سریع

async def fetch_coin_detail(session, coin_id):
    try:
        async with session.get(COINGECKO_COIN_URL.format(coin_id)) as response:
            if response.status == 200:
                data = await response.json()
                platforms = data.get("platforms", {})
                if "solana" in platforms and platforms["solana"]:
                    print(f"✅ توکن امن سولانا: {coin_id}")
                    return {
                        "id": data["id"],
                        "symbol": data["symbol"],
                        "name": data["name"],
                        "platform": "solana",
                        "address": platforms["solana"]
                    }
            else:
                print(f"⚠️ خطا در دریافت {coin_id}: {response.status}")
    except Exception as e:
        print(f"⚠️ خطا در پردازش {coin_id}: {e}")
    return None

async def get_safe_solana_tokens():
    print("در حال گرفتن توکن‌های سولانا از کوین‌گکو...")

    async with aiohttp.ClientSession() as session:
        async with session.get(COINGECKO_LIST_URL) as response:
            if response.status != 200:
                print(f"❌ خطا در گرفتن لیست کوین‌ها: {response.status}")
                return []
            coins = await response.json()

        tasks = []
        for coin in coins[:MAX_TOKENS]:
            tasks.append(fetch_coin_detail(session, coin["id"]))

        results = await asyncio.gather(*tasks)
        return [token for token in results if token is not None]

def save_safe_tokens(tokens):
    with open(SAFE_TOKENS_FILE, "w", encoding="utf-8") as f:
        json.dump(tokens, f, ensure_ascii=False, indent=2)
    print(f"✅ تعداد توکن‌های امن ذخیره‌شده: {len(tokens)}")

if __name__ == "__main__":
    safe_tokens = asyncio.run(get_safe_solana_tokens())
    save_safe_tokens(safe_tokens)
