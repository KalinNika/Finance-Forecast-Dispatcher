import pandas as pd
import numpy as np

np.random.seed(42)
dates = pd.date_range('2025-01-01', '2025-06-01')
amounts = np.random.normal(loc=200, scale=80, size=len(dates)).clip(50, 600)
categories = np.random.choice(['Food', 'Transport', 'Entertainment', 'Utilities'], size=len(dates))

df = pd.DataFrame({
    'date': dates,
    'amount': amounts,
    'category': categories
})

df['date'] = pd.to_datetime(df['date'])

spike_windows = {
    '2025-01-07': [900, 720, 760],  # Рождество
    '2025-02-14': [850, 700, 1010],  # День святого Валентина
    '2025-02-23': [1080, 540, 800],  # 23 февраля
    '2025-03-08': [1200, 780, 920],  # 8 марта
}

for date_str, values in spike_windows.items():
    base_date = pd.to_datetime(date_str)
    for i, val in enumerate(values):
        spike_day = base_date + pd.Timedelta(days=i)
        df.loc[df['date'] == spike_day, 'amount'] = val

df.to_csv('expenses.csv', index=False)
print("✅ Обновлённый 'expenses.csv' сохранён — с сильными тратами (включая праздники).")


