import unittest
import graph
import trie_methods


class test_method__init__(unittest.TestCase):
    def test_normal(self):
        trie = graph.Graph()
        self.assertEqual(trie.O, [])
        self.assertEqual(trie.A, [])
        self.assertEqual(trie.dom, {})
        self.assertEqual(trie.cod, {})
        self.assertEqual(trie.sym, {})


class test_method_node(unittest.TestCase):
    # Input: string. Result: appends to O.
    # Cases: name already exists: valueerror
    # wrong type or none: typeerror
    # custom name
    # auto name
    def test_name_exists(self):
        trie = graph.Graph()
        trie.node('A')
        with self.assertRaises(ValueError):
            trie.node('A')

    def test_no_name(self):
        trie = graph.Graph()
        with self.assertRaises(TypeError):
            trie.node(None)

    def test_normal(self):
        trie = graph.Graph()
        trie.node('A')
        self.assertIn('A', trie.O)

    def test_auto(self):
        trie = graph.Graph()
        n = trie_methods.name()
        trie.node(n)
        self.assertIn(n, trie.O)


class test_method_edge(unittest.TestCase):
    # Input: string. Result: appends to A, dom, cod, sym.
    # Cases: f already is taken : valueerror
    # a or b do not exist: valueerror
    # f, a, b, or s is not a string: typeerror
    # s is not dna: valueerror
    # normal with custom names
    # normal with auto names

    def test_name_taken(self):
        trie = graph.Graph()
        trie.node('A')
        trie.node('B')
        trie.node('C')
        trie.edge('f', 'A', 'B', 'c')
        with self.assertRaises(ValueError):
            trie.edge('f', 'A', 'C', 'g')

    def node_not_exist(self):
        trie = graph.Graph()
        with self.assertRaises(ValueError):
            trie.edge('f', 'A', 'B', 'g')

    def wrong_type(self):
        trie = graph.Graph()
        trie.node('A')
        trie.node('B')
        with self.assertRaises(TypeError):
            trie.edge(None, 'A', 'B', None)

    def misspelled(self):
        trie = graph.Graph()
        trie.node('A')
        trie.node('B')
        with self.assertRaises(ValueError):
            self.edge('f', 'A', 'B', 's')

    def custom_name(self):
        trie = graph.Graph()
        trie.node('A')
        trie.node('B')
        trie.edge('f', 'A', 'B', 'a')
        self.assertIn('f', trie.A)
        self.assertTrue(trie.dom['f'] == 'A')
        self.assertTrue(trie.cod['f'] == 'B')
        self.assertTrue(trie.sym['f'] == 'a')

    def auto_name(self):
        trie = graph.Graph()
        trie.node('A')
        trie.node('B')
        f = trie_methods.name()
        trie.edge(f, 'A', 'B', 't')
        self.assertIn(f, trie.A)
        self.assertTrue(trie.dom[f] == 'A')
        self.assertTrue(trie.cod[f] == 'B')
        self.assertTrue(trie.sym[f] == 't')

if __name__ == '__main__':
    unittest.main(verbosity=2)
