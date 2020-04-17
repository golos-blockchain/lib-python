# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

from golos import *  # noqa
from golosbase import *  # noqa


# pylint: disable=unused-import,unused-variable
def test_import():
    _ = Steem(['wss://golos.lexa.host/ws'])
    _ = account.PasswordKey
