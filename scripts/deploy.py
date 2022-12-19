from ape import accounts, project


def main():
    # This only works if `project.MyContract` was declared previously.
    # The class hash is not necessary as an argument. Ape will look it up.
    #account = accounts.load("demo")
    account = accounts.containers['starknet'].test_accounts[0]
    #declaration = account.declare(project.MyFactory)
    account.declare(project.MyContract)
    #account.deploy(project.MyFactory, declaration.class_hash)
    account.deploy(project.MyContract)

    # OR
    #my_contract = project.MyContract.deploy(sender=account)
    # print(my_contract)
