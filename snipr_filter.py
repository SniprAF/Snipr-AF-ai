import requests

def get_latest_tokens():
    url = "https://api.dexscreener.com/latest/dex/pairs/solana"
    print(f"📡 ارسال درخواست به: {url}")

    try:
        response = requests.get(url, timeout=10)
        print(f"✅ وضعیت پاسخ: {response.status_code}")
        if response.status_code != 200:
            print(f"⚠️ خطا: پاسخ غیرمنتظره با کد {response.status_code}")
            return []

        text_preview = response.text[:500]
        print(f"📄 پاسخ خام (اول ۵۰۰ کاراکتر):\n{text_preview}")

        # سعی می‌کنیم پاسخ را JSON کنیم
        data = response.json()
        pairs = data.get("pairs", [])
        print(f"🔎 تعداد جفت‌های دریافت‌شده: {len(pairs)}")
        return pairs

    except requests.exceptions.Timeout:
        print("❌ خطا: زمان پاسخ API تمام شد (Timeout)")
        return []

    except requests.exceptions.RequestException as e:
        print(f"❌ خطای درخواست: {e}")
        return []

    except ValueError as e:
        # خطای JSONDecodeError هم اینجا پوشش داده می‌شود
        print(f"❌ خطا در تبدیل JSON: {e}")
        print(f"📄 پاسخ دریافت‌شده:\n{response.text}")
        return []

def filter_safe_tokens(tokens):
    """
    فیلتر ساده اولیه:  
    اینجا می‌تونی قواعد امنیتی اولیه رو اضافه کنی مثل:
    - داشتن liquidity
    - تعداد هولدر بیشتر از مثلا 50
    - نبودن در blacklist

    فعلا فقط توکن‌هایی که حداقل یک liquidity دارن برمی‌گردونیم
    """
    safe_tokens = []
    for token in tokens:
        liquidity = token.get("liquidity", 0)
        if liquidity and liquidity > 0:
            safe_tokens.append(token)
    print(f"✅ تعداد توکن‌های امن پس از فیلتر اولیه: {len(safe_tokens)}")
    return safe_tokens

