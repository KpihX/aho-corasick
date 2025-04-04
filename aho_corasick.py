from enum import ENUM

class State(ENUM):
    INIT = 0
    NORMAL = 1
    INTER = 2
    FINAL = 3

def trie (patterns:str):
    node_0 = Node('', None, State.INIT)
    for pattern in patterns:
        build_trie(node_0, pattern)

    return node_0

def build_trie(node:Node, pattern:str):
    for child in node.children:
        if child.char == pattern[0]:
            if len(pattern) == 1:
                child.state = State.INTER
                return
            build_trie(child, pattern[1:])
            return
    
    child = node
    for char in pattern:
        child = Node(char, child)
        child.parent.children.append(child)
    
    child.state = State.FINAL
            



class Node():
    def init(self, char, parent, state:State=State.NORMAL): 
        self.char = char
        self.parent = parent 
        self.state = state
        self.children = []