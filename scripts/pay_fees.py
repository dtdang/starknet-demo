from ape import accounts, project


def main():
    acct = accounts.load("Alias")
    print(acct.balance)
    contract = project.MyContract.deploy()

    receipt = contract.my_mutable_method(123, max_fee=2900000000000)
