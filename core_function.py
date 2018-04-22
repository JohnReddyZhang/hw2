from sys import exit
from datetime import datetime, timedelta
from event_class import Event


class BOffice(object):
    """
    Box Office class that do the operations.
    """
    def __init__(self):
        self.now = None
        self._event_category = {}
        self._serial_numbers = {}
        self._valid_operation_time = timedelta(days=7)

    def buy(self, show_day, show_time, screen, number_of_ticket=1):
        try:
            number_of_ticket = int(number_of_ticket)
            if number_of_ticket > 10:
                print('Cannot buy more than 10 _event_category a time.')
                raise IndexError
            for i in range(0, int(number_of_ticket)):
                success = self._buy(show_day, show_time, screen)
                if not success:
                    return False
            return True
        except IndexError:
            return False

    def _buy(self, show_day, show_time, screen):  # Method for buying a single ticket.
        self.now = datetime.now()
        info = (show_day, show_time, screen)
        # (date, showtime, auditorium)
        if info not in self._event_category:
            event = Event(show_day, show_time, screen)
            if not event.event_is_valid(self.now, self._valid_operation_time):
                print('Cannot buy event tickets for this day.')
                return False
            self._event_category[info] = event
        else:
            event = self._event_category[info]

        if event.remaining_tickets_lookup() == 0:
            print('Ticket for this event is sold out.')
            return False
        else:
            serial = event.generate_serial_number()
            self._serial_numbers[serial] = event
            print('Success! Your serial number is:{}\n'
                  'Price tier: {}\n'
                  .format(serial, self._serial_numbers[serial].price_tier_lookup()))
            return True

    def refund(self, serial):
        self.now = datetime.now()

        if serial not in self._serial_numbers:
            print('Did not find record for this serial number.')
            return False

        event = self._serial_numbers[serial]
        if not isinstance(event, Event):
            raise TypeError
        if event.event_is_over(self.now):
            print('Refundable time passed. Sorry')
            return False

        refund_price = event.execute_refund(serial)
        self._serial_numbers.pop(serial)
        if refund_price is False:
            print('Refund attempt failed.')
            return False
        else:
            print('Success! Refund price: {}'.format(refund_price))
            return True

    def report_event(self, show_day, show_time, screen):
        info = (show_day, show_time, screen)
        # print(info)
        if info in self._event_category.keys():
            print('Current event on {} {} in Auditorium {}\n'
                  'has sold {} _event_category, has {} vacant seats'
                  .format(show_day, 'Matinee' if show_time == 'm' else 'Night', screen,
                          200 - self._event_category[info]['_event_category'], self._event_category[info]['_event_category']))
        else:
            print('Did not find event.')

    def report_day(self, day):
        sold = 0
        if self._event_category == {}:
            print('No data found.')
        else:
            for info, value in self._event_category.items():
                if info[0] == day:
                    sold += (200 - len(value['_event_category']))
            print('{} _event_category sold on day {}'.format(sold, day))