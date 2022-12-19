import ape

"""
This script shows how you can manually transfer funds from an existing account
to a newly created account before deploying the newly created account.
"""


def main():
    existing_account = ape.accounts.load("<EXISTING-ACCOUNT-WITH-FUNDS>")
    print(existing_account.balance)
    new_account = ape.accounts.load("<NEWLY-CREATED-ACCOUNT>")
    existing_account.transfer(new_account, "0.0002 ETH")
    print(new_account.balance)
    new_account.deploy_self()
