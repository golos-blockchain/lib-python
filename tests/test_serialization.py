from binascii import hexlify

import pytest

from golos import Steem
from golosbase import operations
from golosbase.transactions import SignedTransaction

ref_block_num = 54051
ref_block_prefix = "2406554386"
expiration = "2020-06-02T13:38:03"


@pytest.fixture()
def golos(request):
    nodes = ["wss://golos.lexa.host/ws", "wss://golos.solox.world/ws"]
    golos = Steem(nodes=nodes, no_broadcast=True)
    request.cls.golos = golos
    return golos


@pytest.mark.usefixtures("golos")
class TestSerialization:
    def get_hex(self, trx):
        """Get transaction hex."""
        try:
            trx.data.pop("signatures")
        except (AttributeError, KeyError, TypeError):
            pass
        return hexlify(bytes(trx)).decode("ascii")

    def do_test(self, op):
        tx = SignedTransaction(
            ref_block_num=ref_block_num, ref_block_prefix=ref_block_prefix, expiration=expiration, operations=[op]
        )

        node_hex = self.golos.get_transaction_hex(tx.json())
        local_hex = self.get_hex(tx)
        assert local_hex == node_hex

    def print_serialization(self, op):

        for key, value in op.data.items():
            if isinstance(value, operations.GrapheneObject):
                self.print_serialization(value)
            else:
                print("{}: {}".format(key, self.get_hex(value)))

    def test_transfer(self):
        op = operations.Transfer(**{"from": "vvk", "to": "vvk2", "amount": "1.000 GOLOS", "memo": "foo"})

        self.do_test(op)

    @pytest.mark.parametrize(
        "target",
        [
            {"foo": "bar"},
            {"aaa": 123},
            {"author": "ksantoprotein", "permlink": "tip23bot-telegramm-bot-dlya-laikov-avtokleminga-i-igr"},
            {"k{}".format(i): "v{}".format(i) for i in range(0, 35)},
        ],
    )
    def test_donate(self, target):
        _target = operations.VariantObject(target)

        _memo = operations.DonateMemo(**{"app": "golos-id", "version": 1, "target": _target, "comment": "test"})

        op = operations.Donate(
            **{"from": "vvk", "to": "ksantoprotein", "amount": "10 GOLOS", "memo": _memo, "extensions": None}
        )

        self.print_serialization(op)
        self.do_test(op)
