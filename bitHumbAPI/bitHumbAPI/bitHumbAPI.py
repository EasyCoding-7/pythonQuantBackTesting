
import pybithumb
import time

con_key = "86168bd96316eb6f3edc603f5e3fae56"
sec_key = "be2b81d44557f027aa361364c0e01e42"

bithumb = pybithumb.Bithumb(con_key, sec_key)

for ticker in pybithumb.get_tickers() :
    balance = bithumb.get_balance(ticker)
    print(ticker, " ", balance)
    time.sleep(0.1)