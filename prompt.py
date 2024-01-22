list1=[]
n=int(input("enter a limit:"))
i=0
while i<n:
      i=i+1
      inp=int(input("enter an integer:"))
      if(inp<100):
        list1.append(inp)
      else:
        list1.append("over")
print("list is",list1)
