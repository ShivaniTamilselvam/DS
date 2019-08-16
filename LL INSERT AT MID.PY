class node:
  def __init__(self,data):
    self.data=data
    self.nxt=None

class singlylinked:
  def __init__(self):
    self.head=None

  def insrt_atmid(self,middata,data):
    if middata is None:
        print("mentioned node is absent")
        return
    tmp=node(data)
    tmp.nxt=middata.nxt
    middata.nxt=tmp

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
print("enter a new data")
data=input()
list.insrt_atmid(list.head.nxt,data)
list.printlist()
