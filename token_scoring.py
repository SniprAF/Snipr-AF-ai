import json

# مسیر فایل ورودی و خروجی
input_file = 'sample_tokens.json'
output_file = 'scored_tokens.json'

# تعریف تابع نمره‌دهی به هر توکن
def score_token(token):
    score = 0
    max_score = 100

    # معیارهای امنیتی
    if token.get('is_honeypot') is False:
        score += 15
    if token.get('lp_locked') is True:
        score += 15
    if token.get('owner_renounced') is True:
        score += 15

    # حجم معاملات
    volume = float(token.get('volume_usd', 0))
    if volume > 100000:
        score += 15
    elif volume > 10000:
        score += 10
    elif volume > 1000:
        score += 5

    # تعداد هولدر
    holders = int(token.get('holders', 0))
    if holders > 500:
        score += 10
    elif holders > 100:
        score += 5

    # عمر توکن (اگر داریم)
    age_minutes = int(token.get('age_minutes', 0))
    if age_minutes > 60:
        score += 10
    elif age_minutes > 15:
        score += 5

    # نمره نهایی محدود به 100
    return min(score, max_score)

# خواندن داده‌ها
with open(input_file, 'r', encoding='utf-8') as f:
    tokens = json.load(f)

# نمره‌دهی به توکن‌ها
scored_tokens = []
for token in tokens:
    token_score = score_token(token)
    token['score'] = token_score
    scored_tokens.append(token)

# ذخیره خروجی
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(scored_tokens, f, indent=2)

print(f"✅ {len(scored_tokens)} توکن نمره‌گذاری شد و ذخیره شد در {output_file}")
