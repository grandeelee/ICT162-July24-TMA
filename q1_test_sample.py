import unittest
from datetime import datetime, timedelta
from q1 import Customer, Tour


class CustomerTest(unittest.TestCase):

    def setUp(self):
        self.today = datetime.today()
        self.customer1 = Customer('A1234567', 'John Smith', datetime(
            self.today.year - 34, self.today.month, self.today.day), 1234567890)

    def test_attributes(self):
        self.assertEqual(self.customer1.passportNumber, 'A1234567')
        self.assertEqual(self.customer1.name, 'John Smith')
        self.assertEqual(self.customer1._dob, datetime(
            self.today.year - 34, self.today.month, self.today.day))
        self.assertEqual(self.customer1.contact, 1234567890)

    def test_age(self):
        self.assertEqual(self.customer1.getAge(), 34)

    def test_contact_setter(self):
        self.customer1.contact = 9876543210
        self.assertEqual(self.customer1.contact, 9876543210)

    def test_str(self):
        self.assertEqual(str(
            self.customer1), "Passport: A1234567\tName: John Smith\tAge: 34\tContact: 1234567890")


class TourTest(unittest.TestCase):

    def setUp(self):
        self.tour1 = Tour('T1234', 'Europe Tour', 9, 7, 2500.00)

    def test_attributes(self):
        self.assertEqual(self.tour1.code, 'T1234')
        self.assertEqual(self.tour1.name, 'Europe Tour')
        self.assertEqual(self.tour1._days, 9)
        self.assertEqual(self.tour1._nights, 7)
        self.assertEqual(self.tour1.cost, 2500.00)

    def test_daysNights(self):
        self.assertEqual(self.tour1.daysNights, '9D/7N')

    def test_cost_setter(self):
        self.tour1.cost = 2750.00
        self.assertEqual(self.tour1.cost, 2750.00)

    def test_str(self):
        self.assertEqual(str(
            self.tour1), "Tour Code: T1234\tName: Europe Tour (9D/7N)\tBase Cost: $2,500.00")


if __name__ == '__main__':
    unittest.main()
