import os
import sys
import unittest

# allow importing project modules from the parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Supplier import Supplier
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from OrderLine import OrderLine
from Order import Order
from Inventory import Inventory
from ProductFactory import ProductFactory
from DiscountStrategy import (
    DiscountStrategy,
    NoDiscount,
    PercentageDiscount,
    BulkDiscount,
    StudentDiscount,
)


def make_supplier():
    return Supplier("S001", "ACME", "acme@example.com")


class TestDiscountStrategy(unittest.TestCase):
    def test_no_discount_returns_total_unchanged(self):
        self.assertEqual(NoDiscount().apply(250), 250)

    def test_percentage_discount(self):
        self.assertAlmostEqual(PercentageDiscount(10).apply(250), 225.0)

    def test_bulk_discount_applies_over_threshold(self):
        self.assertEqual(BulkDiscount(200, 20).apply(250), 230)

    def test_bulk_discount_skips_under_threshold(self):
        self.assertEqual(BulkDiscount(200, 20).apply(150), 150)

    def test_student_discount(self):
        self.assertAlmostEqual(StudentDiscount().apply(250), 237.5)


class TestOrderUsesStrategy(unittest.TestCase):
    def setUp(self):
        self.supplier = make_supplier()
        self.product = PhysicalProduct(0.5, "P001", "Keyboard", 50.0, 20, self.supplier)

    def _order_totalling_250(self, discount=None):
        order = Order("O001", discount) if discount else Order("O001")
        order.add_order_line(self.product, 5)  # 50 * 5 = 250
        return order

    def test_default_strategy_is_no_discount(self):
        order = self._order_totalling_250()
        self.assertIsInstance(order.discount, NoDiscount)
        self.assertEqual(order.calculate_total(), 250)

    def test_order_calculates_total_through_strategy(self):
        order = self._order_totalling_250(BulkDiscount(200, 20))
        self.assertEqual(order.calculate_total(), 230)

    def test_set_discount_changes_strategy_on_existing_order(self):
        order = self._order_totalling_250(BulkDiscount(200, 20))
        self.assertEqual(order.calculate_total(), 230)
        order.set_discount(PercentageDiscount(10))
        self.assertAlmostEqual(order.calculate_total(), 225.0)

    def test_new_strategy_added_without_changing_order(self):
        # StudentDiscount is a strategy Order has never been told about
        order = self._order_totalling_250(StudentDiscount())
        self.assertAlmostEqual(order.calculate_total(), 237.5)


class TestProductFactory(unittest.TestCase):
    def setUp(self):
        self.supplier = make_supplier()

    def test_creates_physical_product(self):
        product = ProductFactory.create("physical", "P001", "Lamp", 25.0, 10, self.supplier, 2.0)
        self.assertIsInstance(product, PhysicalProduct)

    def test_creates_digital_product(self):
        product = ProductFactory.create("digital", "D001", "App", 49.9, 100, self.supplier, 500)
        self.assertIsInstance(product, DigitalProduct)

    def test_unknown_type_raises_value_error(self):
        with self.assertRaises(ValueError):
            ProductFactory.create("service", "S001", "Install", 30.0, 5, self.supplier)


class TestValidation(unittest.TestCase):
    def setUp(self):
        self.supplier = make_supplier()

    def test_price_must_be_positive(self):
        with self.assertRaises(ValueError):
            PhysicalProduct(2.0, "P001", "Lamp", -5.0, 10, self.supplier)

    def test_stock_cannot_be_negative(self):
        with self.assertRaises(ValueError):
            PhysicalProduct(2.0, "P001", "Lamp", 25.0, -1, self.supplier)

    def test_order_line_quantity_must_be_positive(self):
        product = PhysicalProduct(2.0, "P001", "Lamp", 25.0, 10, self.supplier)
        with self.assertRaises(ValueError):
            OrderLine(product, 0)


if __name__ == "__main__":
    unittest.main()
