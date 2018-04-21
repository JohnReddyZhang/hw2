#! /usr/bin/env python3
import unittest
import core_function


class Test0BuyTickets(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.BoxOffice = core_function.BOffice()

    def test_0_buy_a_ticket(self):
        self.BoxOffice.buy('20180427', 'm', '1', '1')
        print(self.BoxOffice._event_category)
        self.assertIn(('20180427', 'm', '1'), self.BoxOffice._event_category)
        print(self.BoxOffice._serial_numbers)
        self.assertIn('20180427141200', self.BoxOffice._serial_numbers)

    def test_1_buy_5_tickets(self):
        self.assertTrue(self.BoxOffice.buy('20180427', 'm', '1', '5'))

    def test_2_buy_11_tickets(self):
        self.assertFalse(self.BoxOffice.buy('20180427', 'm', '1', '11'))


if __name__ == '__main__':
    unittest.main()
