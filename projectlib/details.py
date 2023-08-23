from dataclasses import dataclass




#usually most use dictionary for such use cases  like below

d_coin = {'symbol':'BTC','name':'Bitcoin','value':1000.10}
print(d_coin['name'])


#Instead we can use dataclass for 
# in order to reduce error based on key string
#

@dataclass
class Coin:
    symbol: str
    name: str
    value: float


coin = Coin('BTC','Bitcoin',1000.10)
print(coin)
print(coin.name)