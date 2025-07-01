# 📤 Finance Forecast Dispatcher

Simple automation tool for sending a financial report (`report.pdf`) to **Telegram** and **Discord** using Python.

> ✅ Perfect for portfolio, alert systems, or lightweight reporting pipelines.

---

## 📌 Project Overview

This repository demonstrates how to automatically deliver a pre-generated PDF file to:

- 📲 **Telegram** using a bot
- 💬 **Discord** using a webhook

The process is minimalistic, portable, and fully customizable.

---

## 📁 Repository Contents

| File | Description |
|------|-------------|
| `config.json`         | API keys and credentials for Telegram and Discord |
| `send_report_bot.py`  | Sends the PDF report to Telegram |
| `discord_report.py`   | Sends the PDF report to Discord |
| `report.pdf`          | Sample financial report (sent by scripts) |
| `expenses.py`         | (Optional) Script to generate sample expenses |
| `forecast_expenses.py`| (Optional) Simple forecasting module |
| `README.md`           | Project documentation |

---

## ⚙️ Configuration

Update `config.json` with your bot credentials and webhook:

```json
{
  "telegram": {
    "bot_token": "YOUR_TELEGRAM_BOT_TOKEN",
    "chat_id": "YOUR_CHAT_ID"
  },
  "discord": {
    "webhook_url": "YOUR_DISCORD_WEBHOOK_URL"
  }
}
```
📌 report.pdf must exist in the root directory. You can generate it yourself or reuse the one provided.


## 🖼 Report Preview
Here's what the generated PDF report looks like:
![image](https://github.com/user-attachments/assets/fc68085b-0179-4129-a1ed-7a63df0afdcd)

## 🧩 Extra Modules
These scripts are not required for dispatching but can be used for additional automation or as mock data generators:

expenses.py — generate sample financial transactions

forecast_expenses.py — apply simple forecasting logic

## 🔧 Stack
Python 3.x

Telegram Bot API

Discord Webhook API

requests for HTTP communication

## ✨ Use Cases
📬 Scheduled report delivery

⚠️ Alert notifications

📊 Business process automation

🎓 Educational / demo project

## 📎 Author
Created by @KalinNika
💡 For learning, automation, and portfolio.

