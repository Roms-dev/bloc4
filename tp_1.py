import algokit_utils as au
import algosdk as sdk

from utils import (
    account_creation,
    display_info,
)

# algorand est une blockchain
algorand = au.AlgorandClient.from_environment()

algod_client = algorand.client.algod
indexer_client = algorand.client.indexer

print(algod_client.block_info(0))
print(indexer_client.health())

# création des comptes
alice = account_creation(algorand, "ALICE", au.AlgoAmount(algo=10_000))
bob = account_creation(algorand, "BOB", au.AlgoAmount(algo=1000))

# création paiement alice vers bob
pay_txn = algorand.create_transaction.payment(
    au.PaymentParams(
        sender=alice.address,
        receiver=bob.address,
        amount=au.AlgoAmount(algo=1)
))

# signer la transaction de alice (envoyeur)
pay_txn_signed = pay_txn.sign(
    alice.private_key
)

# envoie de la transaction
tx_id = algorand.client.algod.send_transaction(txn=pay_txn_signed)

res = sdk.transaction.wait_for_confirmation(algod_client, txid=tx_id)

# afficher le résultat
print(res)

# faire l'action inverse bob vers alice en une seul fois
payback_txn = algorand.send.payment(
    params=au.PaymentParams(
        sender=bob.address,
        receiver=alice.address,
        amount=au.AlgoAmount(algo=1),
        signer=bob.signer
    )
)

# message de confirmation 
print('Transaction confirmed, round: '
        f'{payback_txn.confirmation["confirmed-round"]}')