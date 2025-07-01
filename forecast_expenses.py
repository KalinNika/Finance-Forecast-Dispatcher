import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt
from fpdf import FPDF
from datetime import datetime

df = pd.read_csv('expenses.csv')
df['date'] = pd.to_datetime(df['date'])

df['holiday_spike'] = 0

spike_windows = [
    '2025-01-07',  # Рождество
    '2025-02-14',  # День святого Валентина
    '2025-02-23',  # День защитника Отечества
    '2025-03-08',  # 8 марта
]

for date_str in spike_windows:
    base_date = pd.to_datetime(date_str)
    for i in range(3):
        spike_day = base_date + pd.Timedelta(days=i)
        df.loc[df['date'] == spike_day, 'holiday_spike'] = 1

df_grouped = df[['date', 'amount', 'holiday_spike']].groupby('date').sum().reset_index()
df_grouped.columns = ['ds', 'y', 'holiday_spike']

model = Prophet()
model.add_regressor('holiday_spike')
model.fit(df_grouped)

future = model.make_future_dataframe(periods=30)
future = future.merge(df_grouped[['ds', 'holiday_spike']], on='ds', how='left')
future['holiday_spike'] = future['holiday_spike'].fillna(0)

forecast = model.predict(future)

fig = model.plot(forecast)
fig.savefig("forecast.png", transparent=False)

print("✅ Прогноз построен с учётом праздников. Сохранён как forecast.png")

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=16)
pdf.cell(200, 10, txt="Financial Forecast Report", ln=True, align='C')
pdf.ln(10)

from datetime import datetime
now = datetime.now().strftime("%Y-%m-%d %H:%M")
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt=f"Generated: {now}", ln=True, align='L')
pdf.ln(10)

pdf.image("forecast.png", x=10, w=190)

pdf.output("report.pdf")

print("✅ PDF-отчёт успешно сгенерирован: report.pdf")
