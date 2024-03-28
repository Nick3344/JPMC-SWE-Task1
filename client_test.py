import unittest
from client3 import getDataPoint


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        stock, bid_price, ask_price, price = getDataPoint(quotes[0])
        expected_price = (bid_price + ask_price) / 2  # Calculate average price
        self.assertEqual(price, expected_price)

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        stock, bid_price, ask_price, price = getDataPoint(quotes[0])
        expected_price = (bid_price + ask_price) / 2  # Calculate average price
        self.assertEqual(price, expected_price)

    def test_getDataPoint_emptyQuotes(self):
        quotes = []
        # Assert that an exception is raised or handle empty quotes appropriately
        with self.assertRaises(Exception):  # Replace Exception with specific exception if expected
            getDataPoint(quotes)

    def test_getDataPoint_invalidPrice(self):
        quotes = [
            {'top_ask': {'price': "invalid_price"}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48}, 'id': '0.109974697771', 'stock': 'ABC'}
        ]
        # Assert that the function handles invalid price data (e.g., non-numeric)
        with self.assertRaises(Exception):  # Replace Exception with specific exception if expected
            getDataPoint(quotes[0])



if __name__ == '__main__':
    unittest.main()
