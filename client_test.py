import unittest
from client3 import getDataPoint
from client3 import getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      stock = quote['stock']
      bid_price = float(quote['top_bid']['price'])
      ask_price = float(quote['top_ask']['price'])
      price = (bid_price + ask_price) / 2
      expected = stock, bid_price, ask_price, price
      self.assertEqual(expected, getDataPoint(quote))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      stock = quote['stock']
      bid_price = float(quote['top_bid']['price'])
      ask_price = float(quote['top_ask']['price'])
      price = (bid_price + ask_price) / 2
      expected = stock, bid_price, ask_price, price
      self.assertEqual(expected, getDataPoint(quote))

  """ ------------ Add more unit tests ------------ """

  def test_getRatio_calculateRatio(self):
    prices = [{'price_a': 119.2, 'price_b': 112}, {'price_a': 132.2, 'price_b': 102}]

    for price in prices:
      price_a, price_b = price["price_a"], price["price_b"]
      self.assertEqual(getRatio(price_a, price_b), price_a / price_b)

  def test_getRatio_calculateRatioWithZeros(self):
    prices = [{'price_a': 0, 'price_b': 112}, {'price_a': 132.2, 'price_b': 0}, {'price_a': 0, 'price_b': 0}]

    for price in prices:
      price_a, price_b = price["price_a"], price["price_b"]
      if price_b == 0:
        self.assertEqual(getRatio(price_a, price_b), None)
      else:
        self.assertEqual(getRatio(price_a, price_b), price_a / price_b)

if __name__ == '__main__':
    unittest.main()
