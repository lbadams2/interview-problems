import csv
import json
from node import Node, Purchase

# Create a tree in which a path forms a bucket.  Goes from publisher to duration to price as
# you get deeper in the tree.  A path from publisher to price forms a bucket, purchases are stored 
# in the price(leaf) nodes. The tree has an arbitrary root node to serve as a parent for every
# publisher subtree.
def create_buckets():
    keys = ['publisher', 'duration', 'price']
    num_buckets = 0
    root = Node('root', 'root')
    with open('purchase_buckets.csv', newline='') as pb_file:
        bucket_reader = csv.reader(pb_file, delimiter=',')
        for row in bucket_reader:            
            vals = [row[0], row[2], row[1]]
            root.insert(keys, vals, num_buckets)
            num_buckets = num_buckets + 1

    # if uncategorized bucket wasn't in file create it now
    if not root.get_bucket(keys, ['*', '*', '*']):
            root.insert(keys, ['*', '*', '*'], num_buckets)        
            num_buckets = num_buckets + 1
    return root, num_buckets


# Add each purchase to tree
def fill_buckets(root):
    keys = ['publisher', 'duration', 'price']
    with open('purchase_data.csv', newline='') as data_file:
        data_reader = csv.reader(data_file, delimiter=',')
        for row in data_reader:
            purchase = Purchase(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            vals = [purchase.publisher, purchase.duration, purchase.price]
            # add purchase root will not actually add the purchase, just return node it would be added to
            # and the number of matches so we can compare to other paths with wild cards.
            return_tuple = root.add_purchase_root(purchase, keys, vals, 0)
            
            node = return_tuple[0]
            matches = return_tuple[1]
            # if wild card used and only one match try leading wild card to see if it returns 2 matches
            if node.value == '*' and matches == 1:
                second_tuple = root.add_purchase_root(purchase, keys, ['*', purchase.duration, purchase.price], 0)
                if second_tuple and second_tuple[1] > matches:
                    second_node = second_tuple[0]
                    second_node.add_purchase_node(purchase)
                else:
                    node.add_purchase_node(purchase)
            else:
                node.add_purchase_node(purchase)


def create_json(bucket_list_json):
    json_str = json.dumps([nj.__dict__ for nj in bucket_list_json], indent=4)
    with open('output.json', 'w') as out:
        out.write(json_str)


def run():
    # create tree
    return_tuple = create_buckets()
    root = return_tuple[0]
    num_buckets = return_tuple[1]
    # fill tree with purchases
    fill_buckets(root)
    bucket_list_json = [None] * num_buckets
    # get purchases in json serializable objects
    root.get_leaf_nodes(bucket_list_json, [])
    # generate json file
    create_json(bucket_list_json)

run()