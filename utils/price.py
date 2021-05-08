import pandas as pd

def prices_to_returns(prices):
    """ Convert price data into percentage return data.

    Each data entry is replaced by it's percentage change 
    vs. the entry before it.
    
    Parameters
    ----------
    sr : pd.Series
        Price data.

    Returns
    -------
    returns : pd.Series
        Percentage return data.
        
    Example
    -------
    >>> # Initialise a price series
    >>> prices = pd.Series([100, 101, 100, 125])
    >>> prices
    0    100
    1    101
    2    100
    3    125
    dtype: int64
    >>> # Convert Prices to Returns
    >>> prices_to_returns(prices)
    1    0.010000
    2   -0.009901
    3    0.250000
    dtype: float64
    """
    # Caluculate Returns
    previous_prices = prices.shift(1)
    returns = prices / previous_prices - 1
    
    # Remove First Period
    returns = returns.iloc[1:]  # The first entry has no prior day so return is NaN
        
    return returns


if __name__ == "__main__":
    import doctest
    doctest.testmod()