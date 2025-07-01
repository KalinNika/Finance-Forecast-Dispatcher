import os
import json
import requests

with open("config.json", "r", encoding="utf-8") as f:
    cfg = json.load(f)

TOKEN   = cfg["telegram"]["bot_token"]
CHAT_ID = cfg["telegram"]["chat_id"]
REPORT_PDF = "report.pdf"

def send_report():
    if not os.path.exists(REPORT_PDF):
        print(f"❌ Файл {REPORT_PDF} не найден.")
        return

    url = f"https://api.telegram.org/bot{TOKEN}/sendDocument"
    with open(REPORT_PDF, "rb") as pdf:
        files = {"document": pdf}
        data  = {"chat_id": CHAT_ID}
        resp  = requests.post(url, data=data, files=files)

    if resp.status_code == 200:
        print("✅ Отчёт успешно отправлен в Telegram.")
    else:
        print("❌ Ошибка при отправке:", resp.status_code, resp.text)

if __name__ == "__main__":
    send_report()
