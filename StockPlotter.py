import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd 
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web
import matplotlib.dates as mdates
from mpl_finance import candlestick_ohlc 

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
	df.set_index("Date", inplace=True)
	df.drop("Symbol", axis=1)

	df['100ma'] = df['Close'].rolling(window=100, min_periods=0).mean()
	ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
	ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)

	ax1.plot(df.index, df['Close'])
	ax1.plot(df.index, df['100ma'])
	#Plot bar graph with volume
	ax2.bar(df.index, df['Volume'])

	## Now plot everything
	# df['Close'].plot() #Plot closing prices
	# plt.plot(dates,closes)
	plt.show()

def candlestickPlot(ticker):

	start = dt.datetime(2013,1,1)
	end   = dt.datetime.now()


	df = web.DataReader(ticker,'morningstar',start, end)
	df.reset_index(inplace=True)
	
	# dates_1 = df_1['Date']
	df['mdate'] = [mdates.date2num(d) for d in df['Date']]

	ohlc = df[['mdate','Open','High','Low','Close']]
	ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
	ax2 = plt.subplot2grid((6,1), (5,0), rowspan=5, colspan=1, sharex=ax1)
	candlestick_ohlc(ax1, ohlc.values, width=0.05, colorup='g', colordown='r')
	ax2.bar(df['mdate'], df['Volume'])
	ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
	plt.xticks(rotation=60)
	plt.show()




if __name__ == "__main__":
# ticker= input("Enter ticker:")
	plotTicker('AAPL')
	# candlestickPlot('AAPL')