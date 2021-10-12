#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: CryptON
# @Date: 2021-10-12
# @Last Modified by: CryptON

__author__ = "CryptON"
__copyright__ = "Copyright 2021, CryptON"
__license__ = "MIT"
__version__ = "0.0.1 Beta"
__maintainer__ = "CryptON"
__email__ = "CryptON112358@protonmail.com"


import sys
import argparse
import json
import time

from exbts import CoinbaseAPI


def validate_args(args):
    if args.amount <= 0:
        print('ERROR: amount must be positive number.', file=sys.stderr)
        sys.exit(-1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--coinbase', action='store_true',
                       help="Trade on Coinbase Pro exchange.")
    group.add_argument('--kraken', action='store_true',
                       help="Trade on Kraken exchange (NOT SUPPORTED yet).")
    group.add_argument('--binance', action='store_true',
                       help="Trade on Binance exchange (NOT SUPPORTED yet).")
    parser.add_argument('--amount', required=True, type=float,
                        default=10.0, help='')
    parser.add_argument('--ticker', required=True, type=str,
                        default='BTC-EUR', help='Selected traiding pair (e.g. BTC-EUR)')
    parser.add_argument('--api-key', required=True, type=str, help="")
    parser.add_argument('--api-secret', required=True, type=str, help="")
    parser.add_argument('--api-passphrase', required=True, type=str, help="")
    args = parser.parse_args()

    validate_args(args)

    # connect exchange api
    ex_api = None
    if args.coinbase:
        ex_api = CoinbaseAPI(
            args.api_key, args.api_secret, args.api_passphrase)
    elif args.kraken:
        raise NotImplementedError('Kraken API is not supported yet.')
    elif args.binance:
        raise NotImplementedError('Binance API is not supported yet.')

    ticker_array = args.ticker.split("-")
    crypto = ticker_array[0]
    fiat = ticker_array[1]

    # check fiat balance
    result_fiat, value_fiat = ex_api.check_balance(fiat)
    if not result_fiat:
        print(
            f'ERROR: fiat balance check failed with message: {value_fiat}', file=sys.stderr)
        sys.exit(-1)
    else:
        print(f'Your {fiat} balance is {value_fiat}.')

    # check crypto balance
    result_crypto, value_crypto = ex_api.check_balance(crypto)
    if not result_crypto:
        print(
            f'ERROR: crypto balance check failed with message: {value_crypto}', file=sys.stderr)
        sys.exit(-1)
    else:
        print(f'Your {crypto} balance is {value_crypto}.')

    if args.amount > float(value_fiat):
        print(
            f'ERROR: insufficient balance for purchase.', file=sys.stderr)
        sys.exit(-1)

    result = ex_api.buy_market(args.amount, args.ticker)

    if 'message' in result:
        print(
            f'ERROR: marked order failed {result["message"]}.', file=sys.stderr)
        sys.exit(-1)
    else:
        print(f'Your market order is {result["status"]}.')


    order_id = result['id']
    result = ex_api.get_order(order_id)

    while result['status'] != 'done':
        print(f'Waiting for the order to be closed.')
        time.sleep(0.5)
        result = ex_api.get_order(order_id)

    print(f'Order closed.')
