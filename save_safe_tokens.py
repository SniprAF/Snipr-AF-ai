import asyncio
import aiohttp
import json
from datetime import datetime

COINGECKO_URL = "https://api.coingecko.com/api/v3/coins/{}"
TOKEN_LIST = [
    "solana",               # توکن سولانا رسمی
    "serum",                # SRM توکن Serum
    "usd-coin",             # USDC
    "tether",               # USDT
    "raydium",              # RAY
    "mango-markets",        # MNGO
    "step-finance",         # STEP
    "oxygen",               # OXY
    "star-atlas",           # ATLAS
]

async def fetch_token_data(session, token_id):
    url = COINGECKO_URL.format(token_id)
    try:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                market_cap = data.get("market_data", {}).get("market_cap", {}).get("usd", 0)
                if market_cap and market_cap > 100000:
                    print(f"✅ توکن امن سولانا: {token_id} (Market Cap: ${market_cap:,})")
                    return token_id
                else:
                    print(f"⚠️ توکن {token_id} بازار کافی ندارد (Market Cap: ${market_cap:,})")
            else:
                print(f"⚠️ خطا در دریافت {token_id}: وضعیت {response.status}")
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
            await asyncio.sleep(1.2)  # جلوگیری از محدودیت نرخ درخواست (429)
    
    # ذخیره توکن‌های امن در فایل JSON
    with open("safe_tokens.json", "w", encoding="utf-8") as f:
        json.dump(safe_tokens, f, indent=4, ensure_ascii=False)
    
    # ذخیره تاریخ و زمان آخرین به‌روزرسانی
    last_update = {"last_updated": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")}
    with open("last_update.json", "w", encoding="utf-8") as f:
        json.dump(last_update, f, indent=4, ensure_ascii=False)
    
    print(f"✅ تعداد توکن‌های امن ذخیره‌شده: {len(safe_tokens)}")
    print(f"🕒 آخرین به‌روزرسانی: {last_update['last_updated']} (UTC)")

if __name__ == "__main__":
    asyncio.run(main())
