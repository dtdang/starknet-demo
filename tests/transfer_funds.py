import pytest


@pytest.fixture(scope="session")
def ephemeral_account(devnet_accounts):
    new_account = devnet_accounts.create_account("demo-fund")
    # funder = account.load("argent")
    funder = devnet_accounts.test_accounts[2]
    funder.transfer(new_account, "0.02 ETH")
    new_account.deploy_self()
    return devnet_accounts.load("demo-fund")


def test_ephemeral_balance(ephemeral_account):
    balance = ephemeral_account.balance
    print(balance)
    assert balance > 0
