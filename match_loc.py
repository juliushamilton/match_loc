import argparse
import sys
import fasta
import trie_builder

def parse():

    # parse parses command line arguments and ensures
    # they are of the right type.

    for item in sys.argv[1:]:
        if not (fasta.is_gen(item) or fasta.is_fasta(item)):
            raise ValueError(
                'ERROR: arguments must be dna sequences'
                'or fasta files.')
    else: 
        parser = argparse.ArgumentParser(
            description='Takes a series of patterns as fasta files'
            ' or strings and a text as fasta file or string and'
            ' returns the match locations by constructing a trie.')
        parser.add_argument('text')
        parser.add_argument('patterns', nargs='+')
        args = parser.parse_args()

        text = fasta.convert_to_text(args.text)
        patterns = fasta.convert_to_text(args.patterns)

        return text, patterns

def main():

    # Takes a series of patterns as fasta files
    # or strings and a text as fasta file or string and
    # returns the match locations by constructing a trie.

    text, patterns = parse()
    trie = trie_builder.PrefixTrieConstruction(patterns)
    match_loc = trie_builder.match_loc(text, trie)
    print('Matches at: ', match_loc)
    return match_loc

if __name__ == '__main__':
    main()
    

