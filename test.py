#! /usr/bin/env python3
import unittest
import core_function

# Date is set to fit 20180422, modify them here:
PLUS_1_DAY = '20180423'
PLUS_2_DAY = '20180424'
PLUS_3_DAY = '20180425'
PLUS_4_DAY = '20180426'


class Test0BuyTickets(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.BoxOffice = core_function.BoxOffice(name='test_buy')

    def test_0_buy_a_ticket(self):
        self.assertTrue(self.BoxOffice.buy(PLUS_1_DAY, 'm', '1', '1'))
        print(self.BoxOffice._event_category)
        self.assertIn((PLUS_1_DAY, 'm', '1'), self.BoxOffice._event_category)
        print(self.BoxOffice._serial_numbers)
        self.assertIn(PLUS_1_DAY+'141000', self.BoxOffice._serial_numbers)

    def test_1_buy_5_tickets(self):
        self.assertTrue(self.BoxOffice.buy(PLUS_1_DAY, 'm', '1', '5'))
        self.assertIn(PLUS_1_DAY+'141005', self.BoxOffice._serial_numbers)

    def test_2_buy_11_tickets(self):
        self.assertFalse(self.BoxOffice.buy(PLUS_1_DAY, 'm', '1', '11'))
        self.assertNotIn(PLUS_1_DAY+'141015', self.BoxOffice._serial_numbers)

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
            self.BoxOffice.buy(PLUS_1_DAY, 'm', '1', '10')
        self.assertIn(PLUS_1_DAY+'141199', self.BoxOffice._serial_numbers)
        self.assertFalse(self.BoxOffice.buy(PLUS_1_DAY, 'm', '1', '1'))

    def test_7_buy_two_events(self):
        self.assertTrue(self.BoxOffice.buy(PLUS_1_DAY, 'n', '2', '1'))
        self.assertTrue(self.BoxOffice.buy(PLUS_2_DAY, 'm', '1', '1'))
        self.assertIn(PLUS_1_DAY+'202000', self.BoxOffice._serial_numbers)
        self.assertIn(PLUS_2_DAY+'141000', self.BoxOffice._serial_numbers)
        self.assertEqual(self.BoxOffice._serial_numbers[PLUS_2_DAY+'141000'].price_tier_lookup(), 'tier1')


class Test1RefundTickets(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.BoxOffice = core_function.BoxOffice('test_refund')

    def test_0_refund_1(self):
        self.BoxOffice.buy(PLUS_1_DAY, 'm', '2', '1')
        self.BoxOffice.refund(PLUS_1_DAY+'142000')
        self.assertNotIn(PLUS_1_DAY+'142000', self.BoxOffice._serial_numbers)

    def test_1_refund_one_of_three(self):
        self.BoxOffice.buy(PLUS_1_DAY, 'm', '2', '3')
        self.BoxOffice.refund(PLUS_1_DAY+'142001')
        self.assertNotIn(PLUS_1_DAY+'142001', self.BoxOffice._serial_numbers)

    def test_2_refund_then_buy(self):
        self.BoxOffice.buy(PLUS_1_DAY, 'm', '2', '3')
        self.BoxOffice.refund(PLUS_1_DAY+'142001')
        self.assertNotIn(PLUS_1_DAY+'142001', self.BoxOffice._serial_numbers)

        self.BoxOffice.buy(PLUS_1_DAY, 'm', '2', '1')
        self.assertIn(PLUS_1_DAY+'142001', self.BoxOffice._serial_numbers)
        self.assertNotIn('001', self.BoxOffice._event_category[(PLUS_1_DAY, 'm', '2')]._ticket_counter)

    def test_3_refund_not_existing_event(self):
        self.assertFalse(self.BoxOffice.refund('20160427142001'))


class Test2Reports(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.BoxOffice = core_function.BoxOffice('test_report')
        # 4.23 sells 2 tickets, one for each time in auditorium 1
        cls.BoxOffice.buy(PLUS_1_DAY, 'm', '1', '1')
        cls.BoxOffice.buy(PLUS_1_DAY, 'n', '1', '1')
        # 4.26 sells 15 tickets, all in matinee auditorium 1
        cls.BoxOffice.buy(PLUS_4_DAY, 'm', '1', '10')
        cls.BoxOffice.buy(PLUS_4_DAY, 'm', '1', '5')
        # 4.25 sells 10 tickets in matinee auditorium 1, 6 in night auditorium 2
        cls.BoxOffice.buy(PLUS_3_DAY, 'm', '1', '10')
        cls.BoxOffice.buy(PLUS_3_DAY, 'n', '2', '6')
        # 4.24 sells 2, refunds 2.
        cls.BoxOffice.buy(PLUS_2_DAY, 'n', '1', '2')
        cls.BoxOffice.refund(PLUS_2_DAY + '201000')
        cls.BoxOffice.refund(PLUS_2_DAY + '201001')

    def test_0_report_event(self):
        self.assertEqual(self.BoxOffice.report_event(PLUS_1_DAY, 'm', '1'), 199)

    def test_1_report_event(self):
        self.assertEqual(self.BoxOffice.report_event(PLUS_4_DAY, 'm', '1'), 185)

    def test_2_report_event_not_exist(self):
        self.assertFalse(self.BoxOffice.report_event(PLUS_4_DAY, 'n', '2'))

    def test_3_report_daily(self):
        self.assertEqual(self.BoxOffice.report_day(PLUS_1_DAY), 2)

    def test_4_report_daily(self):
        self.assertEqual(self.BoxOffice.report_day(PLUS_4_DAY), 15)

    def test_5_report_daily(self):
        self.assertEqual(self.BoxOffice.report_day(PLUS_3_DAY), 16)

    def test_6_report_daily(self):
        self.assertEqual(self.BoxOffice.report_day(PLUS_2_DAY), 0)

    def test_6_report_daily_no_record(self):
        self.assertEqual(self.BoxOffice.report_day('20180422'), 0)


class Test3LoadFiles(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.BoxOffice = core_function.BoxOffice('test_report')

    def test_0_report(self):
        self.assertEqual(self.BoxOffice.report_day(PLUS_3_DAY), 16)


if __name__ == '__main__':
    unittest.main()
