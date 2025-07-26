import asyncio
import aiohttp
import json

COINGECKO_URL = "https://api.coingecko.com/api/v3/coins/{}"
TOKEN_LIST = [
    "0xlsd", "0xgasless-2", "0xnumber", "1000btt", "0xsim-by-virtuals",
    "1000bonk", "0dog", "000-capital", "1000cat", "1000x-by-virtuals",
    "0-knowledge-network", "0xscans", "0x0-ai-ai-smart-contract", "0x",
    "1000rats", "0x678-landwolf-1933", "0xgen", "0x-leverage", "0xprivacy",
    "1000shib", "1000chems"
]

async def fetch_token_data(session, token_id):
    url = COINGECKO_URL.format(token_id)
    try:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                if data.get("market_data", {}).get("market_cap", {}).get("usd", 0) > 100000:
                    print(f"✅ توکن امن سولانا: {token_id}")
                    return token_id
            else:
                print(f"⚠️ خطا در دریافت {token_id}: {response.status}")
    except Exception as e:
        print(f"⚠️ خطای ناشناخته در {token_id}: {e}")
    return None

async def main():
    print("در حال گرفتن توکن‌های سولانا از کوین‌گکو...")
    safe_tokens = []
    async with aiohttp.ClientSession() as session:
        for token_id in TOKEN_LIST:
            result = await fetch_token_data(session, token_id)
            if result:
                safe_tokens.append(result)
            await asyncio.sleep(1.2)  # ← اضافه شدن delay برای جلوگیری از 429
    with open("safe_tokens.json", "w", encoding="utf-8") as f:
        json.dump(safe_tokens, f, indent=4, ensure_ascii=False)
    print(f"✅ تعداد توکن‌های امن ذخیره‌شده: {len(safe_tokens)}")

if __name__ == "__main__":
    asyncio.run(main())
