import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Backtesting.Backtest import get_backtest

from Data.YFinance import fetch_benchmark_data, fetch_yfinance_data
from MachineLearning.KMeans import get_clusters
from Math.LogReturns import get_log_returns 
from MachineLearning.PCA import get_pca

def main():
    """
    This is the main method. This wraps all the code into one neat program. 
    """

    # Fetch Tickers
    ticker_symbols = get_ticker_symbols()
    # print(ticker_symbols)

    # Fetch Benchmark Data
    benchmark_data = fetch_benchmark_data
    print(benchmark_data.head())

    # Fetch Historical Data
    historical_data = fetch_yfinance_data(ticker_symbols)
    print(historical_data[0].head())

    # Compute Log Returns
    benchmark_returns = get_log_returns(benchmark_data)
    log_returns = get_log_returns(historical_data)
    # print(log_returns[0].open)

    # Create Pandas DataFrame
    df = pd.DataFrame(log_returns[0].close, columns = [ticker_symbols[0]])
    # print(df.head())

    # Append to DataFrame
    for i in range(1, len(ticker_symbols)):
        # print(ticker_symbols[i][0], ": ", len(log_returns[i].close))
        df.insert(i, ticker_symbols[i][0], log_returns[i].close)    
    # print(df.head())

    # Generate Backtest
    slice_length = 180
    backtest_results = get_backtest(ticker_symbols, historical_data, log_returns, slice_length)

    plt.plot(backtest_results)
    plt.xlabel("Time")
    plt.ylabel("Portfolio Value")
    plt.title("Statistical Arbitrage Portfolio")
    plt.show()

    # Correlation Matrix
    corr_matrix = df.corr()

    # K Means Clustering
    clusters = get_clusters(corr_matrix)
    print("Clusters: ", clusters.cluster_centers_)
    print("Labels: ", clusters.labels_)

    # Principal Component Analysis
    pca = get_pca(corr_matrix)
    print("Correlation Principal Components: ", pca.components_)
    print("Correlation Singular Values: ", pca.singular_values_)
    print("Correlation Mean: ", pca.mean_)
    print("Correlation Explained Variance: ", pca.explained_variance_)

    # sorted = np.sort(pca.components_[0])
    # indexes = np.argsort(pca.components_[0])

    # print(sorted)
    # print(indexes)

    # for i in range(len(indexes)):
        # print(ticker_symbols[indexes[i]][0], ": ", sorted[i])

    # plt.hist(corr_matrix.iloc[:, 0])
    # plt.title("Correlation Distribution")

    # plt.matshow(corr_matrix)
    # plt.xticks(np.arange(3), ['Tom', 'Dick', 'Sue']) 
    # plt.yticks(np.arange(3), ['Tom', 'Dick', 'Sue']) 
    # cb = plt.colorbar()
    # cb.ax.tick_params(labelsize=14)
    # plt.title('Correlation Matrix', fontsize=16)
    # plt.show()

    return 0

def get_ticker_symbols():
    """
    Read Tickers Symbols CSV and convert to Numpy Array
    """

    df = pd.read_csv('TestSymbols.csv')
    ticker_array = df.to_numpy()

    return ticker_array

if __name__ == '__main__':

    main()

