#
#  This program creates a bank account object that has overdraft fees, 
# interest rate, first and last name requirements,  unique account numbers, 
# transaction lists, overdraft counter, and a balance.
#
# Date Created: 3/18/2023
# 
# Created by Kolby Gibson and Caleb Coleman
# 
#  


# import transaction class
from transaction import Transaction

# BankAccount class
class BankAccount :

   #  Define any class variables or constants
   _nextAccount = 1000 # A class variable that hold the number of the next account
   OVERDRAFT_FEE = 20.00
   INTEREST_RATE = 0.075

   #  Constructs a bank account with a given balance.
   #  @param initialBalance the initial account balance (default = 0.0)
   #
   def __init__(self, firstName = "", lastName = "", initialBalance = 0.0) :
      self._accountNum = BankAccount._nextAccount  # The account number
      BankAccount._nextAccount = BankAccount._nextAccount + 1
      if(firstName == ""):
          self.setFirst()   # The first name associate with the account
      else:
          # checks if valid length of the name 
         if(len(firstName) > 25):
               self.setFirst()

         # checks for special characters in name 
         specChars = '[@_!#$%^&*()<>?/\|}{"~:]'
         for char in specChars: 
               if(char in firstName):
                  self.setFirst()
      
         self._firstName = firstName

      if(lastName == ""):
         self.setLast() # The last name associate with the account

      else:
         # checks if valid length of the name 
         if(len(lastName) > 40):
               self.setLast()

         # checks for special characters in name 
         specChars = '[@_!#$%^&*()<>?/\|}{"~:]'
         for char in specChars: 
               if(char in lastName):
                  self.setLast()
      
         self._lastName = lastName
    
      self._tList = []   # The list of transactions
      self._tList.append(Transaction(amount = initialBalance, tType = "Deposit"))
      print("Initial account balance is $%.2f" % initialBalance)

       # ***** handles the overdrawn count of the account *****
      overdraw = 0
      self._overdrawNum = overdraw

   #  Define the Accessor Methods
   #  Gets the current balance of this account.
   #  @return the current balance
   #
   def getBalance(self) :
      return sum(self._tList)

   # Gets the current first name of the account
   def getFirstName(self):
        return self._firstName
   
   # Gets the current last name of the account
   def getLastName(self):
        return self._lastName

   # Gets the current overdraft number for this account.
   # @return current overdraft number
   def getOverdraftNum(self):
       return(self._overdrawNum)
   

   #  Method that prints the transactions in this account.
   #
   def printAccount(self) :
      print("The account information this account: ")
      print("Account Holder is %s %s" %(self._firstName, self._lastName))
      print("Account number is %d" %(self._accountNum))
      print("Balance is %.2f" %(self.getBalance()) )
      return 
 
   #  Method that prints the transactions in this account.
   #
   def printTransactions(self) :
      print("The current transactions for this account: ")
      for element in self._tList:
         element.printTransaction()
      return 

   #  Define the Mutator Methods
   #  Deposits money into this account.
   #  @param amount the amount to deposit
   #
   def deposit(self, amount) :
      self._tList.append(Transaction(amount = amount, tType = "Deposit"))
      print("Deposit of $%.2f, Current account balance is $%.2f" % (amount, sum(self._tList)))
      return

   
   
   #  Makes a withdrawal from this account, or charges a penalty if
   #  sufficient funds are not available.
   #  @param amount the amount of the withdrawal
   #
   def withdraw(self, amount) :

      # if withdrawal is more than balance + 250, deny transaction
      if amount > (sum(self._tList) + 250.0):
          print("Transaction denied")
          return False
      # if withdrawal is more than balance, overdraft penalty
      elif (amount > sum(self._tList)) :
         self._overdrawNum = self._overdrawNum + 1
         self._tList.append(Transaction(amount = -self.OVERDRAFT_FEE, tType = "Penalty"))
         print("Attempt to overdraw account, penalty of %.2f " % self.OVERDRAFT_FEE, end = "")
         return False
      # withdrawal from account
      else :         
         self._tList.append(Transaction(amount = -amount, tType = "Withdrawl"))
         print("withdraw of $%.2f " % amount, end = "")
         return True
      # print("Current account balance is $%.2f" % sum(self._tList))

   
   # Makes a transfer from one bank account to another
   # @param otherAccount other bank account money will be transfered from
   # @param amount the amount of the transfer
   #
   def transfer(self, otherAccount, amount):
       # attempt withdrawal from other onject, transfer is made if true
       if(otherAccount.withdraw(amount) == True):
           self._tList.append(Transaction(amount = amount, tType = "Transfer"))



   #  Adds interest to this account.
   #  @param rate the interest rate as a percent (e.g., 5.5%)
   #
   def addInterest(self) :
      amount = round(sum(self._tList) * self.INTEREST_RATE, 2)
      self._tList.append(Transaction(amount = amount, tType = "Interest"))      
      print("Interest of $%.2f added, Current account balance is $%.2f" % (amount, sum(self._tList)))
      
   # Mutator method that sets the first name for the account holder
   def setFirst(self):
      firstName = input("Enter the first name of the account: ")
      if(firstName == ""):
            self.setFirst()

        # if it is given check the name for format
      else:
      # checks if valid length of the name 
         if(len(firstName) > 25):
               self.setFirst()

         # checks for special characters in name 
         specChars = '[@_!#$%^&*()<>?/\|}{"~:]'
         for char in specChars: 
               if(char in firstName):
                  self.setFirst()
      
         self._firstName = firstName
      return 

   # Mutator method that sets the last name for the account holder
   def setLast(self):
      lastName = input("Enter the last name of the account: ")

      if(lastName == ""):
         self.setLast()

      else:
         # checks if valid length of the name 
         if(len(lastName) > 40):
               self.setLast()

         # checks for special characters in name 
         specChars = '[@_!#$%^&*()<>?/\|}{"~:]'
         for char in specChars: 
               if(char in lastName):
                  self.setLast()
      
         self._lastName = lastName
      return 

    # Prints all of the transaction instance variables.
    # @return: The formatted, human readable string of the transaction
   def __str__ (self):
      transaction = []
      for item in self._tList:
         transaction.append(item) 
      return transaction