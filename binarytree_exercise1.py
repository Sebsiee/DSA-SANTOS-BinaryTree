class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            # add data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    
    def in_order_traversal(self):
        elements = []

        #visit left tree
        if self.left:
            elements += self.left.in_order_traversal()

        # visit base mode
        elements.append(self.data)

        # visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def calculate_sum(self):
        sum = self.data
        if self.left:
            sum += self.left.calculate_sum()
        if self.right:
            sum += self.right.calculate_sum()
        return sum


    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        return elements

    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements

def build_tree(elements):
    print("Elements:", elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    #Full Name: Sebastian Ordonio Santos
    sebastian = ["s", "e", "b", "a", "s", "t", "i", "a", "n", "o", "r", "d", "o", "n", "i", "o", "s", "a", "n", "t", "o", "s"]
    name_tree = build_tree(sebastian)
    print("=============MENU===============")
    print("       1 - Find Min")
    print("       2 - Find Max")
    print("       3 - Calculate Sum")
    print("       4 - Post Order Traversal")
    print("       5 - Pre Order Traversal")
    print("       6 - Exit")
    print("================================")
    while True:
        user_input = input("Choose your option (1-6) ")
        if user_input == "1":
            print("\033[1;32mFound Min : \033[0;0m", name_tree.find_min())
        elif user_input == "2":
            print("\033[1;32mFound Max : \033[0;0m", name_tree.find_max())
        elif user_input == "3":
            print("\033[1;32mCalculated Sum : \033[0;0m", name_tree.calculate_sum())
        elif user_input == "4":
            print("\033[1;32mPost Ordered Traversal : \033[0;0m",name_tree.post_order_traversal())
        elif user_input == "5":
            print("\033[1;32mPre Ordered Traversal : \033[0;0m",name_tree.pre_order_traversal())
        elif user_input == "6":
            exitOption = input("\033[0;31mExit? (Y/N): \033[0;0m")
            if exitOption.upper() == "Y":
                break
            elif exitOption.upper() == "N":
                continue
            else:
                print("Input not recognized.")
        else:
            print("Input not recognized.")
            continue