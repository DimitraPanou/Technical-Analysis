import time, requests, json
import datetime as dt
import pandas as pd
import sys
import time

print("Welcome to the CoinMarketCap Explorer!")

def writeCoin(data):
	for i in range(len(data['data'])):
		dataframe = {
		'Coin': [],
		'Cur. Rank': [],
		'Date': [],
		'Price': [],
		'Market Cap': []
		}
		dataframe['Coin'].append(data['data'][i]['slug'])
		dataframe['Cur. Rank'].append(data['data'][i]['cmc_rank'])
		dataframe['Date'].append(data['data'][i]['last_updated'])
		dataframe['Price'].append(data['data'][i]['quote']['USD']['price'])
		dataframe['Market Cap'].append(data['data'][i]['quote']['USD']['market_cap'])
		coin_data = pd.DataFrame(dataframe)
		write_df_to_csv(coin_data, 'results2/' + data['data'][i]['slug'] + '.csv')
	
def write_df_to_csv(i_df, i_file):
	try:
		i_df.to_csv(i_file)
	except IOError as e:
		print(e)
		sys.exit(13)
		
while True:
	# base URLs
	url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
	headers = {'Accept': 'application/json',
	'Accept-Encoding': 'deflate, gzip',
	'X-CMC_PRO_API_KEY': '98f46f7f-36c7-4a33-8c84-2fbb8430406e',
	}
	r = requests.get(url, headers=headers)
	if r.status_code == 200:
		data = json.loads(r.text)
		
	writeCoin(data);
	time.sleep(5*60);
