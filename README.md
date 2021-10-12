# CryptoBuyBot

CryptoBuyBot is a simple bot that creates a market order on a selected crypto exchange with a selected amount. 

Functionality is intentionally limited to the minimum necessary. This should make it easier to understand and verify the behavior of CryptoBuyBot. 


## Usage
```
usage: bot.py [-h] (--coinbase | --kraken | --binance) --amount AMOUNT
              --ticker TICKER --api-key API_KEY --api-secret API_SECRET
              --api-passphrase API_PASSPHRASE [--verbose]

optional arguments:
  -h, --help            show this help message and exit
  --coinbase            Trade on Coinbase Pro exchange.
  --kraken              Trade on Kraken exchange (NOT SUPPORTED yet).
  --binance             Trade on Binance exchange (NOT SUPPORTED yet).
  --amount AMOUNT
  --ticker TICKER       Selected traiding pair (e.g. BTC-EUR)
  --api-key API_KEY
  --api-secret API_SECRET
  --api-passphrase API_PASSPHRASE
  --verbose

```

## Install
Please install the necessary packages before running bot. 
```
pip install -r requirements.txt
```

## API requirements (Coinbase Pro)
 - View
 - Trade

### How to set a new CoinbasePro API (credists: seCoin3363se)
1. Add an API key
2. Check permitions View and Trade (do not give Transfer permission!)
3. Set a good and long passphrase is you want to. Fill the passphrase in the config.json
4. Set your IP in the white list (security increase)
5. Verify the new API key
6. Fill generated API-SECRET in the config.json as SECRET-KEY
7. Click done (you will not see the API-SECRET anymore)
8. Fill the generated API key (hash like string in the API list) as API-KEY

## Plans and progress
### To Do
- [ ] Kraken support
- [ ] Binance support

## Warning
Please check the functionality of this robot. 
Even if the robot is under your control, never give it an API with the ability to move your fund. 
Check regularly that it works as you expect. 
I make no guarantees that the robot is error-free and will work as you expect.
