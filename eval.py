import algokit_utils as au
import algosdk as sdk
import client as cl
import os as os
import algokit_utils.transactions.transaction_composer as att


from utils import (
    account_creation,
    display_info,
)

# # compiler le fichier app.py
# os.system("algokit compile py --out-dir ./app app.py")

# # générer le fichier client
# os.system("algokit generate client app/Eval.arc32.json --output client.py")

algorand = au.AlgorandClient.testnet()

# trouver son compte
mnemonic = "blame trigger worth cable diesel mule merry fine left embrace tool gate peanut pig lift denial move dish dolphin champion melody wave swift about october"
private_key = sdk.mnemonic.to_private_key(mnemonic)
account_address = sdk.account.address_from_private_key(private_key)
print(f"Adresse du compte: {account_address}")

# récupérer son compte
account = algorand.account.from_mnemonic(mnemonic=mnemonic)

# objet intéragir avec app
factory = algorand.client.get_typed_app_factory(
        cl.EvalFactory, default_sender=account.address
    )


# appeller fonction claim_algo du app.py
app_id = 736038676

ac = factory.get_app_client_by_id(app_id, default_sender=account.address)
sp = algorand.get_suggested_params()
send_params= au.SendParams(populate_app_call_resources=True)

# ac.send.claim_algo(
#     params=au.CommonAppCallParams(
#         box_references=[account.address],
#         sender=account.address,
#         signer=account.signer
#     ),
#     send_params=send_params,
# )

# appeller fonction opt_in_to_asset du app.py

# mbr_pay = algorand.create_transaction.payment(
#     au.PaymentParams(
#         sender=account.address,
#         amount=au.AlgoAmount(algo=0.2),
#         receiver=ac.app_address,
#         extra_fee=au.AlgoAmount(micro_algo=sp.min_fee)
#     )
# )

# result = algorand.send.asset_create(
#         au.AssetCreateParams(
#             sender=account.address,
#             signer=account.signer,
#             total=15,
#             decimals=0,
#             default_frozen=False,
#             unit_name="PY-CL-FD",  # 8 Max
#             asset_name="Proof of Attendance Py-Clermont",
#             url="https://pyclermont.org/",
#             note="Hello Clermont",
#         )
#     )

# asset_id = result.confirmation["asset-index"]
# ac.send.opt_in_to_asset(
#     cl.OptInToAssetArgs(
#         mbr_pay= att.TransactionWithSigner(mbr_pay, account.signer),
#         asset=asset_id
#     ),
#     params=au.CommonAppCallParams(
#         box_references=[account.address],
#         sender=account.address,
#         signer=account.signer
#     ),
#     send_params= au.SendParams(populate_app_call_resources=True)
# )

# ac.send.sum(
#     args=cl.SumArgs(
#         array=bytes([1, 2])
#     ),
#     params=au.CommonAppCallParams(
#         box_references=[account.address],
#         sender=account.address,
#         signer=account.signer
#     ),
#     send_params= au.SendParams(populate_app_call_resources=True)
# )

ac.send.update_box(
    args=cl.UpdateBoxArgs(
        value="Fave"
    ),
    params=au.CommonAppCallParams(
        box_references=[account.address],
        sender=account.address,
        signer=account.signer
    ),
    send_params= au.SendParams(populate_app_call_resources=True)
)