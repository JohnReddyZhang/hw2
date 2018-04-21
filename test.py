#! /usr/bin/env python3
import unittest
import core_function


class Test0BuyTickets(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.BoxOffice = core_function.BOffice()

    def test_0_buy_a_ticket(self):
        self.BoxOffice.buy('20180427', 'm', '1', '1')
        self.assertIn(('20180427', 'm', '1'), self.BoxOffice.tickets)

    def test_1_buy_5_tickets(self):
        self.BoxOffice.buy('20180427', 'm', '1', '5')
        self.assertIn(('20180427', 'm', '1'), self.BoxOffice.tickets)


if __name__ == '__main__':
    unittest.main()