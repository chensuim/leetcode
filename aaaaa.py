class PrefixTree(object):
    def __init__(self):
        self.nodes = dict()
        self.count = dict()

    def insert(self, word, val):
        if not word:
            return
        char = word.pop()
        if char not in self.nodes:
            self.nodes[char] = PrefixTree()
            self.count[char] = 0
        self.nodes[char].insert(word,val)
        self.count[char] += val

    def sum(self, word):
        char = word.pop()
        if char not in self.nodes:
            return 0
        if word:
            return self.nodes[char].sum(word)
        else:
            return self.count[char]


class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.prefix_tree = PrefixTree()
        self.pred = dict()

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        if key in self.pred:
            self.pred[key], val = val, val - self.pred[key]
        else:
            self.pred[key] = val
        word = list(key)
        word.reverse()
        self.prefix_tree.insert(word, val)

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        word = list(prefix)
        word.reverse()
        return self.prefix_tree.sum(word)










func = None
for attr in Solution.__dict__:
    if callable(Solution.__dict__[attr]) and not attr.startswith('__'):
        func = Solution.__dict__[attr]


args = [
    7
]

print func(Solution(), *args)







