# 🛡️ SmishGuard

**A lightweight Termux/Python tool that checks suspicious SMS messages and rates their phishing risk.**

SmishGuard analyzes SMS text (keywords, shortened links, risky domains, money lures, urgency) and gives a risk score: LOW, MEDIUM or HIGH. It never opens links, so it is safe to use.

## Features
- Keyword-based scam scoring (refund, KYC, OTP, prize, etc.)
- Detects shortened links (bit.ly, tinyurl, etc.) and risky TLDs
- Flags IP-address links, money lures and "click to claim" urgency
- Works fully offline, no API keys needed

## Installation (Termux)

```bash
pkg update && pkg upgrade -y
pkg install python git -y
git clone https://github.com/<your-username>/SmishGuard.git
cd SmishGuard
pip install -r requirements.txt
```

## Usage

```bash
python smishguard.py
```

Paste the SMS text when prompted. Example:

```
> Notification: CMAFoundation EXAMRESULT completed successfully. Rs.45,664 tuition fee refunded. Click to claim: bit.ly/4AMC5Jh

Score: 19 | Result: HIGH RISK
```

## Optional: scan inbox automatically

```bash
pkg install termux-api -y
termux-sms-list -l 5
```

(Install the **Termux:API** app too and grant SMS permission.)

## If you receive a scam SMS
- Do not click the link or reply
- Report spam in your messaging app
- India: call **1930** or report at [cybercrime.gov.in](https://cybercrime.gov.in)
- If you shared bank details, contact your bank immediately

## Roadmap
- Redirect-chain check for short links
- Domain age (WHOIS) check
- VirusTotal / Google Safe Browsing integration
- Auto-scan inbox via termux-api

## Disclaimer
SmishGuard is a heuristic tool for education and personal protection. It can produce false positives and negatives. Always verify with the official sender.

## License
MIT License. See [LICENSE](LICENSE).
