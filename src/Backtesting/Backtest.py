import numpy as np
import pandas as pd

from MachineLearning.PCA import get_pca

def get_backtest(ticker_symbols, historical_data, log_returns):
    """
    - Computes Backtest PnL for Long Short Portfolio 
    - Slices Log Returns and Rebalances, 180 Days
    - Computes Correlation Matrix
    - Get Principal Components

    Input: 
    - Historical Data
    - Log Returns

    Output: 
    - PnL, List
    """

    # Slice DataFrame
    N = 180

    # Initialize Portfolio
    capital = 100000
    pnl = [capital]

    # Begin Backtest
    for i in range(len(historical_data[0]['Open']) - N):

        # Create Pandas DataFrame
        df = pd.DataFrame(log_returns[0].close[i:i+N], columns = [ticker_symbols[0]])

        # Append to DataFrame
        for i in range(1, len(ticker_symbols)):
            df.insert(i, ticker_symbols[i][0], log_returns[i].close[i:i+N])   

        # Compute Correlation Matrix
        corr_matrix = df.corr()
        pca = get_pca(corr_matrix)

        # Sort Results
        sorted = np.sort(pca.components_[0])
        indexes = np.argsort(pca.components_[0])

        # Go Long and Short Pairs
        for i in range(0, len(sorted) / 2, 2):

            # Grab Price Data
            stock1_previous = historical_data[indexes[i]]['Close'][i+N]
            stock2_previous = historical_data[indexes[i+1]]['Close'][i+N]
            stock1 = historical_data[indexes[i]]['Close'][i+N]
            stock2 = historical_data[indexes[i+1]]['Close'][i+N]

            # Compute Ratio
            if stock1 < stock2: 
                ratio = int(stock2 / stock1)
                trade = (stock1 - stock1_previous) + (stock2_previous - stock2) * ratio
                pnl.append(trade)
            else: 
                ratio = int(stock1 / stock2)
                trade = (stock1- stock1_previous) * ratio + (stock2_previous - stock2)
                pnl.append(trade)

    return pnl