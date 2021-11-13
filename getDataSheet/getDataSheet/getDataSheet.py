import requests
import pandas as pd
from pykrx import stock
import time
import datetime

#종목, PER 가져오기
def getTickerPER(date):
    tickers = stock.get_market_ticker_list(date, market='ALL')

    corp=[]

    for ticker in tickers:
        corp_name = stock.get_market_ticker_name(ticker)
        corp.append([ticker, corp_name])

    df = pd.DataFrame(data=corp, columns=['종목코드', '종목명'])
    df = df.set_index('종목코드')

    df_f = stock.get_market_fundamental_by_ticker(date, market='ALL')

    df = pd.merge(df, df_f, left_index=True, right_index=True)

    return df

def main():
    checkDateTime = datetime.date(2021,11,11)
    df = getTickerPER(checkDateTime.strftime("%Y%m%d"))
    df.to_csv('./outPut.csv', sep=',', na_rep="NaN", encoding='utf-8-sig')

if __name__ == "__main__":
    main()