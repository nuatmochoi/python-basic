class Node:
    def __init__(self):
        self.__data=None
        self.__link=None

    def __del__(self):
        print('{} is deleted'.format(self.__data))

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, d):
        self.__data=d

    @property
    def link(self):
        return self.__link

    @link.setter
    def link(self, l):
        self.__link=l

class SingleLinkedList:
    def __init__(self):
        self.head=None #head가 none을 가리키고 있는 상태
        self.d_size=0
    #ADT에 따라 함수 생성
    def empty(self):
        if self.d_size==0:
            return True
        else:
            return False
    
    def size(self):
        return self.d_size

    #insert
    def add(self, data):
        #새로운 노드 생성
        #데이터 저장
        new_node= Node()
        new_node.data=data

        new_node.link=self.head
        self.head=new_node

        self.d_size+=1
    
    #search
    def search(self, target):
        cur=self.head
        while cur: #data가 있다면(cur가 있다면)
            if cur.data==target:
                return cur
            cur=cur.link
        return cur
    
    #delete
    def delete(self):
        self.head=self.head.link #head를 뒤로 넘기고
        self.d_size-=1

def show_list(slist):
    cur=slist.head
    for i in range(slist.size()):
        print(cur.data, end='  ')
        cur=cur.link

sl=SingleLinkedList()
sl.add(1)
sl.add(2)
sl.add(3)

show_list(sl)

obj=sl.search(2)
if obj:
    print('{} is in the list'.format(obj.data))
else:
    print("there is no such data")

sl.delete()
show_list(sl)