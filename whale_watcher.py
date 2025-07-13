import requests
import time

def get_latest_sol_trades(limit=20):
    url = f"https://public-api.birdeye.so/public/transaction/solana?limit={limit}"
    headers = {
        "accept": "application/json",
        "x-chain": "solana"
    }
    try:
        response = requests.get(url, headers=headers)
        return response.json().get("data", [])
    except Exception as e:
        print(f"خطا در دریافت تراکنش‌ها: {e}")
        return []

def filter_large_buys(trades, min_amount_usd=5000):
    whale_trades = []
    for tx in trades:
        if tx.get("txType") == "BUY" and tx.get("valueInUsd", 0) >= min_amount_usd:
            whale_trades.append({
                "symbol": tx.get("symbol", "Unknown"),
                "amount": tx["valueInUsd"],
                "address": tx["buyerAddress"],
                "time": tx["blockTime"],
                "txHash": tx["txHash"],
            })
    return whale_trades

if __name__ == "__main__":
    print("در حال بررسی تراکنش‌های بزرگ نهنگ‌ها 🐳...")
    trades = get_latest_sol_trades()
    whales = filter_large_buys(trades)

    if whales:
        print(f"\n✅ {len(whales)} تراکنش بزرگ (نهنگ) پیدا شد:\n")
        for w in whales:
            print(f"{w['symbol']} | ${w['amount']} | 👤 {w['address']} | 🔗 https://solscan.io/tx/{w['txHash']}")
    else:
        print("⛔ فعلاً تراکنش بزرگی دیده نشد.")
