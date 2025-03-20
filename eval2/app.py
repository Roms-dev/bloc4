from typing import TypeAlias
# Doc https://algorandfoundation.github.io/puya/index.html
# Doc https://algorandfoundation.github.io/algokit-utils-py/index.html
from algopy import (
    Account,
    ARC4Contract,
    BoxMap,
    Bytes,
    Asset,
    Global,
    Txn,
    itxn,
    UInt64,
    arc4,
    gtxn,
    op,
)

class Box:
    def __init__(self, boxes):
        self.boxes = boxes
    @arc4.abimethod()
    def get_box(self):
        return self.boxes

