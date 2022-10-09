import numpy as np
import yfinance as yf
from datetime import datetime
from dateutil.relativedelta import relativedelta

from Math.LogReturns import get_log_returns 

def get_statistics(backtest_results, benchmark_data, slice_length):
    """
    Returns Strategy Statistics
    - Max Drawdown 
    - Sharpe Ratio
    - Calmar Ratio
    
    """

    max_drawdown = get_max_drawdown(backtest_results, benchmark_data[slice_length:])
    sharpe_ratio = get_sharpe_ratio(backtest_results, benchmark_data[slice_length:])
    calmar_ratio = get_calmar_ratio(max_drawdown, backtest_results, benchmark_data[slice_length:])

    return 0 

def get_max_drawdown(backtest_results, benchmark_data):
    """
    Computes Max Drawdown
    """

    data = []

    for i in range(len(backtest_results)):

        data.append

    return data

def get_sharpe_ratio(backtest_results, benchmark_data):
    """
    Computes 30 Day Rolling Sharpe Ratio
    """

    data = []

    for i in range(len(backtest_results)):

        data.append

    return data

def get_calmar_ratio(max_drawdown, backtest_results, benchmark_data):
    """
    Computes 30 Day Rolling Calmar Ratio
    """

    data = []

    for i in range(len(backtest_results)):

        data.append

    return data





    