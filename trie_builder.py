import fasta
import trie_methods
import graph

def PrefixTrieConstruction(patterns):

    # This constructs a kind of graph for the list of patterns called
    # a prefix trie. Each symbol of each pattern is represented as an
    # edge on the graph, in the order they occur. Walking from the root node to a leaf spells out
    # one of the patterns.

    if not isinstance(patterns, list):
	    raise TypeError(
	        'ERROR: PrefixTrieConstruction requires'
	        ' a list of strings.')
    elif patterns == []:
        raise ValueError(
            'ERROR: PrefixTrieConstruction requires'
            ' a list of strings.')
    else:
        trie = graph.Graph()
        for pattern in patterns:
            incorporate(pattern, trie)
        return trie


def incorporate(pattern, trie):

    # incorporate takes a pattern and incorporates it as another branch
    # of a preexisting trie.

    # if the trie is empty, add a node.
    if trie.O == []:
        x = trie_methods.name()
        trie.node(x)

    # set the current node to the root.
    x = trie_methods.root(trie)

    # iterate through the pattern.
    for s in pattern:

        # if there is an existing edge matching the symbol, select it.
        if trie_methods.edge_exists(s, x, trie):
            f = trie_methods.select(s, x, trie)

            # update the current node to that edge's codomain.
            x = trie.cod[f]
        else:

            # if there is not an existing edge, create an edge with the current symbol.
            y = trie_methods.name()
            trie.node(y)
            e = trie_methods.name()
            trie.edge(e, x, y, s)

            # update the current node to that edge's codomain.
            x = trie.cod[e]
    return trie


def is_prefix(text, trie):

    # is_prefix determines whether a given text, starting from the text's first character, matches a branch of
    # the given trie, and is thus one of the patterns from which
    # the trie was constructed.

    if not (isinstance(text, str) or isinstance(trie, graph.Graph)):
        raise TypeError('ERROR: is_prefix requires string and trie.')
    else:

        # set the current node to the root of the trie.
        x = trie_methods.root(trie)

        # add an extra space at the end of the text to ensure the algorithm 
        # runs to completion and identifies when it has arrived at a leaf.
        text = text + ' '

        # iterate through the symbols in the text.
        for s in text:
            # if the current node has arrived at a leaf, then a pattern matches this text.
            if trie_methods.arrived(x, trie):
                return True

            # if the current node has not arrived at a leaf, but an edge exists matching
            # the current symbol, select that edge and travel to that edge's codomain.
            elif trie_methods.edge_exists(s, x, trie):
                e = trie_methods.select(s, x, trie)
                x = trie.cod[e]
            else:
                # if no such edge exists, the current text does not match any pattern.
                return False

def match_loc(text, trie):

    # match_loc runs prefix_trie_matching for the text,
    # then eliminates the first charater of the text and checks again.
    # It thus locates matches of prefixes inside the body
    # of the text. It returns those locations in a
    # numerical array.

    match_loc = []
    for loc in range(len(text)):
        if is_prefix(text, trie):
            match_loc.append(loc)
        text = text[1:]
    return match_loc
