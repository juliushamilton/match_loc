import unittest
import trie_methods
import graph
import trie_builder

class test_method_is_gen(unittest.TestCase):
    # Input: string. Output: true / false
    # Cases: not a string : type error
    # dna : true
    # not dna : false

    def test_not_string(self):
        s = None
        with self.assertRaises(TypeError):
            trie_methods.is_gen(s)

    def test_true(self):
        s = 'cga'
        val = trie_methods.is_gen(s)
        self.assertTrue(val)

    def test_false(self):
        s = 'tge'
        val = trie_methods.is_gen(s)
        self.assertFalse(val)

class test_method_name(unittest.TestCase):
    #Output: random string of six characters
    def test_normal(self):
        s = trie_methods.name()
        self.assertIsInstance(s, str)
        self.assertEqual(len(s), 6)

class test_method_edge_exists(unittest.TestCase):
    # input: s, x, trie; output: true/false
    def test_method_true(self):
        s = 'c'
        x = 'A'
        trie = graph.Graph()
        trie.node('A')
        trie.node('B')
        trie.edge('f', 'A', 'B', 'c')
        val = trie_methods.edge_exists(s, x, trie)
        self.assertTrue(val)

    def test_method_false(self):
        s = 'c'
        x = 'A'
        trie = graph.Graph()
        trie.node('A')
        trie.node('B')
        trie.node('C')
        trie.edge('f', 'A', 'B', 'g')
        trie.edge('g', 'A', 'C', 't')

        val = trie_methods.edge_exists(s, x, trie)
        self.assertFalse(val)

class test_method_select(unittest.TestCase):
    def test_method_normal(self):
        s = 'c'
        x = 'A'
        trie = graph.Graph()
        trie.node('A')
        trie.node('B')
        trie.node('C')
        trie.node('D')
        trie.node('E')
        trie.edge('f', 'A', 'B', 'a')
        trie.edge('g', 'A', 'C', 'c')
        trie.edge('h', 'A', 'D', 'g')
        trie.edge('i', 'B', 'E', 'c')
        e = trie_methods.select(s, x, trie)
        self.assertEqual(e, 'g')

class test_method_root(unittest.TestCase):
    # Input: trie Output: node
    # Cases where this could go wrong?
    def test_method_normal(self):
        trie = graph.Graph()
        trie.node('A')
        trie.node('B')
        trie.node('C')
        trie.node('D')
        trie.node('E')
        trie.edge('f', 'A', 'B', 'a')
        trie.edge('g', 'A', 'C', 'c')
        trie.edge('h', 'B', 'D', 'a')
        trie.edge('i', 'C', 'E', 'g')
        r = trie_methods.root(trie)
        self.assertEqual(r, 'A')
    def test_single_node(self):
        trie = graph.Graph()
        trie.node('A')
        r = trie_methods.root(trie)
        self.assertEqual(r, 'A')
    def test_empty_trie(self):
        trie = graph.Graph()
        with self.assertRaises(ValueError):
            trie_methods.root(trie)

    def test_wrong_input(self):
        trie = None
        with self.assertRaises(TypeError):
            trie_methods.root(trie)




class test_method_trie_equivalence(unittest.TestCase):
    # Input: trie1, trie2. Output: true / false
    def test_normal(self):
        p1 = ['ag', 'ct', 'tt']
        p2 = ['tt', 'ct', 'ag']
        tr1 = trie_builder.PrefixTrieConstruction(p1)
        tr2 = trie_builder.PrefixTrieConstruction(p2)
        val = trie_methods.trie_equivalence(tr1, tr2)
        self.assertTrue(val)

class test_method_num_leaves(unittest.TestCase):
    # input: trie. output: int
    # Cases: single node : 1
    # two branches: 2
    # three complicated branches: 3

    def test_method_single(self):
        trie = graph.Graph()
        trie.node('A')
        val = trie_methods.num_leaves(trie)
        self.assertEqual(val, 1)

    def test_method_double(self):
        trie = graph.Graph()
        trie.node('A')
        trie.node('B')
        trie.edge('f', 'A', 'B', 'g')
        val = trie_methods.num_leaves(trie)
        self.assertEqual(val, 1)

    def test_method_complex(self):
        trie = graph.Graph()
        trie.node('A')
        trie.node('B')
        trie.edge('f', 'A', 'B', 'g')
        trie.node('C')
        trie.node('D')
        trie.node('E')
        trie.edge('g', 'B', 'C', 't')
        trie.edge('h', 'B', 'D', 'a')
        trie.edge('i', 'A', 'E', 'c')
        val = trie_methods.num_leaves(trie)
        self.assertEqual(val, 3)


class test_method_arrived(unittest.TestCase):
    def test_normal(self):
        x = 'B'
        trie = graph.Graph()
        trie.node('A')
        trie.node('B')
        trie.edge('f', 'A', 'B', 'c')
        val = trie_methods.arrived(x, trie)
        self.assertTrue(val)

    def test_false(self):
        x = 'A'
        trie = graph.Graph()
        trie.node('A')
        trie.node('B')
        trie.edge('f', 'A', 'B', 'c')
        val = trie_methods.arrived(x, trie)
        self.assertFalse(val)

class test_method_num_edges(unittest.TestCase):
    def test_normal(self):
        trie = graph.Graph()
        trie.node('A')
        trie.node('B')
        trie.node('C')
        trie.edge('f', 'A', 'B', 'c')
        trie.edge('g', 'A', 'C', 't')

        val = trie_methods.num_edges(trie)
        self.assertEqual(val, 2)


if __name__ == '__main__':
    unittest.main(verbosity = 2)