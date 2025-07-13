import json
from snipr_filter import get_latest_tokens, filter_safe_tokens

def save_to_json(tokens, filename="safe_tokens.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(tokens, f, ensure_ascii=False, indent=2)
    print(f"\n💾 توکن‌های امن ذخیره شدند در فایل: {filename}")

if __name__ == "__main__":
    print("در حال بررسی و ذخیره توکن‌های امن...")
    tokens = get_latest_tokens()
    safe_tokens = filter_safe_tokens(tokens)

    if safe_tokens:
        save_to_json(safe_tokens)
    else:
        print("⛔ هیچ توکن امنی برای ذخیره‌سازی پیدا نشد.")

