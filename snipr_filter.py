import requests

def check_token_security(token_address):
    """
    بررسی امنیت یک توکن سولانا با استفاده از API GoPlusLabs.
    ورودی: آدرس قرارداد توکن سولانا (رشته)
    خروجی: دیکشنری داده امنیتی یا دیکشنری خالی اگر داده نبود یا خطا بود.
    """
    url = f"https://api.gopluslabs.io/api/v1/token_security/solana?contract_addresses={token_address}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            print(f"DEBUG - داده دریافتی از GoPlus برای {token_address}: {data}")
            if data and "result" in data and isinstance(data["result"], dict) and token_address in data["result"]:
                return data["result"][token_address]
            else:
                print(f"⚠️ داده‌ای برای آدرس {token_address} در پاسخ GoPlus یافت نشد یا نتیجه نامعتبر است.")
                return {}
        else:
            print(f"❌ خطا در دریافت داده از GoPlus: کد وضعیت {response.status_code}")
            return {}
    except Exception as e:
        print(f"❌ استثناء در ارتباط با GoPlus: {e}")
        return {}

def main():
    # لیست توکن‌های سولانا برای تست - می‌تونی این لیست رو گسترش بدی
    tokens_to_test = [
        "4k3Dyjzvzp8eM7zF3EWh2sSx7wH8dGeVPt2A58xdk6R9",  # مثال توکن SOL (رپد سولانا)
        # توکن‌های بیشتر اینجا اضافه کن
    ]

    for token in tokens_to_test:
        print(f"\n=== بررسی توکن: {token} ===")
        security_info = check_token_security(token)
        if security_info:
            print(f"✅ اطلاعات امنیتی توکن {token}: {security_info}")
        else:
            print(f"⚠️ اطلاعات امنیتی برای توکن {token} موجود نیست.")

if __name__ == "__main__":
    main()
