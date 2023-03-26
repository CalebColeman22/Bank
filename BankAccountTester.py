""" 
Simple Unit Test using Python's unittest module and assertions
@author: Caleb Coleman
@author: Kolby Gibson
@date: March 23, 2023

Import the unittest module and the BankAccount module
Test each method with at least one unit test
"""

import unittest
from BankAccount import BankAccount

class TestBankAccount(unittest.TestCase):
    FIRST = "Caleb" # expected first name
    LAST = "Coleman" # expected last name
    INITIAL_AMOUNT = 400.0 # expected amount of initial deposit

    # setup method creates the bank account 
    def setUp(self):
        self.account1 = BankAccount("Caleb", "Coleman", 5000.0)

    # tests constructor with no values
    def testConstructorNoParameters(self):
        print("\nTesting the constructor with no parameters *******")
        print("Enter ""Caleb"" for first name")
        print("Enter ""Coleman"" for last name")
        print("Enter ""400.0"" for amount")
        #create new bank account
        self.account2 = BankAccount()
        # test to check new bank account's first and last name, and also initial value
        self.assertEqual(self.account2.getFirstName(), TestBankAccount.FIRST)
        self.assertEqual(self.account2.getLastName(), TestBankAccount.LAST)
        self.assertEqual(self.account2.getBalance(), TestBankAccount.INITIAL_AMOUNT)


    # tests constructor with given parameters
    def testConstructorParameters(self):
        print("\nTesting the constructor with parameters")

        # test to check constructor with listed parameters
        self.assertEqual(self.account1.getFirstName(), TestBankAccount.FIRST)
        self.assertEqual(self.account1.getLastName(), TestBankAccount.LAST)
        self.assertEqual(self.account1.getBalance(), 5000.0)

    # tests the getBalance() method
    def testGetBalance(self):
        print("\nTesting getBalance()*********************")
        expected1 = 5000.0

        # testing if balance is equal to expected amount
        print("Expected Balance for account1: %.2f" %expected1)
        print("Actual: %.2f" %self.account1.getBalance())
        self.assertEqual(self.account1.getBalance(), expected1)
      

    # tests the deposit() method
    def testDeposit(self):
        print("\nTesting _deposit)**************")
        deposit = 30.0
        expected1 = 5030.0

        # make a deposit into account 1
        self.account1.deposit(deposit)


        # tests if balance after deposit is equal to the expected
        print("Expected balance after deposit for account1: %.2f" %expected1)
        print("Actual: %.2f" %self.account1.getBalance())
        self.assertEqual(self.account1.getBalance(), expected1)
  

    # tests the withdraw() method using an allowed amount
    def testWithdraw(self):
        print("\nTesting withdrawal normal **********")
        withdrawal = 500.0
        expectedResult = True
        expectedBalance = 4500.0

        # makes the withdrawal
        actual = self.account1.withdraw(withdrawal)

        # testing boolean and balances
        print("Expected: True")
        print("Actual: %s" %actual)
        self.assertTrue(actual == expectedResult)
        self.assertEqual(self.account1.getBalance(), expectedBalance)

    # tests withdraw() method when account is overdrafted
    def testWithdraw2(self):
        print("\nTesting withdrawal overdraft**********")
        withdrawal = 5100.0
        expected = False
        expectedBalance = 4980.0
        expectedOverdraftNum = 1

        # makes the withdrawal
        actual = self.account1.withdraw(withdrawal)

        # tests overdraft fee, overdraft number, and balance after overdraft fee
        print("Expected result: False")
        print("Actual result: %s" %actual)
        self.assertTrue(actual == expected)
        self.assertEqual(self.account1.getBalance(), expectedBalance, "balances do not match")
        self.assertEqual(self.account1.getOverdraftNum(), expectedOverdraftNum, "overdraft number does not match")


    # tests withdraw() method when transaction is declined
    def testWithdraw3(self):
        print("\nTesting withdrawal +250 **********")
        withdrawal = 5300.0
        expected = False

        # attempting to make withdrawal
        actual = self.account1.withdraw(withdrawal)

        # testing if withdraw went through
        print("Expected: False")
        print("Actual: %s" %actual)
        self.assertTrue(actual == expected)


    # testing transfer() method with allowed amount
    def testTransfer1(self):
        print("\nTesting transfer normal**********")
        # create new bank account to transfer $
        altAccount = BankAccount("Kolby", "Gibson", 500)
        transferAmount = 30.0
        expectedBalance1 = 5030.0
        expectedBalance2 = 470.0

        # attempting the transfer
        self.account1.transfer(altAccount, transferAmount)

        # testing if transfer went through in both accounts
        print("Expected balance account 1: %.2f" %expectedBalance1)
        print("Actual balance account 1: %.2f" %self.account1.getBalance())
        print("Expected balance account 2: %.2f" %expectedBalance2)
        print("Actual balance account 2: %.2f" %altAccount.getBalance())
        self.assertEqual(self.account1.getBalance(), expectedBalance1)
        self.assertEqual(altAccount.getBalance(), expectedBalance2)


    # tests transfer() method when a transfer ammount is too large 
    def testTransfer2(self):
        print("\nTesting transfer fail**********")
        # creating alternate bank account
        altAccount = BankAccount("Kolby", "Gibson", 500)
        transferAmount = 5800.0
        expectedBalance1 = 5000.0
        expectedBalance2 = 500.0

        # attempting transfer
        self.account1.transfer(altAccount, transferAmount)

        # testing if transfer didn't go through in both accounts
        print("Expected balance account 1: %.2f" %expectedBalance1)
        print("Actual balance account 1: %.2f" %self.account1.getBalance())
        print("Expected balance account 2: %.2f" %expectedBalance2)
        print("Actual balance account 2: %.2f" %altAccount.getBalance())
        self.assertEqual(self.account1.getBalance(), expectedBalance1)
        self.assertEqual(altAccount.getBalance(), expectedBalance2)


    # testing the addInterest() method
    def testAddInterest(self):
        print("\nTesting adding interest*********")
        expectedBalance = 5375.0
        # adding the interest
        self.account1.addInterest()

        # testing to make sure interest was added to the balance
        print("Expected balance account 1: %.2f" %expectedBalance)
        print("Actual balance account 1: %.2f" %self.account1.getBalance())
        self.assertEqual(self.account1.getBalance(), expectedBalance)


    # testing the setFirst() method
    def testSetFirst(self):
        print("\nTesting setting first name (use Caleb)********")
        # calling method
        self.account1.setFirst()
        actual = self.account1.getFirstName()
        expected = "Caleb"

        # testing if inputted name is equal to expected
        print("Expected first name: %s" %expected)
        print("Actual first name: %s" %actual)
        self.assertEqual(actual, expected, "names do not match")

    # testing the setLast() method
    def testSetLast(self):
        print("\nTesting setting last name (Use Coleman)********")
        # calling method
        self.account1.setLast()
        actual = self.account1.getLastName()
        expected = "Coleman"

        # testing if inputted name is equal to expected
        print("Expected last name: %s" %expected)
        print("Actual last name: %s" %actual)
        self.assertEqual(actual, expected, "names do not match")

if __name__ == '__main__':
    unittest.main()