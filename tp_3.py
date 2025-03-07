import os as os
import client as cl
import algokit_utils.transactions.transaction_composer as att

import algokit_utils as au

from utils import (
    account_creation,
    display_info,
)


# compiler le fichier app.py
#os.system("algokit compile py --out-dir ./app app.py")

# générer le fichier client
#os.system("algokit generate client app/DigitalMarketplace.arc32.json --output client.py")

# algorand est une blockchain
algorand = au.AlgorandClient.from_environment()

assetId = 1012

# création des comptes
alice = account_creation(algorand, "ALICE", au.AlgoAmount(algo=10_000))
bob = account_creation(algorand, "BOB", au.AlgoAmount(algo=1000))

# objet intéragir avec app
factory = algorand.client.get_typed_app_factory(
        cl.DigitalMarketplaceFactory, default_sender=alice.address
    )

# créer l'app
result, _ = factory.send.create.create_application(
        cl.CreateApplicationArgs(
            asset_id=assetId, unitary_price=1
        )
    )

display_info(algorand, ["ALICE"])

app_id = 1030
ac = factory.get_app_client_by_id(app_id, default_sender=alice.address)
sp = algorand.get_suggested_params()

mbr_pay = algorand.create_transaction.payment(
    au.PaymentParams(
        sender=alice.address,
        amount=au.AlgoAmount(algo=0.2),
        receiver=ac.app_address,
        extra_fee=au.AlgoAmount(micro_algo=sp.min_fee)
    )
)

ac.send.opt_in_to_asset(
    cl.OptInToAssetArgs(
        mbr_pay= att.TransactionWithSigner(mbr_pay, alice.signer),
    ),
    send_params= au.SendParams(populate_app_call_resources=True)
)

composer.add_app_call_method_call(

)