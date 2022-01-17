# -*- coding: utf-8 -*-
import os
import sys

from golos import *  # noqa
from golosbase import *  # noqa

sys.path.insert(0, os.path.abspath(".."))


# pylint: disable=unused-import,unused-variable
def test_import():
    _ = Steem(["wss://golos.lexai.host/ws"])
    _ = account.PasswordKey
