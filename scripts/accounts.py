from ape import accounts


"""
This script shows how you can access imported testnet accounts on the starknet testnet.
"""


def main():
    account = accounts.load("argent")
    print(account.balance)
