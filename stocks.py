from bs4 import BeautifulSoup
import requests




def scrape_stock_data(symbol, exchange):
    if exchange == 'NASDAQ':
        url = f"https://finance.yahoo.com/quote/{symbol}"
    elif exchange == 'NSE':
        symbol = symbol+'.NS'
        url = f'https://finance.yahoo.com/quote/{symbol}'

    #headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    print("URL>>>", url)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    current_price = soup.find("fin-streamer",{"class":"livePrice yf-mgkamr"})["data-value"]
    price_changed = soup.find("fin-streamer", {"class":"priceChange yf-mgkamr"}).span.text
    percentage_changed = soup.find("fin-streamer", {"data-field": "regularMarketChangePercent"}).span.text
    previous_close = soup.find("fin-streamer", {"data-field": "regularMarketPreviousClose"}).text
    week_52_range = soup.find('fin-streamer', {'data-field': 'fiftyTwoWeekRange'}).text
    market_cap = soup.find('fin-streamer', {'data-field': 'marketCap'}).text
    pe_ratio = soup.find('fin-streamer', {'data-field': 'trailingPE'}).text
    dividend_yield = soup.find(lambda tag: tag.name == 'li' and tag.find('span', text='Forward Dividend & Yield')).find('span', {'class': 'value yf-tx3nkj'}).get_text()
      # Output: 0.80 (0.48%)
    #previous_close = soup.find('td', {'data-test': 'PREV_CLOSE-value'}).text
    #week_52_range = soup.find('td', {'data-test': 'FIFTY_TWO_WK_RANGE-value'}).text
    #week_52_low, week_52_high = week_52_range.split(' - ')

    #print("Week 52 Low:", week_52_low)
    #print("Week 52 High:", week_52_high)
    print("current_price >>>" , current_price)
    print("price_changed >>>", price_changed)
    print("percentage_change >>>", percentage_changed)
    print("Previous_close >>>", previous_close)
    print("week_52_range >>>", week_52_range)
    print("market_cap >>>", market_cap)
    print("trailing_PE >>>",pe_ratio)
    print("dividend_yield >>>" , dividend_yield )

scrape_stock_data('TSLA', 'NASDAQ')