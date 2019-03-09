import unittest
from node import Node, Purchase

class TestNodeMethods(unittest.TestCase):

    def setUp(self):
        self.root = Node('root', 'root')
        self.keys = ['publisher', 'duration', 'price']

    def test_insert(self):
        val0 = ['Pearson', '*', '5']
        val1 = ['Pearson', '10_day', '6']
        val2 = ['Openstax', '10_day', '6']
        val3 = ['Openstax', '10_day', '6']
        val4 = ['*', '*', '*']
        self.root.insert(self.keys, val0, 0)
        self.root.insert(self.keys, val1, 1)
        self.root.insert(self.keys, val2, 2)
        self.root.insert(self.keys, val3, 3)
        self.root.insert(self.keys, val4, 4)
        
        self.assertTrue(Node('publisher', 'Pearson') in self.root.children)
        self.assertTrue(Node('publisher', 'Openstax') in self.root.children)
        self.assertTrue(Node('publisher', '*') in self.root.children)

        tmp = Node('publisher', 'Pearson')
        for child in self.root.children:
            if child == tmp:
                tmp2 = Node('duration', '*')
                tmp3 = Node('duration', '10_day')
                self.assertTrue(tmp2 in child.children)
                self.assertTrue(tmp3 in child.children)
                for grand_child in child.children:
                    if tmp2 == grand_child:
                        self.assertTrue(Node('price', '5') in grand_child.children)
                    elif tmp3 == grand_child:
                        self.assertTrue(Node('price', '6') in grand_child.children)
                break

    def test_add_purchase_root(self):
        val0 = ['Pearson', '*', '5']
        val1 = ['Pearson', '10_day', '6']
        val2 = ['Pearson', '*', '*']
        val3 = ['*', '*', '*']
        self.root.insert(self.keys, val0, 0)
        self.root.insert(self.keys, val1, 1)
        self.root.insert(self.keys, val2, 2)
        self.root.insert(self.keys, val3, 3)
        purchase1 = Purchase(34534, 546546456, 'Pearson', 'CLT', '6', '10_day', '2017-10-02')
        purchase2 = Purchase(34534, 546546456, 'Pearson', 'CLT', '5', '10_day', '2017-10-02')
        purchase3 = Purchase(34534, 546546456, 'Pearson', 'CLT', '8', '20_day', '2017-10-02')
        purchase4 = Purchase(34534, 546546456, 'aisudha', 'CLT', '8', '20_day', '2017-10-02')
        ret_tup = self.root.add_purchase_root(purchase1, self.keys, [purchase1.publisher, \
                                                            purchase1.duration, purchase1.price], 0)
        self.assertTrue(Node('price', '6') == ret_tup[0])
        self.assertEqual(3, ret_tup[1])

        ret_tup = self.root.add_purchase_root(purchase2, self.keys, [purchase2.publisher, \
                                                            purchase2.duration, purchase2.price], 0)
        self.assertTrue(Node('price', '5') == ret_tup[0])
        self.assertEqual(2, ret_tup[1])

        ret_tup = self.root.add_purchase_root(purchase3, self.keys, [purchase3.publisher, \
                                                            purchase3.duration, purchase3.price], 0)
        self.assertTrue(Node('price', '*') == ret_tup[0])
        self.assertEqual(1, ret_tup[1])

        ret_tup = self.root.add_purchase_root(purchase4, self.keys, [purchase4.publisher, \
                                                            purchase4.duration, purchase4.price], 0)
        self.assertTrue(Node('price', '*') == ret_tup[0])
        self.assertEqual(0, ret_tup[1])

    
    def test_get_leaf_nodes(self):
        val0 = ['Pearson', '*', '5']
        val1 = ['Pearson', '10_day', '6']
        val2 = ['Pearson', '10_day', '6']
        val3 = ['Pearson', '*', '*']
        val4 = ['*', '*', '*']
        self.root.insert(self.keys, val0, 0)
        self.root.insert(self.keys, val1, 1)
        self.root.insert(self.keys, val2, 2)
        self.root.insert(self.keys, val3, 3)
        self.root.insert(self.keys, val4, 4)
        purchase1 = Purchase(34534, 546546456, 'Pearson', 'CLT', '6', '10_day', '2017-10-02')
        purchase2 = Purchase(34534, 546546456, 'Pearson', 'CLT', '5', '10_day', '2017-10-02')
        purchase3 = Purchase(34534, 546546456, 'Pearson', 'CLT', '8', '20_day', '2017-10-02')
        purchase4 = Purchase(34534, 546546456, 'aisudha', 'CLT', '8', '20_day', '2017-10-02')
        
        ret_tup = self.root.add_purchase_root(purchase1, self.keys, [purchase1.publisher, \
                                                            purchase1.duration, purchase1.price], 0)
        ret_tup[0].add_purchase_node(purchase1)
        
        ret_tup = self.root.add_purchase_root(purchase2, self.keys, [purchase2.publisher, \
                                                            purchase2.duration, purchase2.price], 0)
        ret_tup[0].add_purchase_node(purchase2)
        
        ret_tup = self.root.add_purchase_root(purchase3, self.keys, [purchase3.publisher, \
                                                            purchase3.duration, purchase3.price], 0)
        ret_tup[0].add_purchase_node(purchase3)

        ret_tup = self.root.add_purchase_root(purchase4, self.keys, [purchase4.publisher, \
                                                            purchase4.duration, purchase4.price], 0)
        ret_tup[0].add_purchase_node(purchase4)
        
        leaf_node_list = [None] * 5
        self.root.get_leaf_nodes(leaf_node_list, [])
        
        bucket_str_1 = 'Pearson,*,5'
        bucket_str_2 = 'Pearson,10_day,6'
        bucket_str_3 = 'Pearson,*,*'
        bucket_str_4 = '*,*,*'        
        
        self.assertEqual(bucket_str_1, leaf_node_list[0].bucket)
        self.assertEqual(1, len(leaf_node_list[0].purchases))

        self.assertEqual(bucket_str_2, leaf_node_list[1].bucket)
        self.assertEqual(1, len(leaf_node_list[1].purchases))

        self.assertEqual(bucket_str_2, leaf_node_list[2].bucket)
        self.assertEqual(0, len(leaf_node_list[2].purchases))

        self.assertEqual(bucket_str_3, leaf_node_list[3].bucket)
        self.assertEqual(1, len(leaf_node_list[3].purchases))

        self.assertEqual(bucket_str_4, leaf_node_list[4].bucket)
        self.assertEqual(1, len(leaf_node_list[4].purchases))


if __name__ == '__main__':
    unittest.main()