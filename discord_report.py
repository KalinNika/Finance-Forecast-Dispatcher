import os
import json
import requests


with open("config.json", "r", encoding="utf-8") as f:
    cfg = json.load(f)

WEBHOOK_URL = cfg["discord"]["webhook_url"]
REPORT_PDF  = "report.pdf"

if not os.path.exists(REPORT_PDF):
    raise FileNotFoundError(f"Файл не найден: {REPORT_PDF}")

with open(REPORT_PDF, "rb") as f:
    resp = requests.post(
        WEBHOOK_URL,
        data={"content": "📈 Вот ваш финансовый отчёт:"},
        files={"file": (os.path.basename(REPORT_PDF), f, "application/pdf")}
    )

if resp.status_code == 204:
    print("✅ Отчёт отправлен в Discord!")
else:
    print("❌ Ошибка Discord:", resp.status_code, resp.text)
