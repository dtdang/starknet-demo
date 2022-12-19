import ape


def main():
    existing_account = ape.accounts.load("argent")
    new_account = ape.accounts.load("demo")
    existing_account.transfer(new_account, "0.0002 ETH")
    new_account.deploy_self()
