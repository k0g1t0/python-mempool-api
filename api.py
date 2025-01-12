import requests

class Setup:
    def __init__(self, base_url: str = "https://mempool.space/api/"):
        # initialize the instance with the base url for the api
        self._base_url = base_url

    def _url_fetcher(self, endpoint: str) -> dict:
        # fetch data from a given endpoint and return the json response as a dictionary
        try:
            response = requests.get(endpoint)
            response.raise_for_status()
            # attempt to parse the response as json
            try:
                json_response = response.json()
                # check if the parsed response is a dictionary
                if isinstance(json_response, dict):
                    return json_response
            except ValueError:
                # if json parsing fails, we will handle it below
                pass
            # if the response is not a valid json dictionary, return the raw text
            return response.text
                
        except requests.RequestException as e:
            # print the error if the request fails and return none
            print(f"Error fetching {endpoint}: {e}")
            return None
        
class General(Setup):
    def get_difficulty_adjustment(self) -> dict:
        # get the current difficulty adjustment
        difficulty = self._url_fetcher(f"{self._base_url}v1/difficulty-adjustment")
        return difficulty
    
    def get_btc_price(self, currency: str) -> float:
        # get the current btc price in the specified currency
        if not isinstance(currency, str):
            print("Invalid currency type.")
            return
        price = self._url_fetcher(f"{self._base_url}v1/prices")
        if price:
            return float(price.get(currency.upper(), 0.0))
        return 0.0
    
    def get_btc_historical_price(self, currency: str, timestamp: int) -> float:
        # get the historical btc price for a specific currency and timestamp
        if not isinstance(currency, str):
            print("Invalid currency type.")
            return
        historical_data = self._url_fetcher(f"{self._base_url}v1/historical-price?currency={currency.upper()}&timestamp={timestamp}")
        if historical_data and 'prices' in historical_data:
            for price_entry in historical_data['prices']:
                if currency.upper() in price_entry:
                    return float(price_entry[currency.upper()])
    
class Addresses(Setup):
    def get_address_balance(self, address: str) -> float:
        # get the balance of a given btc address
        if not isinstance(address, str):
            print("Invalid address type.")
            return
        balance = self._url_fetcher(f"{self._base_url}address/{address}")
        if balance and 'chain_stats' in balance:
            return float(balance['chain_stats']['funded_txo_sum'] / 100000000)
        print("Could not fetch address balance")
        return 0.0
    
    def address_validation(self, address: str) -> bool:
        # validate if the given btc address is valid
        if not isinstance(address, str):
            print("Invalid address type.")
            return
        validation = self._url_fetcher(f"{self._base_url}v1/validate-address/{address}")
        return bool(validation and validation.get('isvalid'))
    
class Blocks(Setup):
    def get_last_block_height(self) -> int:
        # get the height of the last btc block
        block_info = self._url_fetcher(f"{self._base_url}blocks/tip/height")
        return int(block_info) if block_info else None
    
    def get_block_header(self, block_hash: str) -> str:
        # get the header of a specific block by its hash
        if not isinstance(block_hash, str):
            print("Invalid block hash type.")
            return
        header = self._url_fetcher(f"{self._base_url}block/{block_hash}/header")
        return header
    
class Mining(Setup):
    def get_mining_pools(self, time_frame: str) -> list[dict]:
        # get the list of active btc mining pools for a specified time period
        if not isinstance(time_frame, str):
            print("Invalid time period.")
            return
        pools_info = self._url_fetcher(f"{self._base_url}v1/mining/pools/{time_frame.lower()}")
        return pools_info.get('pools', []) if pools_info else []
    
class Fees(Setup):
    def get_recommended_fees(self) -> dict:
        # get the recommended btc transaction fees
        fees_info = self._url_fetcher(f"{self._base_url}v1/fees/recommended")
        return fees_info
    
class Mempool(Setup):
    def get_mempool(self) -> dict[str, any]:
        # get the current state of the mempool
        mempool = self._url_fetcher(f"{self._base_url}mempool")
        return mempool
    
class Lightning(Setup):
    def get_network_stats(self) -> dict:
        # get the latest statistics of the lightning network
        stats = self._url_fetcher(f"{self._base_url}v1/lightning/statistics/latest")
        return stats['latest']
    
    def get_nodes_in_country(self, country: str) -> list[dict]:
        # get the list of lightning nodes in a specified country
        if not isinstance(country, str):
            print("Invalid country.")
            return
        nodes = self._url_fetcher(f"{self._base_url}v1/lightning/nodes/country/{country.lower()}")
        return nodes['nodes']
    
    def get_node_stats(self, node: str) -> dict:
        # get statistics for a specific lightning node
        if not isinstance(node, str):
            print("Invalid node type.")
            return
        node_stats = self._url_fetcher(f"{self._base_url}v1/lightning/nodes/{node}")
        return node_stats