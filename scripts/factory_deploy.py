from ape import Contract, accounts, networks, project


def main():
    account = accounts.load("<MY_STARK_ACCOUNT>")
    declaration = account.declare(project.MyContract)

    # NOTE: Assuming you have a contract named 'ContractFactory'.
    factory = project.ContractFactory.deploy(declaration.class_hash)

    call_result = factory.deploy_my_contract()
    contract_address = networks.starknet.decode_address(call_result)
    contract = Contract(
        contract_address, contract_type=project.MyContract.contract_type)
