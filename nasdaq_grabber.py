import bs4 as bs
import pickle
import requests
import datetime as dt 
import os
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web

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
	with open("sp500tickers.pickle","wb") as f:
		pickle.dump(tickers,f)
	# print(tickers)
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
	for ticker in tickers:
		try:
			print(ticker)
			if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
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


get_data_from_yahoo(True)