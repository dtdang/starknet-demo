import pytest


@pytest.fixture(scope="module")
def contract(project, account):
    account.declare(project.MyContract)
    contract = project.MyContract.deploy(sender=account)
    contract.initialize(sender=account)
    return contract


def test_increase_balance(contract, account):
    initial_balance = contract.get_balance(account)
    contract.increase_balance(account.address, 100, sender=account)
    assert contract.get_balance(account) == initial_balance + 100
