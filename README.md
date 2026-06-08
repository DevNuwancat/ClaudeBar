# Claude Cap 

![Claude Cap](https://i.imgur.com/Q98YYJR.png)

> Know your cap before you hit it.

A free, open source macOS menu bar app that shows your **Claude.ai usage in real time** — right where you need it.

![Claude Cap Menu Bar](https://i.imgur.com/so7IVq9.png)

---

## What it shows

```
Claude Pro
──────────────────────────
5hr   ▰▰▰▰▱▱▱▱▱▱▱▱  41%
Week  ▰▰▰▱▱▱▱▱▱▱▱▱  24%
──────────────────────────
↳ 5hr resets in     1h 17m
↳ Week resets in    3d 1h 7m
↳ Week date         Fri 1:30 AM
──────────────────────────
Last Updated        12:22 AM
⟳ Refresh Now
──────────────────────────
Set Session Token...
GitHub • nuwancat
♡ Buy me a coffee • $1
──────────────────────────
Quit
```

- **5hr session usage** — with progress bar
- **Weekly limit usage** — with progress bar + reset date
- **Auto refreshes** every 2 minutes
- **Secure** — your token stored in macOS Keychain

---

## Install

### Option 1 — DMG (Recommended)
1. Download `ClaudeCap-v1.0.dmg` from [Releases](https://github.com/DevNuwancat/ClaudeCap/releases)
2. Open the DMG
3. Drag **Claude Cap** to Applications
4. Open it from Applications or Spotlight

### Option 2 — Run from source
```bash
git clone https://github.com/DevNuwancat/ClaudeCap.git
cd ClaudeCap
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

---

## Setup — Getting your Session Token

Claude Cap needs your Claude.ai session token to read your usage. Here's how to get it:

**Step 1** — Open [claude.ai](https://claude.ai) in Chrome or Safari

**Step 2** — Press `F12` to open DevTools

**Step 3** — Click the **Application** tab

![DevTools Application Tab](https://i.imgur.com/we9sGwU.png)

**Step 4** — In the left sidebar, click **Cookies** → `https://claude.ai`

![Cookies Section](https://i.imgur.com/DMgYXic.png)

**Step 5** — Find `sessionKey` in the list and copy its full value

![sessionKey Cookie](https://i.imgur.com/4lQAv6Y.png)

**Step 6** — Click the Claude Cap icon in your menu bar → **Set Session Token** → paste it → **Save**

✅ Done! Claude Cap will now show your real usage data.

---

## Token Expiry

Your session token expires every **~7 days** when Claude.ai refreshes it.

When it expires:
- Claude Cap shows `⚠️` in the menu bar
- Click **Set Session Token** and paste a fresh one
- Takes 30 seconds

---

## How it works

```
sessionKey (macOS Keychain)
        ↓
GET claude.ai/api/organizations → your org ID
        ↓
GET claude.ai/api/organizations/{id}/usage
        ↓
{
  "five_hour": { "utilization": 41.0, "resets_at": "..." },
  "seven_day": { "utilization": 24.0, "resets_at": "..." }
}
        ↓
Displayed in your menu bar ✅
```

- No third party servers
- No data collection
- All requests go directly to claude.ai
- Token stored encrypted in macOS Keychain

---

## Requirements

- macOS 11+
- Python 3.9+ (only if running from source)
- A Claude.ai Pro, Max, or Team account

---

## Project Structure

```
ClaudeCap/
├── app.py          # menu bar UI (rumps)
├── api.py          # fetches usage from claude.ai
├── keychain.py     # secure token storage
├── requirements.txt
├── setup.py        # py2app build config
└── assets/
    └── claudecap.png
```

---

## Built with

- [`rumps`](https://github.com/jaredks/rumps) — macOS menu bar framework
- [`curl_cffi`](https://github.com/yifeikong/curl_cffi) — Chrome TLS impersonation (bypasses Cloudflare)
- [`keyring`](https://github.com/jaraco/keyring) — macOS Keychain storage

---

## Disclaimer

Claude Cap reads data from Claude.ai's internal API endpoints which are not officially public. This is an independent open source project, not affiliated with Anthropic. Use at your own discretion.

---

## Contributing

PRs welcome! Ideas for v2:

- [ ] Notifications when session hits 80%
- [ ] Auto launch on login
- [ ] Support for multiple accounts
- [ ] Windows/Linux support via `pystray`
- [ ] Homebrew Cask formula

---

## Support

If Claude Cap saved you from hitting your limits — [ko-fi.com/nuwancat](https://ko-fi.com/nuwancat) $1 goes a long way!

---

Made with by [nuwancat](https://github.com/DevNuwancat)

[![Ko-fi](https://img.shields.io/badge/Ko--fi-Support-orange)](https://ko-fi.com/nuwancat)
[![GitHub](https://img.shields.io/badge/GitHub-DevNuwancat-black)](https://github.com/DevNuwancat)
[![License](https://img.shields.io/badge/License-MIT-blue)](LICENSE)
