import yfinance as yf
from datetime import datetime
from dateutil.relativedelta import relativedelta

def fetch_yfinance_data(ticker_symbols):
    """
    Returns Historical Price Data from Yahoo Finance 

    Input: 
    - List of Ticker Symbols

    Output: 
    - Historical Price Data

    """

    current_date = datetime.today()
    past_date = current_date - relativedelta(months = 60)

    current_date = current_date.strftime('%Y-%m-%d')
    past_date = past_date.strftime('%Y-%m-%d')

    data = []

    for ticker in ticker_symbols:
        stock = yf.Ticker(ticker[0])   
        data.append(stock.history(start = past_date, end = current_date))

    return data