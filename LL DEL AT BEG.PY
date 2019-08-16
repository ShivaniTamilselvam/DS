class node():
    def __init__(self,data):
        self.data=data
        self.nxt=None
class sll():
    def __init__(self):
        self.head=None
    def insertion(self,data):
        tmp=node(data)
        tmp.nxt=self.head
        self.head=tmp
    def deletion(self,data):
        tmp=self.head
        self.head=self.head.nxt
        tmp.nxt=None
    def printlist(self):
        tmp=self.head
        while tmp!=None:
            print(tmp.data,"==>",end='')
            tmp=tmp.nxt
        print("none")
        
obj=sll()
n=int(input("enter the number"))
for i in range(0,n):
    data=input("enter the number to be inserted")
    obj.insertion(data)
obj.printlist()
n1=int(input("enter how many numbers to delete"))
for j in range(0,n1):
    obj.deletion(data)
obj.printlist()
