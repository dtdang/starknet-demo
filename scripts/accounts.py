from ape import accounts


def main():
    container = accounts.containers['starknet']
    test_acc = container.test_accounts[0]
    print(test_acc.balance)
