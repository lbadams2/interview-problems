import unittest
from node import Node, Purchase

class TestNodeMethods(unittest.TestCase):

    def setUp(self):
        self.root = Node('root', 'root')
        self.keys = ['publisher', 'duration', 'price']

    def test_insert(self):
        val0 = ['Pearson', '*', 5]
        val1 = ['Pearson', '10_day', 6]
        val2 = ['Openstax', '10_day', 6]
        val3 = ['Openstax', '10_day', 6]
        val4 = ['*', '*', '*']
        self.root.insert(self.keys, val0, 0)
        self.root.insert(self.keys, val1, 1)
        self.root.insert(self.keys, val2, 2)
        self.root.insert(self.keys, val3, 3)
        self.root.insert(self.keys, val4, 4)

    def test_add_purchase_root(self):
        purchase1 = Purchase(34534, 546546456, 'Pearson', 'CLT', 6, '10_day', '2017-10-02')
        purchase2 = Purchase(34534, 546546456, 'Pearson', 'CLT', 5, '10_day', '2017-10-02')


if __name__ == '__main__':
    unittest.main()