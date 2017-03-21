import unittest
from suffix_tree import SuffixTree
from expects import *

class TestSuffixTree(unittest.TestCase):
    def test_single_suffix_tree(self):
        tree = SuffixTree.from_seq(['a'])

        expect(tree['a'].count).to(equal(1))
        expect(tree['b'].count).to(equal(0))
        expect(tree['a']['$'].count).to(equal(1))

    def test_two_elements_in_tree(self):
        tree = SuffixTree.from_seq(['a', 'a'])
        expect(tree['a'].count).to(equal(2))
        expect(tree['a']['a'].count).to(equal(1))

    def test_elements_are_reversed(self):
        tree = SuffixTree.from_seq(['a', 'a', 'b'])
        expect(tree['a']['b'].count).to(equal(1))
        expect(tree['b']['a'].count).to(equal(0))

    def test_get_depth_tuples(self):
        tree = SuffixTree.from_seq(['a', 'a', 'b'])
        expect(tree.items()).to(equal(set((
            (('a', '$'), 2),
            (('a', 'a', '$'), 1),
            (('a', 'a', 'b', '$'), 1),
            (('a', 'b', '$'), 1),
            (('b', '$'), 1),
            ))))

