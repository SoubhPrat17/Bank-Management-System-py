#Project-3____Bank_Management_System____####
#__________Name- Soubhagya Pratik_____####
#__________mail id- pratikmercer@gmail.com____####


class Bank:

    #Global variables
    num_of_accounts = 0
    __acc_nos = []

    def __init__(self,acc_num = None,name = None,balance =0 ):

        self.__acc_no = acc_num
        self.__name = name
        self.__balance = balance

        if ((acc_num) and (acc_num!=-1)):
            self.__acc_no = acc_num
        else:
            if self.__acc_no in Bank.__acc_nos:
                self.__acc_no = Bank.__acc_nos[-1] + 1
            else:
                self.num_of_accounts += 1

        Bank.__acc_nos.append(self.__acc_no)
        Bank.num_of_accounts += 1


    def get__accno(self):
        return self.__acc_no

    def get_Balance(self):
        return self.__balance

    def get_name(self):
        return self.__name



    def set_acc_no(self,value):
        self.__acc_no = value

    def set_name(self,value):
        self.__name = value

    def set_Balance(self,value):
        self.__balance = value


class Saving_account(Bank):


    def __init__(self,acc_num,name,balance):
super.__init__(acc_num,name,balance)

        if branchName == '-1':
            self.branchName = "NCR"
        else:
            self.branchName = branchName

    if branchName == '-1':
        self.branchName = "NCR"
    else:
        self.branchName = branchName

    def withdrawMoney(self, amount):

        bal = super().get_Balance()
        if bal >= amount:
            bal -= amount
            super().set_Balance(bal)
            print('Money Withdrawn Successfully!')
        else:
            print('Insufficient Funds to withdraw Money!')\

    def checkBalance(self):
        print(f'Your Current Balance is : $ {super().get_Balance()}')


    def depositMoney(self):
        bal = super().get_Balance()
        bal += amount
        super().set_Balance(bal)
        print('Money Successfully Deposited!')



class FixedDeposit(Bank):

    def __init__(self,acc_num,name,duration,amount,rateOfInterest):

        super.__init__(acc_num,name)
        self.__duration = duration
        self.__amount = amount
        self.__rateOfInterest = rateOfInterest

    def get_Duration(self):
        return self.__duration

    def get_amount(self):
        return self.__amount

    def get_Rate_Of_Interest(self):
        return self.__rateOfInterest

    def set_Duration(self, value):
        self.__duration = value

    def set_amount(self,value):
        self.__amount = value

    def set_Rate_Of_Interest(self,value):
        self.__rateOfInterest = value
class RecurringDeposit(Bank):

    def __init__(self,acc_num,name,duration,amount,monthlyPayment,rateOfInterest):

        super.__init__(acc_num,name)

        self.__duration = duration
        self.__monthlyPayment = monthlyPayment
        self.rateOfInterest = rateOfInterest

    def get_Duration(self):
        return self.__duration

    def get_monthly_Payment(self):
        return self.__monthlyPayment

    def get_rateOfInterest(self):
        return self.rateOfInterest


    def set_Duration(self, value):
        self.__duration = value

    def set_monthly_Payment(self,value):
        self.__monthlyPayment = value

    def set_rateOfInterest(self,value):
        self.rateOfInterest = value


def main():
     while True:
         print()
         print("*" * 30)
         print(" Welcome to Bank of Shimla Pvt. Ltd. ")
         print("*" * 30, "\n")
         print("1. Create or Manage a Savings Account")
         print("2. Create or Manage a Fixed Deposit Account")
         print("3. Create or Manage a Recurring Deposit Account")
         print("4. Exit")

         choice = int(input("\nEnter your Choice : "))

         if choice == 1:
             print()
             print("*" * 5, "Welcome to the Savings Section", "*" * 5)
             n = int(input(
                 "What do you want to do?\n1. Create a New Account. \n2. Checkout Existing Account.\nEnter your Choice : "))

             if n == 1:
                 name = input("Enter your Name : ")
                 accNo = int(input("Enter an Account Number of your Choice or Leave it Random [-1] : "))
                 balance = int(input("Enter your Opening Balance : "))
                 branch = input("Enter a Branch Name of your Choice or Leave it Random [-1] : ")
                 savingsObj = SavingAccount(accNo, name, balance, branch)
                 print(f"\nSaving Account Created Successfully for {name}!\n")

             if n == 2:

                 x = int(
                     input(
                         "Select : \n1. Know your Balance \n2. Withdraw Money \n3. Deposit Money\nEnter your Choice : "))

                 # Checking Balance
                 if x == 1:
                     savingsObj.checkBalance()

                 # Withdrawing Money
                 elif x == 2:
                     amount = int(input("Enter the Amount you want to Withdraw : "))
                     savingsObj.withdrawMoney(amount)

                 # Depositing Money
                 elif x == 3:
                     amount = int(input("Enter the Amount you want to Deposit : "))
                     savingsObj.depositMoney(amount)

                 # Other Cases
                 else:
                     print("Illegal Input, Please Try Again")

         elif choice == 2:

             print()
             print("*" * 5, "Welcome to the Fixed Deposit Section", "*" * 5)
             n = int(input(
                 "What do you want to do?\n1. Create a New Account. \n2. Checkout Existing Account.\nEnter your Choice : "))

             pass

         elif choice == 3

             print()
             print("*" * 5, "Welcome to the Recurring Deposit Section", "*" * 5)
             n = int(input(
                 "What do you want to do?\n1. Create a New Account. \n2. Checkout Existing Account.\nEnter your Choice : "))

             pass

         elif choice == 4:
             exit(0)

         else:
             print("Sorry, Wrong Choice! Please Try Again!")


if __name__ == '__main__':
    main()
