# Basic Binary Tree insertion
class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None


class Tree:
    def __init__(self):
        self.root = None

    # This did not work. Why I do not know now.
    def insert1(self,newNode):

        if self.root == None:
            self.root = newNode
        else:
            lastNode = self.root
            while True:

                if lastNode.left is None or lastNode.right is None:
                    break
                elif(lastNode.data > newNode.data):
                    lastNode = lastNode.left

                elif(lastNode.data < newNode.data):
                    lastNode = lastNode.right

            lastNode = newNode
            print(lastNode)
            print(self.root.left)

    # Insert a node
    def insert(self,node, key):

        # Return a new node if the tree is empty
        if node is None:
            return Node(key)

        # Traverse to the right place and insert the node
        if key < node.data:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)

        return node

    def printdata(self,root):

        if (root == None):
            return
        print(root.data, end=" ")
        self.printdata(root.left)
        self.printdata(root.right)



#
# n1 = Node(10)
# n2 = Node(5)
# # n3 = Node(11)
# # n4 = Node(6)
#
# tree =Tree()
#
# tree.insert(n1)
# tree.insert(n2)
# tree.insert(n3)
# tree.insert(n4)




root = None

tree =Tree()
root = tree.insert(root, 10)
root = tree.insert(root, 5)
root = tree.insert(root, 6)
root = tree.insert(root, 11)

tree.printdata(root)


