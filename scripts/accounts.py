from ape import accounts


"""
This script shows how you can access test accounts on the local starknet network.
"""


def main():
    container = accounts.containers['starknet']
    test_acc = container.test_accounts[0]
    print(test_acc.balance)
