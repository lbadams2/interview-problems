import unittest
from unittest.mock import patch, mock_open
import fill_buckets
from node import Node, Purchase
import builtins

class TestFillBucketMethods(unittest.TestCase):
    
    def setUp(self):
        self.purchases = []
        self.purchases.append(Purchase(34534, 546546456, 'Pearson', 'CLT', '6', '10_day', '2017-10-02'))
        self.purchases.append(Purchase(34534, 546546456, 'Pearson', 'CLT', '5', '10_day', '2017-10-02'))
        self.purchases.append(Purchase(34534, 546546456, 'Pearson', 'CLT', '8', '20_day', '2017-10-02'))
        self.purchases.append(Purchase(34534, 546546456, 'aisudha', 'CLT', '8', '20_day', '2017-10-02'))
        #with patch("builtins.open", mock_open(read_data=purchases)) as mock_file:
        self.root = Node('root', 'root')
        self.keys = ['publisher', 'duration', 'price']

    #@patch("builtins.open", new_callable=mock_open, read_data=self.purchases)
    #def test_fill_buckets(self):
    #    fill_buckets.fill_buckets(self.root)

    def test_fill_buckets(self):
        mock_open_fn = mock_open(read_data=self.purchases)
        with patch('builtins.open', mock_open_fn):
            fill_buckets.fill_buckets(self.root)
            print('sdkfjnksdjn')


if __name__ == '__main__':
    unittest.main()