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
    
    def printlist(self):
        tmp=self.head
        while tmp!=None:
            print(tmp.data,"==>",end='')
            tmp=tmp.nxt
        print("none")
        
obj=sll()
n=int(input("enter how many numbers u want to enter"))
for i in range(0,n):
    data=input("enter the number to be inserted")
    obj.insertion(data)
obj.printlist()
