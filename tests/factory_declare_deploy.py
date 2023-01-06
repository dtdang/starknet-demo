from ape import accounts, project, Contract
from ape_starknet import Starknet


def test_declare_and_deploy():
    """
    This test shows a realistic flow.
    1. Declare a contract.
    2. Declare a factory contract.
    3. Use the universal deployer contract to deploy factory contract
       (with other class hash as argument).
    4. Use the factory contract to deploy the other contract.
    """
    account = accounts.containers['starknet'].test_accounts[0]
    # Declare the contracts
    # Tracked to make sure Declares cost money.
    balance_before = account.balance
    declaration = account.declare(project.MyContract)
    factory_declaration = account.declare(project.MyFactory)
    assert (declaration.class_hash)
    assert (factory_declaration.class_hash)

    # Ensure the Declares cost money
    actual_balance = account.balance
    total_fees = declaration.total_fees_paid + factory_declaration.total_fees_paid
    expected_balance = balance_before - total_fees
    assert (actual_balance == expected_balance)

    # Deploy the factory contract. It takes the class hash of the other contract as its
    # argument so it can create instances of it.
    # NOTE: We would not be able to deploy the factory if we did not declare it above.
    #  and we don't need to tell ape the factory's class-hash - it can configure it out.
    factory = project.MyFactory.deploy(
        declaration.class_hash, sender=account)
    assert (factory.address)
    assert (factory.deploy_my_contract)

    # Use custom factory method to create a new contract.
    balance_before = account.balance
    receipt = factory.create_my_contract(sender=account)
    actual_balance = account.balance
    expected_balance = balance_before - receipt.total_fees_paid
    assert (actual_balance == expected_balance)

    # Grab the new contract address from the receipt's logs.
    logs = list(receipt.decode_logs(factory.contract_deployed))
    new_contract_address = Starknet.decode_address(logs[0]["contract_address"])

    # Interact with deployed contract from 'class_hash'.
    new_contract_instance = Contract(
        new_contract_address, contract_type=project.MyContract.contract_type
    )
    assert (new_contract_instance)
    new_contract_instance.initialize(sender=account)
    balance_pre_call = new_contract_instance.get_balance(account)
    new_contract_instance.increase_balance(account, 9, sender=account)
    assert (new_contract_instance.get_balance(account) == balance_pre_call + 9)
