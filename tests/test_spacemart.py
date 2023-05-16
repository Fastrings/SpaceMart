import unittest
from spacemart import SpaceMart
from json_interface import get_starting_inventory

class SpaceTest(unittest.TestCase):
    
    def setUp(self):
        self.mart = SpaceMart(100000)
    
    def test_init_properly(self):
        self.assertEqual(len(self.mart.products), 200)
        self.assertDictEqual(self.mart.current_report, {})
        self.assertEqual(self.mart.budget, 100000)
        self.assertEqual(self.mart.days, 1)
    
    def test_time_passed(self):
        self.mart.add_time(10)
        self.assertEqual(self.mart.get_time_passed(), 11)
    
    def test_budget(self):
        self.assertEqual(self.mart.get_budget(), 100000)

    def test_taxes(self):
        self.assertEqual(self.mart.budget, 100000)
        self.mart.pay_taxes()
        self.assertEqual(self.mart.budget, -50000)
    
    def test_init_products(self):
        self.assertEqual(len(self.mart.products), 200)
        item1, item2, item3 = self.mart.products[50], self.mart.products[100], self.mart.products[150]
        self.mart.init_products(get_starting_inventory())
        self.assertEqual(len(self.mart.products), 200)
        self.assertNotEqual(item1, self.mart.products[50])
        self.assertNotEqual(item2, self.mart.products[100])
        self.assertNotEqual(item3, self.mart.products[150])

    def test_making_money(self):
        bud = self.mart.get_budget()
        self.assertEqual(self.mart.total_sales(), 0)
        report = self.mart.calculate_sales()
        self.mart.update_report(report)
        self.assertNotEqual(self.mart.total_sales(), 0)
        self.mart.make_money()
        self.assertEqual(self.mart.get_budget(), bud + self.mart.total_sales())

    def test_restock(self):
        for p in self.mart.products:
            self.assertEqual(p['quantity'], 5)
        report = self.mart.calculate_sales()
        count = 0
        for p in self.mart.products:
            count += p['quantity'] != 5
        self.assertGreater(count, 0)
        self.mart.restock()
        for p in self.mart.products:
            self.assertEqual(p['quantity'], 5)

    def test_discounts(self):
        for p in self.mart.products:
            self.assertEqual(p['discount'], 0)
        self.mart.apply_discounts()
        count = 0
        for p in self.mart.products:
            count += p['discount'] != 0
        self.assertGreater(count, 0)

    def test_expiry_dates(self):
        for p in self.mart.products:
            self.assertGreaterEqual(p['remaining_days'], 5)
        
        for _ in range(10):
            self.mart.add_time()
            self.mart.update_expiry_date()
            self.mart.throw_expired()
        
        self.mart.throw_expired()
        
        self.assertNotEqual(len(self.mart.products), 200)

        for p in self.mart.products:
            self.assertNotEqual(p['remaining_days'], -3)
            if p['remaining_days'] <= 0:
                self.assertEqual(p['discount'], 50)
            