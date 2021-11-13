
import pandas_datareader as pdr 
import pandas as pd # from datetime 
import datetime, timedelta 
import matplotlib.pyplot as plt 
import seaborn as sns 

pd.options.display.float_format = '{:.2f}'.format 

start_day = datetime.date(2009,1,1) # 시작일 
end_day = datetime.date(2021,11,13) # 종료일 

# 공격자산 
SPY = pdr.get_data_yahoo('SPY', start_day - datetime.timedelta(days=365), end_day)['Adj Close'] 
VEA = pdr.get_data_yahoo('VEA', start_day - datetime.timedelta(days=365), end_day)['Adj Close'] 
EEM = pdr.get_data_yahoo('EEM', start_day - datetime.timedelta(days=365), end_day)['Adj Close'] 
AGG = pdr.get_data_yahoo('AGG', start_day - datetime.timedelta(days=365), end_day)['Adj Close'] 

# 수비자산 
LQD = pdr.get_data_yahoo('LQD', start_day - datetime.timedelta(days=365), end_day)['Adj Close'] 
SHY = pdr.get_data_yahoo('SHY', start_day - datetime.timedelta(days=365), end_day)['Adj Close'] 
IEF = pdr.get_data_yahoo('IEF', start_day - datetime.timedelta(days=365), end_day)['Adj Close']

df_VAA = pd.concat([SPY,VEA,EEM,AGG,LQD,SHY,IEF],axis=1) 
df_VAA.columns = ['SPY','VEA','EEM','AGG','LQD','SHY','IEF'] 
df_VAA.head(5)

print(df_VAA)