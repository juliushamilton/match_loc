import unittest
import trie_builder
import graph
import trie_methods


class test_method_PrefixTrieConstruction(unittest.TestCase):
    # takes a list of patterns and returns a prefix trie
    # Cases: no input or wrong type -> typeerror
    # empty list -> valueerror
    # not dna -> value error
    # a string -> value error
    # multichar, single pattern -> expected trie
    # singlechar, multipattern -> expected trie

    def test_wrong_input(self):
        patterns = None
        with self.assertRaises(TypeError):
            trie_builder.PrefixTrieConstruction(patterns)

    def test_flawed_input(self):
        patterns = []
        with self.assertRaises(ValueError):
            trie_builder.PrefixTrieConstruction(patterns)

    def test_misspelled_input(self):
        patterns = ['cgeta']
        with self.assertRaises(ValueError):
            trie_builder.PrefixTrieConstruction(patterns)

    def test_no_list(self):
        patterns = 'gtccaaa'
        with self.assertRaises(TypeError):
            trie_builder.PrefixTrieConstruction(patterns)

    def test_multichar(self):
        patterns = ['ac']
        trie = graph.Graph()
        trie.node('A')
        trie.node('B')
        trie.node('C')
        trie.edge('f', 'A', 'B', 'a')
        trie.edge('g', 'B', 'C', 'c')
        expected = trie_builder.PrefixTrieConstruction(patterns)
        val = trie_methods.trie_equivalence(trie, expected)
        self.assertTrue(val)

    def test_normal_2(self):
        patterns = ['t', 'a']
        trie = graph.Graph()
        trie.node('A')
        trie.node('B')
        trie.node('C')
        trie.edge('f', 'A', 'B', 't')
        trie.edge('g', 'A', 'C', 'a')
        expected = trie_builder.PrefixTrieConstruction(patterns)
        val = trie_methods.trie_equivalence(trie, expected)
        self.assertTrue(val)

    def test_complex(self):
        patterns = ['cga', 'cg', 'gta']
        trie = graph.Graph()
        trie.node('A')
        trie.node('B')
        trie.node('C')
        trie.node('D')
        trie.node('E')
        trie.node('F')
        trie.node('G')
        trie.edge('f', 'A', 'B', 'c')
        trie.edge('g', 'B', 'C', 'g')
        trie.edge('h', 'C', 'D', 'a')
        trie.edge('i', 'A', 'E', 'g')
        trie.edge('j', 'E', 'F', 't')
        trie.edge('k', 'F', 'G', 'a')

        expected = trie_builder.PrefixTrieConstruction(patterns)
        val = trie_methods.trie_equivalence(trie, expected)
        self.assertTrue(val)


class test_method_incorporate(unittest.TestCase):
    # Input: text, trie. Output: trie
    # Assuming text and trie are valid and correct:
    # Cases: text matches trie: no alteration
    # text differs: specify alteration
    def test_differ(self):
        pattern = 'cg'
        trie = graph.Graph()
        trie.node('A')
        trie.node('B')
        trie.node('C')
        trie.edge('f', 'A', 'B', 'c')
        trie.edge('g', 'B', 'C', 'g')

        expected = graph.Graph()
        expected = trie_builder.incorporate(pattern, expected)

        val = trie_methods.trie_equivalence(trie, expected)
        self.assertTrue(val)

    def test_same(self):
        pattern = 'cg'
        trie = graph.Graph()
        trie.node('A')
        trie.node('B')
        trie.node('C')
        trie.edge('f', 'A', 'B', 'c')
        trie.edge('g', 'B', 'C', 'g')

        expected = trie_builder.incorporate(pattern, trie)

        val = trie_methods.trie_equivalence(expected, trie)
        self.assertTrue(val)


class test_method_is_prefix(unittest.TestCase):
    # Input: text, trie. Output: True / False.
    def test_wrong_text(self):
        text = None
        patterns = ['a']
        trie = trie_builder.PrefixTrieConstruction(patterns)
        with self.assertRaises(TypeError):
            trie_builder.is_prefix(text, trie)

    def test_normal(self):
        text = 'agtgggg'
        patterns = ['ag']
        trie = trie_builder.PrefixTrieConstruction(patterns)
        val = trie_builder.is_prefix(text, trie)
        self.assertTrue(val)

    def test_false(self):
        text = 'ccca'
        patterns = ['ca', 'gt']
        trie = trie_builder.PrefixTrieConstruction(patterns)
        val = trie_builder.is_prefix(text, trie)
        self.assertFalse(val)


class test_method_match_loc(unittest.TestCase):
    # Input: text, trie. Output: set of integral locations.
    def test_normal(self):
        text = 'acgta'
        patterns = ['cg', 'gta']
        trie = trie_builder.PrefixTrieConstruction(patterns)
        val = trie_builder.match_loc(text, trie)
        self.assertEqual(val, [1, 2])

if __name__ == '__main__':
    unittest.main(verbosity=2)
