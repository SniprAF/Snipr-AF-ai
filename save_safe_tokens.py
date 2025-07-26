#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

from snipr_token_fetcher import get_latest_tokens
from snipr_filter import filter_safe_tokens


def save_to_json(tokens: List[Dict[str, Any]], filename: Path) -> None:
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "count": len(tokens),
        "tokens": tokens,
    }

    filename.parent.mkdir(parents=True, exist_ok=True)

    with filename.open("w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    print(f"💾 {len(tokens)} توکن امن در فایل «{filename}» ذخیره شد.")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="بررسی و ذخیره‌سازی توکن‌های امن (Safe Tokens) در شبکه سولانا."
    )
    parser.add_argument(
        "-o",
        "--output",
        default="data/safe_tokens.json",
        help="مسیر فایل خروجی (پیش‌فرض: data/safe_tokens.json)",
    )
    parser.add_argument(
        "--also-timestamped",
        action="store_true",
        help="همچنین نسخه‌ای زمان‌دار برای آرشیو ذخیره شود.",
    )
    args = parser.parse_args()

    print("⏳ دریافت توکن‌های جدید از شبکه سولانا...")
    tokens = get_latest_tokens()

    if not tokens:
        print("⛔ هیچ توکن جدیدی دریافت نشد.")
        return

    print(f"🔎 تعداد کل توکن‌ها: {len(tokens)} — در حال بررسی امنیت...")
    safe_tokens = filter_safe_tokens(tokens)

    if not safe_tokens:
        print("⚠️ هیچ توکن امنی شناسایی نشد.")
        return

    out_path = Path(args.output)
    save_to_json(safe_tokens, out_path)

    if args.also_timestamped:
        ts_name = f"safe_tokens_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}.json"
        ts_path = out_path.parent / ts_name
        save_to_json(safe_tokens, ts_path)


if __name__ == "__main__":
    main()
