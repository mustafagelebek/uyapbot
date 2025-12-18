UYAP System Status Monitor Bot
This bot automatically monitors the accessibility of the UYAP Lawyer Portal (Beta) and sends a notification via X (Twitter) if a downtime is detected.

🚀 Features
Automated Monitoring: Powered by GitHub Actions to run every 15 minutes.

Twitter Integration: Automatically posts a tweet when the system is down or returns an error code (404, 500, etc.).

24/7 Availability: Runs on GitHub servers even when your computer is turned off.

🛠️ Setup and Requirements
1. GitHub Secrets Configuration
To run this bot securely, you must add the following keys to your repository under Settings > Secrets and variables > Actions:

API_KEY: Your X Developer API Key

API_SECRET: Your X Developer API Secret

ACCESS_TOKEN: Your X Access Token

ACCESS_TOKEN_SECRET: Your X Access Token Secret

2. Local Installation
If you want to test the bot on your local machine:

Bash

pip install -r requirements.txt
python twitter.py
