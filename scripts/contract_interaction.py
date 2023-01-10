from ape import project, accounts


"""
This script shows you how you can interact with your contract after you have 
successfully declared and deployed the contract.
"""


def main():
    account = accounts.containers['starknet'].test_accounts[1]
    contract = project.MyContract.deploy(sender=account)

    # Interact with deployed contract
    # Use a mutable method and include sender to delegate the transaction
    receipt = contract.increase_balance(account.address, 123, sender=account)
    # Use a view method
    value = contract.get_balance(account)
    print(f"value: {value}")
    # Access return data from mutable method receipt
    result = receipt.return_value
    print(f"result: {result}")

    # Note: To pass in arrays as an argument, you have to include the array size beforehand
    contract.store_sum(3, [1, 2, 3], sender=account)
    print(contract.get_last_sum())
