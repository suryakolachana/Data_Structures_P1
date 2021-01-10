import sys

class Node:

    def __init__(self, char = None, freq = None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def set_left(self,node):
        self.left = node
    
    def set_right(self,node):
        self.right = node
    
    def get_char(self):
        return self.char
    
    def get_freq(self):
        return self.freq
    
    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right

class Tree:
    def __init__(self,root= None):
        self.root = root

    def set(self, node):
        self.root = node
    
    def get(self):
        return self.root
    
    def binary_code_traverse(self):
        binary_code = {}

        if (self.root.get_left() is None) and (self.root.get_right() is None):
            binary_code[self.root.get_char()] = '1'
            return binary_code
        
        path = []

        def traverse(node):
            if node:
                if node.get_char() is not None:
                    binary_code[node.get_char()] = "".join(path)
                path.append('0')
                traverse(node.get_left())

                path.append('1')
                traverse(node.get_right())

                if path != []:
                    path.pop()
            else:
                if path != []:
                    path.pop()

        traverse(self.root)
        return binary_code

def huffman_encode(data):
    data =str(data)

    char_list = list(set(data))

    node_list = []

    for char in char_list:
        char_freq = data.count(char)
        node = Node(char=char,freq=char_freq)
        node_list.append(node)
    
    sorted_list = sorted(node_list,key=lambda node : node.get_freq())

    while len(sorted_list) > 1:
        left_node = sorted_list.pop(0)
        right_node = sorted_list.pop(0)
        merged_node_freq = (left_node.get_freq() + right_node.get_freq())

        new_form_node = Node(freq=merged_node_freq)
        new_form_node.set_left(left_node)
        new_form_node.set_right(right_node)

        if sorted_list != []:
            for i, node in enumerate(sorted_list):
                if node.get_freq() > new_form_node.get_freq():
                    sorted_list.insert(i,new_form_node)
                    break
                elif i == len(sorted_list) - 1:
                    sorted_list.append(new_form_node)
                    break
                else:
                    continue
        else:
            sorted_list.append(new_form_node)

    huffman_tree = Tree(root=sorted_list.pop())

    binary_code = huffman_tree.binary_code_traverse()

    encoded_data = ''

    for char in data:
        encoded_data += binary_code[char]
    
    return (encoded_data,huffman_tree)

def huffman_decode(encoded_data,tree):
    curr_node = tree.get()

    decoded_data = ''

    if (curr_node.get_left() is None) and (curr_node.get_right() is None):
        decoded_data += curr_node.get_char() *\
            curr_node.get_freq()
        return decoded_data
    
    for i,bit in enumerate(encoded_data):
        if bit == '0':
            curr_node = curr_node.get_left()
        else:
            curr_node = curr_node.get_right()
        if curr_node.get_char() is not None:
            decoded_data += curr_node.get_char()
            curr_node = tree.get()

    return decoded_data


def main():

    #Test case 1
    sentence = "AAAAAAABBBCCCCCCCDDEEEEEE"

    print('The content of the data to encode is: {}.\n'.format(sentence))
    print('The size of the data to encode is: {}.\n'.format(sys.getsizeof(sentence)))

    encoded_data,tree = huffman_encode(sentence)

    print('The content of the encoded data is: {}.\n'.format(encoded_data))
    print('The size of the encoded data is: {}.\n'.format(sys.getsizeof(int(encoded_data,base=2))))

    decoded_data = huffman_decode(encoded_data,tree)

    print('The data has been decoded.\n')

    print('The content of the decoded data is:{}.\n'.format(decoded_data))

    print('The size of the decoded data is: {}.\n'.format(sys.getsizeof(decoded_data)))

    #Test case 2
    sentence = "suryakolachana"

    print('The content of the data to encode is: {}.\n'.format(sentence))
    print('The size of the data to encode is: {}.\n'.format(sys.getsizeof(sentence)))

    encoded_data,tree = huffman_encode(sentence)

    print('The content of the encoded data is: {}.\n'.format(encoded_data))
    print('The size of the encoded data is: {}.\n'.format(sys.getsizeof(int(encoded_data,base=2))))

    decoded_data = huffman_decode(encoded_data,tree)

    print('The data has been decoded.\n')

    print('The content of the decoded data is:{}.\n'.format(decoded_data))

    print('The size of the decoded data is: {}.\n'.format(sys.getsizeof(decoded_data)))

    #Test case 3
    sentence = "venkata surya kolachana"

    print('The content of the data to encode is: {}.\n'.format(sentence))
    print('The size of the data to encode is: {}.\n'.format(sys.getsizeof(sentence)))

    encoded_data,tree = huffman_encode(sentence)

    print('The content of the encoded data is: {}.\n'.format(encoded_data))
    print('The size of the encoded data is: {}.\n'.format(sys.getsizeof(int(encoded_data,base=2))))

    decoded_data = huffman_decode(encoded_data,tree)

    print('The data has been decoded.\n')

    print('The content of the decoded data is:{}.\n'.format(decoded_data))

    print('The size of the decoded data is: {}.\n'.format(sys.getsizeof(decoded_data)))

    #Test case 4
    sentence = 1234567894321

    print('The content of the data to encode is: {}.\n'.format(sentence))
    print('The size of the data to encode is: {}.\n'.format(sys.getsizeof(sentence)))

    encoded_data,tree = huffman_encode(sentence)

    print('The content of the encoded data is: {}.\n'.format(encoded_data))
    print('The size of the encoded data is: {}.\n'.format(sys.getsizeof(int(encoded_data,base=2))))

    decoded_data = huffman_decode(encoded_data,tree)

    print('The data has been decoded.\n')

    print('The content of the decoded data is:{}.\n'.format(decoded_data))

    print('The size of the decoded data is: {}.\n'.format(sys.getsizeof(decoded_data)))

     #Test case 5
    sentence = None

    print('The content of the data to encode is: {}.\n'.format(sentence))
    print('The size of the data to encode is: {}.\n'.format(sys.getsizeof(sentence)))

    encoded_data,tree = huffman_encode(sentence)

    print('The content of the encoded data is: {}.\n'.format(encoded_data))
    print('The size of the encoded data is: {}.\n'.format(sys.getsizeof(int(encoded_data,base=2))))

    decoded_data = huffman_decode(encoded_data,tree)

    print('The data has been decoded.\n')

    print('The content of the decoded data is:{}.\n'.format(decoded_data))

    print('The size of the decoded data is: {}.\n'.format(sys.getsizeof(decoded_data)))

    #Test case 6
    sentence = ' '

    print('The content of the data to encode is: {}.\n'.format(sentence))
    print('The size of the data to encode is: {}.\n'.format(sys.getsizeof(sentence)))

    encoded_data,tree = huffman_encode(sentence)

    print('The content of the encoded data is: {}.\n'.format(encoded_data))
    print('The size of the encoded data is: {}.\n'.format(sys.getsizeof(int(encoded_data,base=2))))

    decoded_data = huffman_decode(encoded_data,tree)

    print('The data has been decoded.\n')

    print('The content of the decoded data is:{}.\n'.format(decoded_data))

    print('The size of the decoded data is: {}.\n'.format(sys.getsizeof(decoded_data)))

    #Test case 7
    sentence = 'AAA'

    print('The content of the data to encode is: {}.\n'.format(sentence))
    print('The size of the data to encode is: {}.\n'.format(sys.getsizeof(sentence)))

    encoded_data,tree = huffman_encode(sentence)

    print('The content of the encoded data is: {}.\n'.format(encoded_data))
    print('The size of the encoded data is: {}.\n'.format(sys.getsizeof(int(encoded_data,base=2))))

    decoded_data = huffman_decode(encoded_data,tree)

    print('The data has been decoded.\n')

    print('The content of the decoded data is:{}.\n'.format(decoded_data))

    print('The size of the decoded data is: {}.\n'.format(sys.getsizeof(decoded_data)))


if __name__ == "__main__":
    main()