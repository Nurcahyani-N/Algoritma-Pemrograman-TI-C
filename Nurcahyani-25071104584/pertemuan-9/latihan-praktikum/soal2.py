class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class CDLL:
    def __init__(self):
        self.head = None

    # Traversal
    def display(self):
        if self.head is None:
            print("List kosong")
            return
        
        temp = self.head
        while True:
            print(temp.data, end=" <-> ")
            temp = temp.next
            if temp == self.head:
                break
        print()

    # Insert depan
    def insert_depan(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node.prev = new_node
            self.head = new_node
            return
        
        tail = self.head.prev
        
        new_node.next = self.head
        new_node.prev = tail
        tail.next = self.head.prev = new_node
        self.head = new_node

    # Insert belakang
    def insert_belakang(self, data):
        if self.head is None:
            self.insert_depan(data)
            return
        
        new_node = Node(data)
        tail = self.head.prev
        
        tail.next = new_node
        new_node.prev = tail
        new_node.next = self.head
        self.head.prev = new_node

    # Insert tengah (posisi)
    def insert_tengah(self, data, pos):
        if pos == 1:
            self.insert_depan(data)
            return
        
        new_node = Node(data)
        temp = self.head
        
        for i in range(pos - 2):
            temp = temp.next
        
        new_node.next = temp.next
        new_node.prev = temp
        temp.next.prev = new_node
        temp.next = new_node

    # Delete depan
    def delete_depan(self):
        if self.head is None:
            return
        
        tail = self.head.prev
        
        if self.head.next == self.head:
            self.head = None
            return
        
        self.head = self.head.next
        self.head.prev = tail
        tail.next = self.head

    # Delete belakang
    def delete_belakang(self):
        if self.head is None:
            return
        
        tail = self.head.prev
        
        if self.head.next == self.head:
            self.head = None
            return
        
        new_tail = tail.prev
        new_tail.next = self.head
        self.head.prev = new_tail

    # Delete tengah
    def delete_tengah(self, pos):
        temp = self.head
        
        for i in range(pos - 1):
            temp = temp.next
        
        temp.prev.next = temp.next
        temp.next.prev = temp.prev

    # Searching
    def search(self, key):
        temp = self.head
        pos = 1
        
        while True:
            if temp.data == key:
                return pos
            temp = temp.next
            pos += 1
            if temp == self.head:
                break
        return -1

    # Update
    def update(self, pos, data):
        temp = self.head
        
        for i in range(pos - 1):
            temp = temp.next
        
        temp.data = data