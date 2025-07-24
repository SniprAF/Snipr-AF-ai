# Snipr-AF-ai

🚀 A powerful sniper bot for filtering, tracking, and auto-trading new tokens on the Solana blockchain.

---

## 🔍 Overview

**Snipr-AF-ai** is designed to help crypto traders identify promising new tokens on Solana using custom filters and automated safety checks.  
It automates token monitoring and enables semi or fully automatic trading based on secure conditions.

---

## ⚙️ Features

- 🔄 Real-time monitoring of new token pairs on Solana
- 🧠 Custom filters (liquidity, volume, holders, renounced, etc.)
- 🛡 Token safety checks using GoPlus, Gmgn, Photon, and others
- 💾 Auto-save safe tokens for review or auto-trade
- ⚡️ Fast, multi-threaded scanning
- 🤖 Optional auto-buy feature for quick execution
- 📊 Output to `safe_tokens.csv`

---

## 🧪 Token Safety Checks

Each token is scanned for:

- ✅ Verified source code  
- 🔒 Liquidity lock status  
- 🧾 Ownership renounced  
- ☑️ Whitelist/safety score (via GoPlus, GMGN, Photon APIs)  
- 📈 Trading volume, LP info, and holder count

---

## 💻 Usage

```bash
python snipr_token_fetcher.py
```

---

## 🛠 Installation

```bash
git clone https://github.com/username/Snipr-AF-ai.git
cd Snipr-AF-ai
pip install -r requirements.txt
```

---

## 🎛 Command-line Options

| Option              | Description                                        |
|---------------------|----------------------------------------------------|
| `--min-liquidity`   | Minimum token liquidity in USD                     |
| `--min-holders`     | Minimum number of holders                          |
| `--save`            | Save safe tokens to CSV                            |
| `--auto-buy`        | Enable auto-buy mode (use with caution!)           |
| `--interval`        | Time delay between scans in seconds                |

---

## 📁 Output

Safe tokens are saved in:

```text
safe_tokens.csv
```

Each entry includes:

- Token name  
- Token address  
- Liquidity  
- Renounce status  
- Holder count  
- Timestamp  

---

## 🤝 Contributing

Pull requests are welcome!  
Feel free to fork, open issues, or suggest improvements.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## ✨ Author

**Snipr AF.ai** by Mirwais Yarzadah  
_Powered by Python, Crypto & 💡Ideas_
