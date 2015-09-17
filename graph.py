import trie_methods


class Graph():

    # A trie consists of a set of objects (nodes) and a set of arrows (edges),
    # and a function mapping edges to their domain nodes, their codomain nodes,
    # and their symbols.

    def __init__(self):
        self.O = []
        self.A = []
        self.dom = {}
        self.cod = {}
        self.sym = {}

    def node(self, x):

        # node creates a new node on the trie.

        if not isinstance(x, str):
            raise TypeError('ERROR: Node name must be a string.')
        elif x in self.O:
            raise ValueError('ERROR: Node name already used.')
        else:
            self.O.append(x)

    def edge(self, f, a, b, s):

        # edge creates a new edge on the trie.

        if not (
                isinstance(f, str) and isinstance(a, str)
                and isinstance(b, str) and isinstance(s, str)):
            raise TypeError('ERROR: Edge requires string arguments.')

        elif f in self.A:
            raise ValueError('ERROR: Edge name already taken.')

        elif not trie_methods.is_gen(s):
            raise ValueError('ERROR: Edge requires a dna char for symbol.')

        else:
            self.A.append(f)
            self.dom[f] = a
            self.cod[f] = b
            self.sym[f] = s
