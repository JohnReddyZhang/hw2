#! /usr/bin/env python3
import unittest
import core_function


class Test0BuyTickets(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.BoxOffice = core_function.BOffice()

    def test_0_buy_a_ticket(self):
        self.assertTrue(self.BoxOffice.buy('20180427', 'm', '1', '1'))
        print(self.BoxOffice._event_category)
        self.assertIn(('20180427', 'm', '1'), self.BoxOffice._event_category)
        print(self.BoxOffice._serial_numbers)
        self.assertIn('20180427141200', self.BoxOffice._serial_numbers)

    def test_1_buy_5_tickets(self):
        self.assertTrue(self.BoxOffice.buy('20180427', 'm', '1', '5'))
        self.assertIn('20180427141195', self.BoxOffice._serial_numbers)

    def test_2_buy_11_tickets(self):
        self.assertFalse(self.BoxOffice.buy('20180427', 'm', '1', '11'))
        self.assertNotIn('20180427141185', self.BoxOffice._serial_numbers)

    def test_3_buy_invalid_date_tickets(self):
        self.assertFalse(self.BoxOffice.buy('20180901', 'm', '1', '1'))
        self.assertNotIn('20180901', self.BoxOffice._event_category)

    def test_4_buy_invalid_date_tickets_2(self):
        self.assertFalse(self.BoxOffice.buy('20160901', 'm', '1', '1'))
        self.assertNotIn('20160901', self.BoxOffice._event_category)

    def test_5_buy_wrong_tickets(self):
        self.assertFalse(self.BoxOffice.buy('20160901', 'm', '1', '21'))

    def test_6_sold_out(self):
        for i in range(20):
            self.BoxOffice.buy('20180427', 'm', '1', '10')
        self.assertIn('20180427141001', self.BoxOffice._serial_numbers)
        self.assertFalse(self.BoxOffice.buy('20180427', 'm', '1', '1'))


if __name__ == '__main__':
    unittest.main()
