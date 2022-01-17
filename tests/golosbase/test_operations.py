import unittest

from golosbase.operations import Amount

class Testcases(unittest.TestCase):
    def test_amount(self):
        am = Amount('1.010 GOLOS')
        self.assertEqual(am.amount, 1.010)
        self.assertEqual(am.asset, 'GOLOS')
        self.assertEqual(am.precision, 3)
        self.assertEqual(str(am), '1.010 GOLOS')
        self.assertEqual(am.isUIA, False)

        am = Amount('1 GOLOS')
        self.assertEqual(am.amount, 1)
        self.assertEqual(am.asset, 'GOLOS')
        self.assertEqual(am.precision, 3)
        self.assertEqual(str(am), '1.000 GOLOS')
        self.assertEqual(am.isUIA, False)

        am = Amount('-1.010 GBG')
        self.assertEqual(am.amount, -1.010)
        self.assertEqual(am.asset, 'GBG')
        self.assertEqual(am.precision, 3)
        self.assertEqual(str(am), '-1.010 GBG')
        self.assertEqual(am.isUIA, False)

        am = Amount('1.000001 GESTS')
        self.assertEqual(am.amount, 1.000001)
        self.assertEqual(am.asset, 'GESTS')
        self.assertEqual(am.precision, 6)
        self.assertEqual(str(am), '1.000001 GESTS')
        self.assertEqual(am.isUIA, False)

        am = Amount('1.00000000000001 AAA')
        self.assertEqual(am.amount, 1.00000000000001)
        self.assertEqual(am.asset, 'AAA')
        self.assertEqual(am.precision, 14)
        self.assertEqual(str(am), '1.00000000000001 AAA')
        self.assertEqual(am.isUIA, True)

        # fails now due to float type usage
        # am = Amount('9223372036854775807 BBB')
        # self.assertEqual(am.amount, 9223372036854775807)
        # self.assertEqual(am.asset, 'BBB')
        # self.assertEqual(am.precision, 0)
        # self.assertEqual(str(am), '9223372036854775807 BBB')
        # self.assertEqual(am.isUIA, True)

if __name__ == '__main__':
    unittest.main()
