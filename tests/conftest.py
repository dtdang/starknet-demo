import pytest
import ape


@pytest.fixture(scope="session")
def devnet_accounts():
    with ape.networks.starknet.local.use_provider("starknet"):
        return ape.accounts.containers["starknet"]


@pytest.fixture(scope="session")
def account(devnet_accounts):
    return devnet_accounts.test_accounts[0]
