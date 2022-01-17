from binascii import hexlify

import json
import pytest

from golos import Steem
from golosbase import operations
from golosbase.transactions import SignedTransaction

ref_block_num = 54051
ref_block_prefix = "2406554386"
expiration = "2020-06-02T13:38:03"


@pytest.fixture()
def golos(request):
    nodes = ["wss://golos.lexai.host/ws", "wss://golos.solox.world/ws"]
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
            {"aaa": -123},
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

    def test_invite_transfer(self):
        op = operations.InviteTransfer(**{
            "from": "GLS7Pbawjjr71ybgT6L2yni3B3LXYiJqEGnuFSq1MV9cjnV24dMG3",
            "to": "GLS7Pbawjjr71ybgT6L2yni3B3LXYiJqEGnuFSq1MV9cjnV24dMG3",
            "amount": "1.000 GOLOS",
            "memo": "foo"
        })

        self.do_test(op)

    # test last operation in operationids, in order to check no ids skipped in operationids
    # also it tests extension serialization
    def test_limit_order_cancel_ex(self):
        op = operations.LimitOrderCancelEx(**{
            "owner": "vvk",
            "orderid": 123,
        })

        self.do_test(op)
        op = operations.LimitOrderCancelEx(**{
            "owner": "vvk",
            "pair_to_cancel": {
                "base": "GOLOS",
                "quote": "GBG",
                "reverse": True,
            },
        })

        self.do_test(op)
        obj = str(op)
        obj = json.loads(obj)
        assert len(obj['extensions']) == 1
        assert len(obj['extensions'][0]) == 2
        assert obj['extensions'][0][0] == 0
        assert obj['extensions'][0][1]['base'] == 'GOLOS'
        assert obj['extensions'][0][1]['quote'] == 'GBG'
        assert obj['extensions'][0][1]['reverse'] == True

    def test_delegate_vesting_shares(self):
        op = operations.DelegateVestingShares(**{
            "delegator": "vvk",
            "delegatee": "vvk2",
            "vesting_shares": "10.000001 GESTS",
        })

        self.do_test(op)
        op = operations.DelegateVestingSharesWithInterest(**{
            "delegator": "vvk",
            "delegatee": "vvk2",
            "vesting_shares": "10.000001 GESTS",
            "interest_rate": 1000,
        })

        self.do_test(op)
