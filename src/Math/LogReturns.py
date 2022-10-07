import numpy as np
from numba import jit 

class LogReturns: 
    """
    Log Returns of OHLC
    """

    def __init__(self, open, high, low, close):
        self.open = open
        self.high = high
        self.low = low 
        self.close = close

# @jit(nopython = True)
def get_log_returns(historical_data):
    """
    Computes the Log Returns for OHLC Price Data

    Input: 
    - A List of OHLC Data

    Output: 
    - A List of OHLC Log Returns
    """

    returns = []

    for data in historical_data:

        open = []
        for i in range(len(data['Open']) - 1):
            open.append(np.log(data['Open'][i+1] / data['Open'][i]) * 100)

        high = []
        for i in range(len(data['High']) - 1):
            high.append(np.log(data['High'][i+1] / data['High'][i]) * 100)

        low = []
        for i in range(len(data['Low']) - 1):
            low.append(np.log(data['Low'][i+1] / data['Low'][i]) * 100)

        close = []
        for i in range(len(data['Close']) - 1):
            close.append(np.log(data['Close'][i+1] / data['Close'][i]) * 100)

        obj = LogReturns(open, high, low, close)
        returns.append(obj)

    return returns