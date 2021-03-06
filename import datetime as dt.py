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


def plotTicker(ticker):


	start = dt.datetime(2010,1,1)
	end   = dt.datetime.now()

	# tickers = ['AAPL','MSFT']

	df = web.DataReader('AAPL','morningstar',start,end)
	df.reset_index(inplace=True)

	dates = df['Date']
	closes = df['Close']

	## Now plot everything
	# df['Close'].plot() #Plot closing prices
	plt.plot(dates,closes)
	plt.show()

def compareTickers(ticker1, ticker2):


	start = dt.datetime(2010,1,1)
	end   = dt.datetime.now()


	df_1 = web.DataReader(ticker1,'morningstar',start, end)
	df_2 = web.DataReader(ticker2,'morningstar',start, end)

	df_1.reset_index(inplace=True)
	df_2.reset_index(inplace=True)
	
	dates_1 = df_1['Date']
	dates_2 = df_2['Close']
	close_1 = df_1['Close']
	close_2 = df_2['Close']

	plt.plot(dates_1, close_1, 'b')
	# plt.plot(dates_2, close_2, 'g')
	# plt.plot(dates_2, close_2)

	plt.show()



if __name__ == "__main__":
# ticker= input("Enter ticker:")
	# plotTicker('AAPL')
	compareTickers('AAPL','MSFT')