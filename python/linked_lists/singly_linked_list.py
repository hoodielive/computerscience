class Node:
    def __init__(self, value):
        self.info =  value
        self.link = None

class SingleLinkedList:
    def __init__(self):
        self.start = None 

    def display_list(self):
        if self.start is None:
            print("List is empty.")
            return
        else:
            print("List  is :    ")
            p = self.start 
            while p is not None:
                print(p.info, " ", end='')
                p = p.link 
            print()
    
    def count_nodes(self):
        p = self.start
        n = 0
        while p is not None:
            n += 1
            p = p.link 
        print("Number of nodes in the list = ", n)

    def seach(self, x):
        position = 1
        p = self.start
        while p is not None:
            if p.info == x:
                print(x, " is at position ", position)
                return True
            position += 1 
            p = p.link 
        else:
            print(x, " not found in list")
            return False 

    def insert_in_beginning(self, data):
        pass

