import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd 
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web

style.use('ggplot')

# start = dt.datetime(2015,1,1)
# end = dt.datetime.now()


# # stocks = ['AAPL', 'MSFT','TSLA']

# # df = web.DataReader("AAPL",'morningstar',start,end)

# # df.reset_index(inplace=True)
# # df.set_index("Date", inplace=True)
# # df = df.drop("Symbol", axis=1)

# # print(df.head())

# # df.to_csv('TSLA.csv')
# # df = pd.read_csv('tsla.csv',parse_dates=True, index_col=0)
# # df['Close'].plot()
# # plt.show()

# def compare_tickers(
# 	tickers,
# 	 start =dt.datetime(2010,1,1),
# 	 end   = dt.datetime.now() ):
# 	if (len(tickers) < 2):
# 		print('Multiple tickers must be supplied!')
# 		return


def printTickerHead(ticker):


	start = dt.datetime(2010,1,1)
	end   = dt.datetime.now()

	# tickers = ['AAPL','MSFT']

	df = web.DataReader('AAPL','morningstar',start,end)
	df.reset_index(inplace=True)
	# print(df.head())
	df['Close'].plot() #Plot closing prices
	plt.show()

	

if __name__ == "__main__":
# ticker= input("Enter ticker:")
	printTickerHead('AAPL')