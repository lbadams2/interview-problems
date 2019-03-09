class Purchase:
    def __init__(self, order_id, isbn, publisher, school, price, duration, order_datetime):
        self.order_id = order_id
        self.isbn = isbn
        self.publisher = publisher
        self.school = school
        self.price = price
        self.duration = duration
        self.order_datetime = order_datetime

    def __lt__(self, other):
        if isinstance(other, Purchase):
            return self.order_id < other.order_id

    def __str__(self):
        return str(self.order_id) + ',' + str(self.isbn) + ',' + str(self.publisher) + ',' + str(self.school) + \
            ',' + str(self.price) + ',' + str(self.duration) + ',' + str(self.order_datetime)


class Node_Json:
    def __init__(self, bucket_str, purchases):
        self.bucket = bucket_str
        self.purchases = purchases


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.children = set()
        self.purchases = []
        self.valid_keys = ['root', 'publisher', 'duration', 'price']
        self.creation_order = []


    def get_leaf_nodes(self, bucket_list, path):
        if not self.children:
            i = 0
            path.append(self.value)
            path_str = ','.join(path)            
            for instance in self.creation_order:
                if i == 0:
                    purchase_strs = [p.__str__() for p in self.purchases]
                    node_json = Node_Json(path_str, purchase_strs)
                    bucket_list[instance] = node_json
                    i = i + 1
                else:
                    node_json = Node_Json(path_str, [])
                    bucket_list[instance] = node_json
            return

        else:
            for child in self.children:
                branch = path.copy()
                if self.value != 'root':
                    branch.append(self.value)
                child.get_leaf_nodes(bucket_list, branch)    


    def insert(self, keys, vals, bucket_num):
        if not vals:
            return

        node = Node(keys[0], vals[0])
        if len(keys) == 1:
            node.creation_order.append(bucket_num)
        
        if not self.children:
            self.children.add(node)
            node.insert(keys[1:], vals[1:], bucket_num)
        else:   
            if node in self.children:
                for child in self.children:
                    if child == node:           
                        child.insert(keys[1:], vals[1:], bucket_num)
                        break
            else:
                self.children.add(node)
                node.insert(keys[1:], vals[1:], bucket_num)


    def add_purchase_root(self, purchase, keys, vals, matches):
        tmp = Node(keys[0], vals[0])
        if tmp in self.children:
            for child in self.children:
                if vals[0].lower() == child.value.lower():
                    if vals[0] != '*':
                        matches = matches + 1
                    if len(vals) == 1:
                        return child, matches
                    else:
                        ret_val = child.add_purchase_root(purchase, keys[1:], vals[1:], matches)
                        if not ret_val:
                            # break to back track and try wild card
                            break
                        return ret_val
            # if this line is reached val matched key but no child matched
            # try wild card to see if it has a matching child
            wild_tmp = Node(keys[0], '*')
            if wild_tmp in self.children:
                for child in self.children:
                    if '*' == child.value:
                        return child.add_purchase_root(purchase, keys[1:], vals[1:], matches)
            else:
                return None
        
        else:
            wild_card = Node(keys[0], '*')
            if wild_card in self.children:
                for child in self.children:
                    if child == wild_card:
                        if len(vals) == 1:
                            return child, matches
                        else:
                            return child.add_purchase_root(purchase, keys[1:], vals[1:], matches)
            else:
                return None

    def add_purchase_node(self, purchase):
        self.purchases.append(purchase)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.value.lower() == other.value.lower() and self.key == other.key
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.value.lower() < other.value.lower()

    def __hash__(self):
        return self.value.lower().__hash__() * self.key.__hash__()