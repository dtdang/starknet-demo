from ape import project, accounts


def main():
    account = accounts.containers['starknet'].test_accounts[0]
    contract = project.MyContract.deploy(sender=account)

    # Interact with deployed contract
    receipt = contract.my_mutable_method(123)
    value = contract.my_view_method()
    print("value " + value)
    result = receipt.return_value
    print("result " + result)

    # Include a sender to delegate the transaction to an account contract
    account = accounts.load("my_account")
    receipt = contract.my_mutable_method(123, sender=account)
    print("receipt " + receipt)
