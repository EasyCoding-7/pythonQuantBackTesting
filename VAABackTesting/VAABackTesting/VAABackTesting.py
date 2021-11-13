
import pandas_datareader as pdr 
import pandas as pd
import datetime, timedelta 
import matplotlib.pyplot as plt 
import seaborn as sns 

# 모멘텀 지수 계산 함수 
def get_momentum(df_VAA, x): 
    momentum = pd.Series([0,0,0,0,0,0,0], index=['SPY','VEA','EEM','AGG','LQD','SHY','IEF']) 

    try: 
        # df_VAA[x.name-datetime.timedelta(days=35):x.name-datetime.timedelta(days=30)].iloc[-1] 하는 이유?
        # X달 전 데이터를 잘못 가져올 경우를 대비 5일치를 가져와서 마지막 행만 읽어준다
        before1 = df_VAA[x.name-datetime.timedelta(days=35):x.name-datetime.timedelta(days=30)].iloc[-1] 
        before3 = df_VAA[x.name-datetime.timedelta(days=95):x.name-datetime.timedelta(days=90)].iloc[-1] 
        before6 = df_VAA[x.name-datetime.timedelta(days=185):x.name-datetime.timedelta(days=180)].iloc[-1] 
        before12 = df_VAA[x.name-datetime.timedelta(days=370):x.name-datetime.timedelta(days=365)].iloc[-1] 
           
        momentum = 12 * (x / before1 - 1) + 4 * (x / before3 - 1) + 2 * (x / before6 - 1) + (x / before12 - 1) 
    except: 
        pass 
    
    return momentum

def main():
    pd.options.display.float_format = '{:.2f}'.format 

    start_day = datetime.date(2009,1,2) # 시작일 
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
    #df_VAA.head(5)

    # 각 자산별 모멘텀 지수 계산 
    df_VAA[['SPY_M','VEA_M','EEM_M','AGG_M','LQD_M','SHY_M','IEF_M']] = df_VAA.apply(lambda x: get_momentum(df_VAA, x), axis=1) 
    #df_VAA.tail(10)

    # 백테스트할 기간 데이터 추출 
    df_VAA = df_VAA[start_day:end_day] 
    
    # 매월 말일 데이터만 추출(리밸런싱에 사용) 
    df_VAA = df_VAA.resample(rule='M').apply(lambda x: x[-1]) 
    df_VAA.head(10)

    #print(df_VAA) # print to Console
    df_VAA.to_csv('./outPut.csv', sep=',', na_rep="NaN") # printf to File


if __name__ == "__main__":
    main()