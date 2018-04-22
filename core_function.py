import pickle, pathlib
from datetime import datetime, timedelta
from event_class import Event

PATH = pathlib.Path('./data')
if not PATH.exists():
    PATH.mkdir()


class BoxOffice(object):
    """
    Box Office class that do the operations.
    """
    def __init__(self, name='default'):
        self.name = name
        self.now = None
        self._event_category = {}
        self._serial_numbers = {}
        self._valid_operation_time = timedelta(days=7)
        self._history = PATH / '{}.pkl'.format(self.name)
        if self._history.exists():
            with open(self._history, 'rb') as source:
                self._event_category, self._serial_numbers = pickle.load(source)

    def dump_data(self):
        with open(self._history, 'wb') as dump:
            pickle.dump([self._event_category, self._serial_numbers], dump, pickle.HIGHEST_PROTOCOL)

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
            self.dump_data()
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
            self.dump_data()
            return True

    def report_event(self, show_day, show_time, screen):
        info = (show_day, show_time, screen)
        # print(info)
        if info in self._event_category:
            isinstance(self._event_category[info], Event)
            event = self._event_category[info]
            print('\nCurrent event on {} {} in Auditorium {}\n'
                  'has sold {} tickets, has {} vacant seats'
                  .format(show_day, 'Matinee' if show_time == 'm' else 'Night', screen,
                          200 - event.vacant_ticket_report(), event.vacant_ticket_report()))
            return event.vacant_ticket_report()
        else:
            print('\nDid not find event.')

    def report_day(self, day):
        sold = 0
        if self._event_category == {}:
            print('No data found.')
            return None
        else:
            for info, event in self._event_category.items():
                isinstance(event, Event)
                if info[0] == day:
                    sold += (200 - event.vacant_ticket_report())
            print('{} tickets sold on day {}'.format(sold, day))
            return sold
