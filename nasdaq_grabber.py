import bs4 as bs
import pickle
import requests
import datetime as dt 
import os
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import numpy as np 

			# print('Already have {}'.format(ticker))

def save_sp500_tickers():
	resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies') #grab info from page
	soup = bs.BeautifulSoup(resp.text, 'lxml') #Save list for later use
	table = soup.find('table', {'class': 'wikitable sortable'})
	tickers = []
	for row in table.findAll('tr')[1:]:
		ticker = row.findAll('td')[0].text #for all table data, grab text
		ticker = ticker.replace('.','-').strip()
		tickers.append(ticker)


	tickers.remove('ANDV')
	tickers.remove('BKNG')
	tickers.remove('BF-B')
	tickers.remove('BHF')
	tickers.remove('DWDP')
	tickers.remove('CBRE')
	tickers.remove('DXC')
	tickers.remove('EVRG')
	tickers.remove('JEF')
	tickers.remove('TPR')
	tickers.remove('UAA')
	tickers.remove('WELL')
	tickers.remove('BRK-B')

	with open("sp500tickers.pickle","wb") as f:
		pickle.dump(tickers,f)
	# print(tickers)

	return tickers

def get_data_from_yahoo(reload_sp500=False):
	if reload_sp500:
		tickers = save_sp500_tickers()
	else:
		with open("sp500tickers.pickle", "rb") as f:
			tickers = pickle.load(f)
	if not os.path.exists('stock_dfs'):
		os.makedirs('stock_dfs')

	start = dt.datetime(2000, 1, 1)
	# end   = dt.datetime(2016, 1, 1)
	end   = dt.datetime.now()

	## Save all tickers to a .csv
	for ticker in tickers:
		try:
			# print(ticker)
			if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
				print(ticker)
				df = web.DataReader(str(ticker), 'morningstar', start, end)
				df.to_csv('stock_dfs/{}.csv'.format(ticker))
			 	# df.reset_index(inplace=True)
				# df.set_index("Date", inplace=True)
			 	# df = df.drop("Symbol", axis=1)
				# df.to_csv('stock_dfs/{}.csv'.format(ticker))
			else:
				print('Already have {}'.format(ticker))
		except:
			print('Cannot obtain data for ' + ticker)

def compile_data():
	with open("sp500tickers.pickle", "rb") as f:
		tickers = pickle.load(f)

	main_df = pd.DataFrame()
	# print(main_df)

	for count, ticker in enumerate(tickers):
		df = pd.read_csv('stock_dfs/{}.csv'.format(ticker))
		df.set_index('Date', inplace=True)

		df.rename(columns={'Close': ticker}, inplace=True)
		df.drop(['Open', 'High', 'Symbol', 'Low', 'Volume'], 1, inplace=True)

		if main_df.empty:
			main_df = df
		else:

			main_df = main_df.join(df, how='outer')

		if count % 10 == 0:
			print(count) #just see every 10 so we know its working


	print(main_df.head())
	main_df.to_csv('sp500_joined_closes.csv')

def visualize_data():
	df = pd.read_csv('sp500_joined_closes.csv')

	#create correlation table for all data
	df_corr = df.corr()

	# print(df_corr.head())
	data = df_corr.values # gets inner values, no ticker names
	fig = plt.figure()
	ax = fig.add_subplot(1,1,1)

	# Create heatmap with colrs from red to green
	heatmap = ax.pcolor(data, cmap = plt.cm.RdYlGn)
	fig.colorbar(heatmap)
	ax.set_xticks(np.arange(data.shape[0]) + 0.5, minor=False)
	ax.set_yticks(np.arange(data.shape[1]) + 0.5, minor=False)

	ax.invert_yaxis()
	ax.xaxis.tick_top() #moves ticks to top of heatmap

	column_labels = df_corr.columns 
	row_labels = df_corr.index 
	ax.set_xticklabels(column_labels)
	ax.set_yticklabels(row_labels)

	plt.xticks(rotation=90) #rotate ticks so we can easily read them
	heatmap.set_clim(-1,1) #limit colors

	plt.tight_layout()
	plt.show()


# save_sp500_tickers()
# get_data_from_yahoo(True)
# compile_data()
visualize_data()