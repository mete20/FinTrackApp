from alpha_vantage.timeseries import TimeSeries 
from alpha_vantage.techindicators import TechIndicators 
from matplotlib.pyplot import figure 
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv
# Your key here
load_dotenv()
key = os.getenv('API_KEY')
# Chose your output format, or default to JSON (python dict)
ts = TimeSeries (key, output_format='pandas')
ti = TechIndicators (key)
# Get the data, returns a tuple
# aapl data is a pandas dataframe, aapl meta_data is a dict
aapl_data, aapl_meta_data = ts.get_daily (symbol= 'IBM')
# aant_sma is a dict, aapt meta sma also a dict
aapl_sma, aap_meta_sma = ti.get_sma(symbol='IBM')
# Visualization
figure(num=None, figsize=(15, 6), dpi=80, facecolor='w', edgecolor='k')
aapl_data['4. close'].plot()
plt.tight_layout()
plt.grid()
plt.show()