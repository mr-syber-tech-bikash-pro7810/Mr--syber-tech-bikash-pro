#!/usr/bin/env python3
"""SmishGuard - offline fraud/phishing SMS risk checker (text analysis only)."""
import re

KEYWORDS = {
    "refund": 3, "claim": 3, "click": 2, "urgent": 2,
    "kyc": 3, "blocked": 3, "suspended": 3, "prize": 3,
    "winner": 3, "otp": 2, "verify": 2, "expire": 2,
    "lottery": 3, "free": 1, "congratulations": 2,
}
SHORTENERS = ["bit.ly", "tinyurl.com", "t.co", "goo.gl",
              "cutt.ly", "is.gd", "rb.gy", "shorturl.at"]
RISKY_TLDS = [".xyz", ".top", ".click", ".info", ".live", ".icu"]


def analyze(sms):
    score, reasons = 0, []
    text = sms.lower()

    for word, pts in KEYWORDS.items():
        if word in text:
            score += pts
            reasons.append(f"Suspicious keyword: '{word}' (+{pts})")

    urls = re.findall(r"(?:https?://)?[\w.-]+\.[a-z]{2,}(?:/\S*)?", text)
    urls = [u for u in urls if "." in u and not u.replace(".", "").isdigit()]

    for u in urls:
        if any(s in u for s in SHORTENERS):
            score += 5
            reasons.append(f"Shortened link: {u} (+5)")
        if any(u.split("/")[0].endswith(t) for t in RISKY_TLDS):
            score += 3
            reasons.append(f"Risky domain: {u} (+3)")
        if re.search(r"\d+\.\d+\.\d+\.\d+", u):
            score += 5
            reasons.append("IP address in link (+5)")

    if re.search(r"(rs\.?|₹|inr)\s?[\d,]+", text):
        score += 2
        reasons.append("Money amount mentioned (+2)")
    if "click to" in text or "tap to" in text:
        score += 2
        reasons.append("Urgency to click link (+2)")

    level = "HIGH RISK" if score >= 8 else "MEDIUM" if score >= 4 else "LOW"
    return score, level, reasons


if __name__ == "__main__":
    print("Paste the SMS text and press Enter:")
    sms = input("> ")
    score, level, reasons = analyze(sms)
    print(f"\nScore: {score} | Result: {level}")
    for r in reasons:
        print(" -", r)
    print("\nWarning: never click suspicious links.")
