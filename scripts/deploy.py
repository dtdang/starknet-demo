from ape import accounts, project


"""
This script will show you the different methods available of how to 
declare and deploy a contract.
"""


def main():
    # Load either a starknet account or use a test account
    # account = accounts.load("demo")
    account = accounts.containers['starknet'].test_accounts[0]
    declaration = account.declare(project.MyContract)
    print(f"declaration {declaration.class_hash}")

    # This only works if `project.MyContract` was declared previously.
    # The class hash is not necessary as an argument. Ape will look it up.
    account.deploy(project.MyContract)

    # OR you can deploy using
    my_contract = project.MyContract.deploy(sender=account)
    print(my_contract)

    # OR you can deploy using a factory contract
    # This contracts accepts a class hash of a declared contract and then deploys it
    account.declare(project.MyFactory)
    factory = project.MyFactory.deploy(declaration.class_hash, sender=account)
    factory_deployment = factory.deploy_my_contract(sender=account)
    print(factory_deployment.status)
