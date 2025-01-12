# Python Mempool API

Welcome to the **Python Mempool API** documentation!  Here, we take a wild ride through the world of Bitcoin using the [mempool.space](https://mempool.space/) REST API.  
Buckle up, because we're about to fetch some serious data!

## Introduction

Ever wanted to know the price of Bitcoin in your favorite currency? Or maybe check the balance of your Bitcoin address?  
Well, you've come to the right place!  
This Python package is your trusty sidekick in the quest for Bitcoin knowledge.

## Classes

- **General**:
    - get the current difficulty adjustment
    - check live bitcoin price in various fiat currencies
    - retrieve historical bitcoin price in various fiat currencies in a specific timestamp
- **Addresses**:
    - see a specified address balance
    - check the validation status of a specified address
- **Blocks**:
    - check the last block height
    - retrieve a block header by specifying the blocks hash
- **Mining**:
    - get a list of active mining pools by specifying the time frame
- **Fees**:
    - check the current network fees in various formats
- **Mempool**:
    - get the current mempool backlog statistics
- **Lightning**:
    - check the lightning network statistics
    - get a list of nodes by specifying the desired country
    - retrieve a node statistics by specifying its public key

## Methods

- **General**:
    - `get_difficulty_adjustment()`, `get_btc_price(currency: str)`, `get_btc_historical_price(currency: str, timestamp: int)`

- **Addresses**:
    - `get_address_balance(address: str)`, `address_validation(address: str)`

- **Blocks**
    - `get_last_block_height()`, `get_block_header(block_hash: str)`

- **Mining**:
    - `get_mining_pools(time_frame: str)`

- **Fees**:
    - `get_recommended_fees()`

- **Mempool**
    - `get_mempool()`

- **Lightning**
    - `get_network_stats()`, `get_nodes_in_country(country: str)`, `get_node_stats(node: str)`

## Notes

- **Supported FIAT Currencies**: for every method where a fiat currency is required, here is the list of the supported one
    - ***USD***
    - ***EUR***
    - ***GBP***
    - ***CAD***
    - ***CHF***
    - ***AUD***
    - ***JPY***

- **Time frames**: for every method where a timeframe is required here are the supported one `24h`, `3d`, `1w`, `1m`, `3m`, `6m`, `1y`, `2y`, `3y`

## How To Use

You can easily use and install this package by simply typing:

```
pip install python-mempool-api
```

1. **Import the desired class (the full list is available [here](#classes))**

```
from mempool import <class>
```

2. **Create an object**

```
obj = <class()>
```

3. **Access the methods (the full list is available [here](#methods))**

```
obj.<method>
```


## Conclusion

Congratulations! You've just unlocked the secret to effortlessly fetching Bitcoin data without needing a PhD or a magic crystal ball.  
This script is like your friendly neighborhood Bitcoin butler—ready to serve up various topics around the Bitcoin world with just a few lines of code.

Whether you're trying to impress your friends with your newfound knowledge or just want to keep an eye on your digital treasure, this script has got your back.  
So go ahead, tinker with it, and remember: in the world of Bitcoin, the only thing more volatile than the price is your coffee consumption while you watch the charts.

If you encounter any issue or would like to participate in the development of this package, feel free to DM me on [X.com](https://x.com/k0g1t0?s=11)

Happy coding!

~*It is a mistake to think you can solve any major problems just with potatoes.*~
