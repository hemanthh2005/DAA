import heapq
class Node:

    def __init__(self,symbol=None,frequency=None):
        self.symbol=symbol
        self.frequency=frequency
        self.left=None
        self.right=None

    def __lt__(self,other):
        return self.frequency<other.frequency

def buildhuffmantree(chars,frequency):
    priority_queue=[Node(char,f) for char,f in zip(chars,frequency)]
    heapq.heapify(priority_queue)

    while len(priority_queue)>1:
        left_child=heapq.heappop(priority_queue)
        right_child=heapq.heappop(priority_queue)
        merge_node=Node(frequency=left_child.frequency + right_child.frequency)
        merge_node.left=left_child
        merge_node.right=right_child
        heapq.heappush(priority_queue,merge_node)
    return priority_queue[0]

def generate_code(node,code="",huffman_codes={}):
    if node is not None:
    #     huffman_codes={}
    # if node is not None:
        if node.symbol is not None:
            huffman_codes[node.symbol]=code
        generate_code(node.left, code + "0", huffman_codes)
        generate_code(node.right, code + "1", huffman_codes)
    return huffman_codes

chars=['a','b','c','d','e','f']
freq=[4,7,15,17,22,42]
root=buildhuffmantree(chars,freq)
huffman_codes=generate_code(root)
for char,code in huffman_codes.items():
    print(f"Character: {char},Code:{code}")