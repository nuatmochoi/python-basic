class Node:
    def __init__(self):
        self.__data=None
        self.__prev=None
        self.__next=None

    def __del__(self):
        print('{} is deleted'.format(self.__data))

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, d):
        self.__data=d

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, p):
        self.__prev=p

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, n):
        self.__next=n

class DoubleLinkedList:
    def __init__(self):
        self.head=Node()
        self.tail=Node()
        
        self.head.next=self.tail
        self.tail.prev=self.head

        self.d_size=0

    def empty(self):
        if self.d_size==0:
            return True
        else:
            return False

    def size(self):
        return self.d_size

    def add_first(self, data):
        new_node=Node()
        new_node.data=data
        new_node.next=self.head.next
        new_node.prev=self.head

        self.head.next.prev=new_node
        self.head.next=new_node

        self.d_size+=1

    def add_last(self, data): #head를 tail로 /순서를 반대로
        new_node=Node()
        new_node.data=data

        new_node.prev=self.tail.prev
        new_node.next=self.tail
        self.tail.prev.next=new_node
        self.tail.prev=new_node
        
        self.d_size+=1


    def insert_after(self, data, node): #기준을 node로
        new_node=Node()
        new_node.data=data

        new_node.prev=node.next
        new_node.next=node
        node.next.prev=new_node
        node.next=new_node
        
        self.d_size+=1

    def insert_before(self, data, node):
        new_node=Node()
        new_node.data=data
        new_node.prev=node.prev
        new_node.next=node

        node.prev.next=new_node
        node.prev=new_node

        node.d_size+=1

    def search_forward(self, target):
        cur=self.head.next

        while cur is not self.tail:
            if cur.data==target:
                return cur
            cur=cur.next
        return None #cur가 tail을 가리키고 있을 것이므로(None)
        
    def search_backward(self, target):
        cur=self.tail.prev

        while cur is not self.head:
            if cur.data==target:
                return cur
            cur=cur.prev
        return None

    def delete_first(self): #reference count=0으로 만들면 됨
        if self.empty():
            return
        self.head.next=self.head.next.next
        self.head.next.prev=self.head #self.head.next가 바뀌는 것이므로 순서 중요

        self.d_size-=1

    def delete_last(self): 
        if self.empty():
            return
        self.tail.prev=self.tail.prev.prev
        self.tail.prev.next=self.tail

        self.d_size-=1

    def delete_node(self,node):
        if self.empty():
            return
        node.prev.next=node.next
        node.next.prev=node.prev

        self.d_size-=1

def show_list(dl):
    cur=dl.head.next
    while cur is not dl.tail:
        print(cur.data, end='   ')
        cur=cur.next


if __name__="__main__":

    dl=DoubleLinkedList()
    #insert
    dl.add_first(1)
    dl.add_first(2)
    dl.add_first(3)
    #search

    #delete

    show_list(dl)

    print()