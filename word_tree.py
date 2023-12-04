""" Word Tree"""


class Node:
    """Tree Node"""

    def __init__(self, prefix="", is_terminal=False, parent=None) -> None:
        self.prefix = prefix
        self.is_terminal = is_terminal
        self.parent = parent

        self.children = [None] * 26

    def char_to_child_index(self, char) -> int:
        """Convert char to child index

        Args:
            char (str): char to find index for

        Returns:
            int: index of child
        """
        assert len(char) == 1
        char_index = ord(char) - 97
        assert 0 <= char_index < 26
        return char_index

    def set_child(self, char: str, child_node: "Node") -> None:
        """Set a node's child based on char

        Args:
            char (str): character of child to set
            child_node (Node): child node to set
        """
        self.children[self.char_to_child_index(char)] = child_node

    def get_child(self, char) -> "Node":
        """Get a node's child based on char

        Args:
            char (str): character of child to get

        Returns:
            Node: child
        """
        char_index = ord(char) - 97
        assert (char_index >= 0) and (char_index < 26)
        return self.children[char_index]

    def __repr__(self):
        return f"'{self.prefix}'"


alphabet = [chr(i) for i in range(97, 123)]


class WordTree:
    """Word Tree"""

    def __init__(self) -> None:
        self.root_node = Node("")
        self.node_dict = {"": self.root_node}

    def add_node(self, word, terminal=True) -> Node:
        """Add word node to tree, recursively build required prefix nodes

        Args:
            word (str): _description_
            terminal (bool, optional): Is provided string a terminal word. Defaults to True.

        Returns:
            Node: newly added node
        """
        # Check if word already in node list
        if word in self.node_dict:
            return self.node_dict[word]

        # if not get prefix, creating if needed, and add this node as child
        word_prefix = word[:-1]
        last_char = word[-1]

        prefix_node = self.add_node(word_prefix, False)

        new_node = Node(prefix=word, is_terminal=terminal, parent=prefix_node)

        prefix_node.set_child(last_char, new_node)

        # put word in node list
        self.node_dict[word] = new_node

        return new_node

    def get_valid_words(self, bog: "list[str]", node: Node) -> "list[str]":
        """Get terminal nodes you can build from bag-of-words from a given node

        Args:
            bog (list[str]): bag of words used to build
            node (Node): starting node

        Returns:
            list[str]: terminal nodes you can build
        """
        ret_list = []

        # Add Current
        if node.is_terminal:
            ret_list.append(node.prefix)

        # Explore children
        for i, char in enumerate(bog):
            remaining_bog = bog[:i] + bog[i + 1 :]

            # wildcard behavior
            if char == "*":
                # Treat as every character
                for current_char in alphabet:
                    child = node.get_child(current_char)
                    if child is not None:
                        ret_list = ret_list + self.get_valid_words(remaining_bog, child)
            else:
                child = node.get_child(char)
                if child is not None:
                    ret_list = ret_list + self.get_valid_words(remaining_bog, child)

        return list(set(ret_list))

    def get_all_valid_words(self, bog: "list[str]") -> "list[str]":
        """Get terminal nodes you can build from bag-of-words from root node

        Args:
            bog (list[str]): bag of words used to build

        Returns:
            list[str]: terminal nodes you can build
        """
        return self.get_valid_words(bog, self.root_node)

    def __len__(self) -> int:
        return len(self.node_dict)


def load_word_tree(tree: WordTree, file: str) -> int:
    """Load word tree with word file

    Args:
        tree (WordTree): WordTree to load words into
        file (str): filename

    Returns:
        int: new tree size
    """
    with open(file, encoding="iso8859-1") as word_file:
        for line in word_file:
            word = line.strip().replace("'", "")
            try:
                tree.add_node(word)
            except AssertionError:
                #print('Invalid word: ', word)
                pass
    return len(tree)
