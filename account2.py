class bank:
     __acc_name=""
     __acc_no=""
     __acc_type=""
     __acc_balance=0

     def __init__(self,a_name,a_no,a_type,a_balance):
        self.__acc_name=a_name
        self.__acc_no=a_no
        self.__acc_type=a_type
        self.__acc_balance=a_balance
    
     def deposite(self,a_deposit):
        print("Intial balance is:",self.__acc_balance)
        print("Deposite is:",a_deposit)
        self.__acc_balance+=a_deposit
        print("current balance is:",self.__acc_balance)
    
     def withdraw(self):
        print("current balance is:",self.__acc_balance)
        self.amount=int(input("How much need to withdraw:"))
        if self.amount>self.__acc_balance:
           print("you don't have enough balance to withdraw||")
           print("current balance is:",self.__acc_balance)
        else:
           print(self.amount,"is withdrawed.")
           self.__acc_balance-=self.amount
           print("current balance is:",self.__acc_balance)
    
     def acc_info(self):
         print("\n\n||||||||||||||||||||||||||||||||||||||||||||\n")
         print("Account holder name:",self.__acc_name)
         print("Account number:",self.__acc_no)
         print("Account type:",self.__acc_type)
         print("Account Balance is:",self.__acc_balance)
         print("\n\n||||||||||||||||||||||||||||||||||||||||||||\n")
    
def main():
       
    name=input("Enter Account holder name:")
    no=input("Enter Account number:")
    atype=input("Enter Account type:")
    bal=int(input("Enter Account initial balance:"))
    holder=bank(name,no,atype,bal)
      
    while(True):
       print("\n\n.................................................\n\n")
       opt=int(input("1)Deposite \n2)withdraw \n3)Account info \n4)Exit\n choose your option::"))
       print("\n\n.................................................\n\n")
       if opt==1:
          amount=int(input("Deposite amount:"))
          holder.deposite(amount)
       elif opt==2:
           holder.withdraw()
       elif opt==3:
           holder.acc_info()
       elif opt==4:
           exit(0)
       else:
          print("Invalid option!")

if __name__ == "__main__":
    while(True):
      main()
              
   




 
