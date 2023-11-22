import unittest
import pytest
from unittest.mock import patch
from unittest.mock import MagicMock
from src.models.orders import Orders


class TestOrders(unittest.TestCase):

    def setUp(self) -> None:
        self.orders = Orders()

    def test_read_file(self):
        json_file = self.orders.read_file()
        self.assertIsInstance(json_file, dict)


