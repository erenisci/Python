class BinarySearchNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def node_inorder(self, root):
        if root != None:
            self.node_inorder(root.left)
            print(f"{root.data} ", end="")
            self.node_inorder(root.right)


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None
        self.size = 0

    def insert(self, data):
        if self.root == None:
            self.root = BinarySearchNode(data)
        else:
            new_node = BinarySearchNode(data)
            current = self.root
            while current != None:
                parent = current
                if new_node.data < current.data:
                    current = current.left
                else:
                    current = current.right

            if new_node.data < parent.data:
                parent.left = new_node
            else:
                parent.right = new_node

        self.size += 1

    def inorder(self):
        if self.root != None:
            return self.root.node_inorder(self.root)
        else:
            print("Tree is empty!")

    # def inorder(self):
    #     stack = []
    #     while self.root != None or len(stack) != 0:
    #         if self.root != None:
    #             stack.append(self.root)
    #             self.root = self.root.left
    #         else:
    #             self.root = stack.pop()
    #             print(str(self.root.data) + " ", end="")
    #             self.root = self.root.right


if __name__ == "__main__":

    lis = [50, 30, 23, 31, 66, 71, 70, 20, 24, 77, 27, 76, 78, 79]
    size = len(lis)

    tree = BinarySearchTree()
    tree.inorder()

    for i in range(size):
        tree.insert(lis[i])
    tree.inorder()
