from ape import accounts, project


def main():
    #account = accounts.load("<MY_STARK_ACCOUNT>")
    account = accounts.containers['starknet'].test_accounts[0]
    declaration = account.declare(project.MyContract)
    print(declaration.class_hash)
