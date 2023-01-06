from ape import accounts, project


def main():
    #acct = accounts.load("Alias")
    acct = accounts.containers['starknet'].test_accounts[0]
    print(acct.balance)
    contract = project.MyContract.deploy(sender=acct)

    receipt = contract.increase_balance(acct.address, 100, sender=acct, max_fee=400000000000000)
    print(receipt.return_value)
