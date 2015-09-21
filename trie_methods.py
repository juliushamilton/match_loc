import string
import random
import graph


def is_gen(s):

    # If s is a dna sequence, is_gen returns True.

    if not isinstance(s, str):
        raise TypeError('ERROR: is_gen requires a string.')
    else:
        gen = {'A', 'G', 'T', 'C'}
        for c in s:
            if c not in gen:
                return False
        else:
            return True


def name(size=6, chars=string.ascii_uppercase + string.digits):

    # name returns a random name of six characters.

    return ''.join(random.choice(chars) for _ in range(size))


def root(trie):

    # root returns the root node of a trie.

    if not isinstance(trie, graph.Graph):
        raise TypeError('ERROR: root requires a trie object;')
    elif len(trie.O) == 0:
        raise ValueError('ERROR: root requires a trie with a node.')
    else:
        return trie.O[0]


def select(s, x, trie):

    # select selects the edge f leading from node x such that
    # the symbol of f is s.

    for e in trie.A:
        if trie.dom[e] == x and trie.sym[e] == s:
            f = e
    return f


def edge_exists(s, x, trie):

    # edge_exists determines whether an edge f, whose domain is x, matching
    # the given symbol s, exists.

    for e in trie.A:
        if trie.dom[e] == x and trie.sym[e] == s:
            return True
    else:
        return False


def trie_equivalence(trie1, trie2):

    # this is a very weak measure of equivalence which relies on the fact
    # that the number of edges and leaves in tries of identical structure
    # are equivalent.

    if num_edges(trie1) == num_edges(trie2):
        if num_leaves(trie1) == num_leaves(trie2):
            return True
    else:
        return False


def arrived(x, trie):

    # arrived expresses whether x is a leaf of the trie or not.

    if x not in trie.dom.values():
        return True
    else:
        return False


def num_edges(trie):
    return len(trie.A)


def num_leaves(trie):

    # num_leaves determines the number of leaves of a trie by considering
    # all nodes that are codomains of an edge, but not domains of any edge.

    count = 0
    for o in trie.O:
        if o not in trie.dom.values():
            count += 1
    return count
