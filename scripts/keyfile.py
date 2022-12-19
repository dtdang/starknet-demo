import keyring
from ape import accounts


"""
This script shows how use the set_autosign method available on keyfile accounts 
to autosign messages. This should only be done on necessary occasions like
during testnet automated deployments.
"""


def main():
    # Use keyring package to store secrets
    password = keyring.get_password(
        "starknet-testnet-automations", "ci-shared-account")
    testnet_account = accounts.load("starknet-testnet-account")
    testnet_account.set_autosign(True, passphrase=password)

    # Won't prompt for signing or unlocking
    testnet_account.sign_message([123])
