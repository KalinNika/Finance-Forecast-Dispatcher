# 📤 Finance Forecast Dispatcher

Simple automation tool for sending a financial report (`report.pdf`) to **Telegram** and **Discord** using Python.

> ✅ Perfect for portfolio, alert systems, or lightweight reporting pipelines.

---

## 📌 Project Overview

This repository demonstrates how to automatically deliver a pre-generated PDF file to:

- 📲 **Telegram** using a bot
- 💬 **Discord** using a webhook

The process is based on minimal configuration and fully customizable.

---

## 🗂️ Repository Structure

📁 finance-forecast-dispatcher/
├── config.json # API credentials for Telegram and Discord
├── discord_report.py # Sends report.pdf to Discord via webhook
├── expenses.py # (Optional) Generates sample expense data
├── forecast_expenses.py # (Optional) Forecasts future expenses
├── report.pdf # The PDF file to be sent
├── send_report_bot.py # Sends report.pdf to Telegram via Bot API
└── README.md # Project documentation

---

## ⚙️ Configuration

Before running the scripts, make sure to update your `config.json`:

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

