from bs4 import BeautifulSoup
import requests


def scrape_stock_data(symbol, exchange):
    if exchange == 'NASDAQ':
        url = f"https://finance.yahoo.com/quote/{symbol}"
    elif exchange == 'NSE':
        symbol = symbol+'.NS'
        url = f'https://finance.yahoo.com/quote/{symbol}?p={symbol}&.tsrc=fin-srch'

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            current_price = soup.find("fin-streamer",{"class":"livePrice yf-mgkamr"})["data-value"]
            price_changed = soup.find(f"fin-streamer", {"class":"priceChange yf-mgkamr"}).span.text
            percentage_changed = soup.find("fin-streamer", {"data-field": "regularMarketChangePercent"}).span.text
            previous_close = soup.find("fin-streamer", {"data-field": "regularMarketPreviousClose"}).text
            week_52_range = soup.find('fin-streamer', {'data-field': 'fiftyTwoWeekRange'}).text
            week_52_low, week_52_high = week_52_range.split(' - ')
            market_cap = soup.find('fin-streamer', {'data-field': 'marketCap'}).text
            pe_ratio = soup.find('fin-streamer', {'data-field': 'trailingPE'}).text
            dividend_yield = soup.find(lambda tag: tag.name == 'li' and tag.find('span', text='Forward Dividend & Yield')).find('span', {'class': 'value yf-tx3nkj'}).get_text()


            stock_response = {
                'current_price': current_price,
                'previous_close': previous_close,
                'price_changed': price_changed,
                'percentage_changed': percentage_changed,
                'week_52_low': week_52_low,
                'week_52_high': week_52_high,
                'market_cap': market_cap,
                'pe_ratio': pe_ratio,
                'dividend_yield': dividend_yield,
            }
            return stock_response
        
    except Exception as e:
        # print(f'Error scraping the data: {e}')
        return None