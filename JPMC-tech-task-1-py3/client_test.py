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
    for x in quotes:
      stock, bid_price, ask_price, price = getDataPoint(x)
      self.assertEqual(stock, x['stock'])
      self.assertEqual(bid_price, x['top_bid']['price'])
      self.assertEqual(ask_price, x['top_ask']['price'])
      self.assertEqual(price, (x['top_bid']['price'] + x['top_ask']['price'])/2)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for x in quotes:
      stock, bid_price, ask_price, price = getDataPoint(x)
      self.assertEqual(stock, x['stock'])
      self.assertEqual(bid_price, x['top_bid']['price'])
      self.assertEqual(ask_price, x['top_ask']['price'])
      self.assertEqual(price, (x['top_bid']['price'] + x['top_ask']['price'])/2)

  """ ------------ Add more unit tests ------------ """
  def test_getDataPoint_calculateRatio(self):
    quotes = [
      {'top_ask': {'price': 120.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 156.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 98.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    prices={}
  
    for x in quotes:
      stock, bid_price, ask_price, price = getDataPoint(x)
      prices[stock] = price

    self.assertEqual(getRatio(prices['ABC'], prices['DEF']), (prices['ABC']/prices['DEF']))






if __name__ == '__main__':
    unittest.main()
