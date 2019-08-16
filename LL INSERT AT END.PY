class node:
  def __init__(self,data):
    self.data=data
    self.nxt=None

class singlylinked:
  def __init__(self):
    self.head=None

  def insrt_at_end(self,data):
    tmp=node(data) 
    if self.head is None:
        self.head=tmp
        return
    laste=self.head
    while(laste.nxt):
       laste=laste.nxt
    laste.nxt=tmp

  def printlist(self):
      printval=self.head
      while printval is not None:
          print(printval.data,"==>",end='')
          printval=printval.nxt
      print("none")
      
list=singlylinked()
list.head=node("1")
val2=node("2")
val3=node("3")
list.head.nxt=val2
val2.nxt=val3
print("enter data")
data=input()
list.insrt_at_end(data)
list.printlist()
