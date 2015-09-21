def is_fasta(name):

    # is_fasta determines whether a filename is fasta or not.

    if not isinstance(name, str):
        raise TypeError('ERROR: is_fasta requires string inpute.')
    elif len(name) <= 10:
        return False
    elif name[-10:] == '.fasta.txt':
        return True
    else:
        return False


def open_fasta(file_name):

    # open_fasta returns a string of the dna sequences
    # contained in a fasta file by opening the file, reading the lines, and
    # eliminating the first line.

    if not isinstance(file_name, str):
        raise TypeError('ERROR: filename must be a string.')
    elif not is_fasta(file_name):
        raise ValueError('ERROR: open_fasta requires a fasta file.')
    else:
        f = open(file_name)
        lines = f.readlines()
        f.close()
        lines = lines[1:]
        for index, line in enumerate(lines):
            lines[index] = line.rstrip()
        text = "".join(lines)
        return text


def make_sample_fasta(file_name, text):

    # make_sample_fasta make a model fasta file for texting,
    # saved under the name file_name, containing text as the body

    if not isinstance(file_name, str):
        raise TypeError('ERROR: filename must be a string.')
    elif not isinstance(text, str):
        raise TypeError('ERROR: text must be a string.')
    elif not is_fasta(file_name):
        raise ValueError('ERROR: filename but be a fasta file.')
    else:
        f = open(file_name, 'w')
        f.write('xxxxxxxxx\n' + text)
        f.close()


def convert_to_text(i):

    # convert_to_text converts a fasta file into its text,
    # or a list of fasta files and strings
    # into a list of texts.

    if not (isinstance(i, list) or isinstance(i, str)):
        raise TypeError('ERROR: convert_to_text requires a list or a string.')

    elif isinstance(i, str):
        if is_fasta(i):
            return open_fasta(i)
        else:
            return i
    elif isinstance(i, list):
        for index, item in enumerate(i):
            i[index] = convert_to_text(item)
        return i


def is_gen(gen):
    for sym in gen:
        if sym not in ('A', 'C', 'G', 'T'):
            return False
    else:
        return True
