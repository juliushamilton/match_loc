import unittest
import fasta
import match_loc.py


class test_method_is_fasta(unittest.TestCase):
    # Input: string, '.fasta.txt'. Output: Boolean
    def test_int(self):
        name = 1
        with self.assertRaises(TypeError):
            fasta.is_fasta(name)

    def test_none(self):
        name = None
        with self.assertRaises(TypeError):
            fasta.is_fasta(name)

    def test_not_fasta(self):
        name = 'aacgtc'
        val = fasta.is_fasta(name)
        self.assertEqual(val, False)

    def test_not_fasta_long(self):
        name = 'aaaaaaaaaaaaaaaaaaaaaaaa'
        val = fasta.is_fasta(name)
        self.assertEqual(val, False)
        
    def test_normal(self):
        name = 'spirulina.fasta.txt'
        val = fasta.is_fasta(name)
        self.assertEqual(val, True)

class test_method_open_fasta(unittest.TestCase):
	# Input: fasta filename. Output: the text within.
    def test_not_string(self):
        file_name = None
        with self.assertRaises(TypeError):
            fasta.open_fasta(file_name)
    def test_not_fasta(self):
        file_name = 'tacgtgacggg'
        with self.assertRaises(ValueError):
            fasta.open_fasta(file_name)
    def test_normal(self):
        file_name = 'spirulina_ribosome.fasta.txt'
        text = 'ccgccgtagattt'
        fasta.make_sample_fasta(file_name, text)

        val = fasta.open_fasta(file_name)
        self.assertEqual(val, text)

class test_method_make_sample_fasta(unittest.TestCase):
    def test_wrong_name(self):
        file_name = None
        text = 'cgtt'
        with self.assertRaises(TypeError):
            fasta.make_sample_fasta(file_name, text)

    def test_wrong_text(self):
        file_name = 'apple'
        text = None
        with self.assertRaises(TypeError):
            fasta.make_sample_fasta(file_name, text)

    def test_not_fasta(self):
        file_name = 'spirulina'
        text = 'cgta'
        with self.assertRaises(ValueError):
            fasta.make_sample_fasta(file_name, text)

    def test_normal(self):
        file_name = 'spirulina_ribosome.fasta.txt'
        text = 'cgtgatcgatcgttactac'

        val = fasta.make_sample_fasta(file_name, text)

        self.assertEqual(fasta.open_fasta(file_name), text)

class test_method_convert_to_text(unittest.TestCase):
	# Takes a list of strings and fasta filenames
	# or a single string or fasta filename
	# and returns with fasta filenames replaced with
	# their texts.
    def test_wrong_input(self):
        input = None
        with self.assertRaises(TypeError):
            fasta.convert_to_text(input)
    def test_string(self):
        input = 'cgtgaggcgtattt'
        val = fasta.convert_to_text(input)
        self.assertEqual(val, input)

    def test_filename(self):
        file_name = 'spirulina.fasta.txt'
        text = 'cgtacgtacgtaa'
        fasta.make_sample_fasta(file_name, text)

        val = fasta.convert_to_text(file_name)
        self.assertEqual(val, text)

    def test_list(self):
        name_1 = 's.fasta.txt'
        name_2 = 't.fasta.txt'
        text_1 = 'cgtagtc'
        text_2 = 'ccccccccc'
        fasta.make_sample_fasta(name_1, text_1)
        fasta.make_sample_fasta(name_2, text_2)
        l = [name_1, name_2, 'aaa']

        val = fasta.convert_to_text(l)
        self.assertEqual(val, [text_1, text_2, 'aaa'])

class test_method_is_gen(unittest.TestCase):
    def test_not(self):
        gen = 'gctgd'
        val = match_loc.is_gen(gen)
        self.assertFalse(val)

    def test_is(self):
        gen = 'gtcaaaaa'
        val = match_loc.is_gen(gen)
        self.assertTrue(val)

if __name__ == '__main__':
    unittest.main()
