# 🤖 UYAP System Status Monitor Bot

[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-Automated-blue?logo=github-actions)](https://github.com/features/actions)
[![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Twitter](https://img.shields.io/badge/Twitter-Integration-1DA1F2?logo=twitter&logoColor=white)](https://twitter.com)

Automated bot that monitors **UYAP Lawyer Portal (Beta)** accessibility and sends X (Twitter) alerts when downtime is detected.

---

## ✨ Features

- 🔄 **Automated Monitoring** - Runs every 11 minutes via GitHub Actions
- 🐦 **Twitter/X Integration** - Auto-posts tweets on system errors
- ⚡ **Real-time Alerts** - Instant notifications for 404, 500, and connection errors
- 🌐 **24/7 Availability** - Runs on GitHub infrastructure
- 🔒 **Secure** - Uses GitHub Secrets for API credentials

## 🛠️ Tech Stack

Python 3.9+ • `requests` • `tweepy` • GitHub Actions

---

## � Quick Setup

### 1. Get Twitter API Credentials

Visit [Twitter Developer Portal](https://developer.twitter.com/en/portal/dashboard) and generate:
- API Key & Secret
- Access Token & Secret

### 2. Configure GitHub Secrets

Go to **Settings** → **Secrets and variables** → **Actions** and add:

| Secret Name | Value |
|------------|-------|
| `API_KEY` | Your Twitter API Key |
| `API_SECRET` | Your Twitter API Secret |
| `ACCESS_TOKEN` | Your Twitter Access Token |
| `ACCESS_TOKEN_SECRET` | Your Twitter Access Token Secret |

### 3. Enable GitHub Actions

Navigate to **Actions** tab and enable workflows. The bot will run automatically every 11 minutes.

---

## 💻 Local Testing

```bash
# Install dependencies
pip install requests tweepy

# Set environment variables
export API_KEY="your_api_key"
export API_SECRET="your_api_secret"
export ACCESS_TOKEN="your_access_token"
export ACCESS_TOKEN_SECRET="your_access_token_secret"

# Run single check
python twitter.py

# Run continuous monitor
python bot.py
```

---

## 📱 Alternative Trigger Methods

The bot can also be triggered manually via **Google Apps Script** for custom scheduling or integration with Google Sheets/Calendar.

---

## ⚙️ Configuration

**Change monitoring interval** - Edit `.github/workflows/run_bot.yml`:
```yaml
schedule:
  - cron: '*/11 * * * *'  # Every 11 minutes
```

**Change target URL** - Edit `twitter.py`:
```python
HEDEF_URL = "https://avukatbeta.uyap.gov.tr/"
```

---

## 🐛 Troubleshooting

**Bot not tweeting?**
- Check GitHub Actions logs under **Actions** tab
- Verify all 4 secrets are set correctly
- Ensure Twitter app has **Read and Write** permissions

**Workflow not running?**
- Enable GitHub Actions in repository settings
- Manually trigger: **Actions** → **UYAP Kontrol Botu** → **Run workflow**

---

## 🤝 Contributing

Contributions welcome! Fork the repo, create a feature branch, and submit a pull request.

**Ideas**: Discord/Telegram integration • Web dashboard • Email notifications • Multi-URL monitoring

---

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

---

<div align="center">

**Made with ❤️ for the Turkish legal community**

⭐ Star this repo if it helps you!

</div>
