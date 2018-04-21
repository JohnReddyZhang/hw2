from datetime import datetime
PRICE_TIERS = ['tier1', 'tier2', 'tier3', 'tier4']
SHOW_TIME = ['m', 'n']
SCREEN = ['1', '2', '3', '4', '5']


class Event(object):
    def __init__(self, show_day, show_time, screen):
        if show_time not in SHOW_TIME:
            print('Show time not valid. Choose between m or n.')
            raise ValueError
        self._showtime_date_form = datetime.strptime(show_day + '1400' if show_time == 'm'
                                                     else show_day + '2000',
                                                     '%Y%m%d%H%M')
        if screen not in SCREEN:
            print('Auditorium not valid. Choose between 1 to 5.')
            raise ValueError
        self._price = None
        self.screen = screen
        self._calculate_price_tier()
        self._ticket_counter = 200

    def _calculate_price_tier(self):
        if self._showtime_date_form.isoweekday() <= 4:
            if self._showtime_date_form.hour == 14:
                self._price = PRICE_TIERS[0]
            elif self._showtime_date_form.hour == 20:
                self._price = PRICE_TIERS[1]
        else:
            if self._showtime_date_form.hour == 14:
                self._price = PRICE_TIERS[2]
            elif self._showtime_date_form.hour == 20:
                self._price = PRICE_TIERS[3]
        return True

    def is_event_valid(self, current_time, valid_operation_time):
        if self._showtime_date_form - current_time > valid_operation_time or self._showtime_date_form < current_time:
            return False
        return True

    def remaining_tickets_lookup(self):
        return self._ticket_counter

    def price_tier_lookup(self):
        return self._price

    def generate_serial_number(self):
        serial = str(self._showtime_date_form.date()).replace('-', '') \
                 + str(self._showtime_date_form.hour).replace(':', '') \
                 + self.screen \
                 + '{:0>3}'.format(str(self._ticket_counter))
        self._ticket_counter -= 1
        return serial
