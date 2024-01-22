class bank:
     _acc_name=""
     _acc_no=""
     _acc_type=""
     _acc_balance=0

     def _init_(self,a_name,a_no,a_type,a_balance):
        self._acc_name=a_name
        self._acc_no=a_no
        self.acc_type=a_type
        self._acc_balance=a_balance
    
     def deposite(self,a_deposit):
        print("Intial balance is:",self._acc_balance)
        print("Deposite is:",a_deposit)
        self._acc_balance+=a_deposit
        print("current balance is:",self._acc_balance)
    
     def withdraw(self):
        print("current balance is:",self._acc_balance)
        self.amount=int(input("How much need to withdraw:"))
        if self.amount>self._acc_balance:
           print("you don't have enough balance to withdraw||")
           print("current balance is:",self._acc_balance)
        else:
           print(self.amount,"is withdrawed.")
           self._acc_balance-=self.amount
           print("current balance is:",self._acc_balance)
    
     def acc_info(self):
         print("\n\n||||||||||||||||||||||||||||||||||||||||||||\n")
         print("Account holder name:",self._acc_name)
         print("Account number:",self._acc_no)
         print("Account type:",self._acc_type)
         print("Account Balance is:",self._acc_balance)
         print("\n\n||||||||||||||||||||||||||||||||||||||||||||\n")
    
def main():
       
    name=input("Enter Account hpolder name:")
    no=input("Enter Account number:")
    atype=input("Enter Account type:")
    bal=int(input("Enter Account initial balance:"))
    holder=bank(name,no,atype,bal)
      
    while(True):
       print("\n\n.................................................\n\n")
       opt=int(input("1)Deposite \n2)withdraw \n3)Account info \n0)Exit\n choose your option::"))
       print("\n\n.................................................\n\n")
       if opt==1:
          amount=int(input("Deposite amount:"))
          holder.deposite(amount)
       elif opt==2:
           holder.withdraw()
       elif opt==3:
           holder.acc_info()
       elif opt==0:
           break
       else:
          print("Invalid option!")

if __name__ == "_main_":
    while(True):
      main()
              
   




 
