import algokit_utils as au
import algosdk as sdk
from algokit_utils import AlgorandClient, SigningAccount, AssetCreateParams
import random

from utils import (
    account_creation,
    display_info,
)

def generate_test_asset(algorand: au.AlgorandClient, sender: SigningAccount, total: int | None = None) -> int:
    """Create a test asset and return its ID"""
    if total is None:
        total = random.randint(20, 120)

    create_result = algorand.send.asset_create(
        au.AssetCreateParams(
            sender=sender.address,
            total=total,
            decimals=0,
            default_frozen=False,
        
            unit_name="TST",
            asset_name=f"Test Asset {random.randint(1,100)}",
            manager=sender.address,
            reserve=sender.address,
            freeze=sender.address,
            clawback=sender.address,
        )
    )

    return int(create_result.confirmation["asset-index"])

if __name__ == "__main__":

    algorand = au.AlgorandClient.from_environment()

    suggested_params = algorand.get_suggested_params()

    algod_client = algorand.client.algod
    indexer_client = algorand.client.indexer
    alice=account_creation(algorand, "Alice", au.AlgoAmount(algo=10_000))
    bob=account_creation(algorand, "Bob", au.AlgoAmount(algo=100))

    asset_id = generate_test_asset(algorand, alice)
    params = algod_client.suggested_params()
    # Bob opts-in to receive the asset
    opt_in_txn = algorand.send.asset_opt_in(
        params=au.AssetOptInParams(
                sender=bob.address,
                asset_id=1015
        )
    )

    # Create the asset transfer transaction
    asset_transfer_txn = algorand.send.asset_transfer(
        au.AssetTransferParams(
            sender=alice.address,
            asset_id= 1015,
            amount=1,
            receiver=bob.address
        )
    )

    # message de confirmation 
    print('Transaction confirmed, round: '
            f'{asset_transfer_txn.confirmation["confirmed-round"]}')