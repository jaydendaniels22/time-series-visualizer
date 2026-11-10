import pandas as pd
import numpy as np

np.random.seed(42)

dates = pd.date_range(start='2016-05-09', end='2019-12-03', freq='D')
n = len(dates)

trend = np.linspace(20000, 150000, n)

t = np.arange(n)
seasonality = 15000 * np.sin(2 * np.pi * t / 365.25 - 1.5)

noise = np.random.normal(0, 5000, n)

views = trend + seasonality + noise
views = np.maximum(views, 1000)

df = pd.DataFrame({'date': dates, 'value': views.astype(int)})
df['date'] = df['date'].dt.strftime('%Y-%m-%d')

df.to_csv('fcc-forum-pageviews.csv', index=False)
print("Successfully created fcc-forum-pageviews.csv")