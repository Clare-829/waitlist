import unittest
from waitlist import Waitlist


class TestWaitLost(unittest.TestCase):
    def test_add_customer(self):
    #Testing to make sure items are being added and stored in the list
        new_waitlist = Waitlist()
        new_waitlist.add_customer('Mary Willow', '10:55')
        new_waitlist.add_customer('Collins Ponds', '08:30')
        self.assertTrue(len(new_waitlist), 2)

    def test_peek(self):
        new_waitlist = Waitlist()
        new_waitlist.add_customer('Mary Willow', '10:55')
        new_waitlist.add_customer('Collins Ponds', '08:30')
        new_waitlist.add_customer('Michelle Rice', '18:45')
        assert(new_waitlist.peek() ==  'Collins Ponds', '08:30')

    def test_seat_customer(self):
        new_waitlist = Waitlist()
        new_waitlist.add_customer('Mary Willow', '10:55')
        new_waitlist.add_customer('Collins Ponds', '08:30')
        new_waitlist.add_customer('Michelle Rice', '18:45')
        assert(new_waitlist.seat_customer() ==  'Collins Ponds')

    def test_print_reservationk(self):
        new_waitlist = Waitlist()
        new_waitlist.add_customer('Mary Willow', '10:55')
        new_waitlist.add_customer('Collins Ponds', '08:30')
        new_waitlist.add_customer('Michelle Rice', '18:45')
        assert(new_waitlist.print_reservation_list() ==  [('Collins Ponds', '08:30'), ('Mary Willow', '10:55'), ('Michelle Rice', '18:45')])

    def test_change_reservation(self):
        new_waitlist = Waitlist()
        new_waitlist.add_customer('Mary Willow', '10:55')
        new_waitlist.add_customer('Collins Ponds', '08:30')
        new_waitlist.add_customer('Michelle Rice', '18:45')
        new_waitlist.change_reservation('Mary Willow', '13:00')
        assert(new_waitlist.print_reservation_list() ==  [('Collins Ponds', '08:30'), ('Mary Willow', '13:00'), ('Michelle Rice', '18:45')])



unittest.main()
