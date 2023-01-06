import pytest
import ape


@pytest.fixture(scope="session")
def devnet_accounts():
    with ape.networks.starknet.local.use_provider("starknet"):
        return ape.accounts.containers["starknet"].test_accounts


@pytest.fixture(scope="session")
def owner(devnet_accounts):
    return devnet_accounts[0]


@pytest.fixture(scope="session")
def ephemeral_account(devnet_accounts):
    # Any account deployed in the local network are not saved to disk and are ephermeral
    new_account = devnet_accounts.create_account("demo-fund")
    funder = devnet_accounts.test_accounts[2]
    funder.transfer(new_account, "0.02 ETH")
    new_account.deploy_self()

    # This account only exists in the devnet and is not a key-file account.
    return devnet_accounts.load("demo-fund")
