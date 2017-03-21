from collections import defaultdict

class SuffixTree(object):
    def __init__(self, key=None):
        self.key = key
        self.dict = {
                'count': 0,
                'children': {}
                }

    def __getitem__(self, key):
        if key == 'count':
            return self.dict['count']

        return self.dict['children'][key]

    def __setitem__(self, key, value):
        if key == 'count':
            self.dict['count'] = value
        else:
            self.dict['children'].setdefault(key, SuffixTree(key))

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.dict)

    def keys(self):
        return self.children.keys()

    @property
    def count(self):
        return self.dict['count']

    @property
    def children(self):
        return self.dict['children']

    @classmethod
    def from_seq(klass, seq):
        inf = SuffixTree()

        for i in range(len(seq)):
            node = inf

            for token in seq[i:]:
                node[token]['count'] += 1
                node = node[token].children

            node['$']['count'] += 1

        return inf

    def all_keys(self):
        paths = []
        for key in self.keys():
            if key == '$':
                paths.append(['$'])
            else:
                node = self[key]

                future_paths = node.all_keys()
                for path in future_paths:
                    paths.append([key, *path])

        return paths

    @property
    def is_leaf(self):
        return len(self.dict['children']) <= 1

    def flattened_items(self):
        results = set()
        for k, v in self.children.items():
            results.add(((k, ), v.count))

        return results
