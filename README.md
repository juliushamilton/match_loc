# match_loc

match_loc matches DNA sequences 'patterns' to a reference genome 'text' and returns a list of the indices in the text where matches occur.
match_loc is a command line tool. Simply command:
$ python3 match_loc text patterns,
where 'text' and 'patterns' are fasta files or DNA sequences. You can add as many patterns as you want, like so:

$ python3 match_loc arthospira.fasta.txt AGTGA GGTTTTAAA AAATG CCGTA
Matches at: [3, 345, 1006]
