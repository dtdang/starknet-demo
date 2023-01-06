import pytest


@pytest.fixture(scope="module")
def contract(project, owner):
    owner.declare(project.MyContract)
    contract = project.MyContract.deploy(sender=owner)
    contract.initialize(sender=owner)
    return contract


def test_increase_balance(contract, owner):
    initial_balance = contract.get_balance(owner)
    contract.increase_balance(owner.address, 100, sender=owner)
    assert contract.get_balance(owner) == initial_balance + 100
