import json
import requests
import time

# بارگذاری توکن‌ها از فایل تست
def fetch_mock_tokens():
    with open("sample_tokens.json", "r", encoding="utf-8") as f:
        tokens = json.load(f)
    print(f"📁 تعداد توکن‌های تستی بارگذاری‌شده: {len(tokens)}")
    return tokens

# بررسی امنیت توکن با GoPlus API
def check_token_security(token_address):
    url = f"https://api.gopluslabs.io/api/v1/token_security/1?contract_addresses={token_address}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['result'].get(token_address, {})
        else:
            return {}
    except Exception as e:
        print(f"⛔ خطا در اتصال به GoPlus: {e}")
        return {}

# فیلتر کردن توکن‌های امن
def apply_goplus_filter(tokens):
    final = []
    for token in tokens:
        base_token = token.get("baseToken", {})
        address = base_token.get("address")
        name = base_token.get("name")
        symbol = base_token.get("symbol")
        price = token.get("priceUsd")

        if not address:
            continue

        print(f"🔍 بررسی {name} ({symbol}) ...")
        info = check_token_security(address)
        time.sleep(0.5)  # جلوگیری از بلاک شدن API

        try:
            if (
                info.get("is_open_source") == "1" and
                info.get("is_proxy") == "0" and
                info.get("can_take_back_ownership") == "0" and
                info.get("is_mintable") == "0" and
                info.get("is_blacklisted") == "0" and
                info.get("is_honeypot") == "0"
            ):
                final.append({
                    "name": name,
                    "symbol": symbol,
                    "address": address,
                    "price": price,
                    "security": info
                })
        except Exception as e:
            print(f"⛔ خطا در پردازش فیلتر: {e}")
            continue

    print(f"\n🔐 تعداد توکن‌های امن: {len(final)}")
    return final

# ذخیره توکن‌ها در فایل JSON
def save_tokens(tokens, filename="secure_tokens_goplus.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(tokens, f, ensure_ascii=False, indent=2)
    print(f"✅ ذخیره شد در فایل: {filename}")

if __name__ == "__main__":
    tokens = fetch_mock_tokens()
    safe_tokens = apply_goplus_filter(tokens)
    save_tokens(safe_tokens)


