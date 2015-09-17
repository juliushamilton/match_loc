import unittest
import match_loc
import sys
import fasta

class test_method_parse(unittest.TestCase):
    # Input: commands line args. Output: text, patterns

    def test_misspelled_pattern(self):
        sys.argv = ['botulism.fasta.txt', 'gttttggacc', 'gttcgs']
        with self.assertRaises(ValueError):
            match_loc.parse()

    def test_single_files(self):
        n1 = 'genome.fasta.txt'
        n2 = 'ribosome.fasta.txt'
        t1 = 'acgttcagctacgatcgactacgactagctacgactacgactacg'
        t2 = 'gtcacta'
        fasta.make_sample_fasta(n1, t1)
        fasta.make_sample_fasta(n2, t2)

        sys.argv = [sys.argv[0], n1, n2]
        text, patterns = match_loc.parse()
        self.assertEqual(text, t1)
        self.assertEqual(patterns, [t2])

    def test_multiple_strings(self):
        t1 = 'acgtacgactacgactacgactacgact'
        t2 = 'tcgc'
        t3 = 'acg'
        t4 = 'actgg'

        sys.argv = [sys.argv[0], t1, t2, t3, t4]

        text, patterns = match_loc.parse()
        self.assertEqual(text, t1)
        self.assertEqual(patterns, [t2, t3, t4])

class test_method_main(unittest.TestCase):
    def test_normal(self):
        t1 = 'cgtcga'
        t2 = 'ga'
        sys.argv = [sys.argv[0], t1, t2]

        val = match_loc.main()

        self.assertEqual(val, [4])


if __name__ == '__main__':
    unittest.main(verbosity = 2)
