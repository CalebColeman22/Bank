"""
Simple Unit Test Example using Python's unittest module and assertions
@author: John McManus
@date: March 19, 2021
Import the unittest module and the Transaction module
Test each method with at least one unit test
"""
import unittest
from transaction import Transaction
import copy 
import datetime

""" Define test testTransaction class by extending the unittest.TestCase class"""
class TestTransaction(unittest.TestCase):
    DEPOSIT = 2000 # Expected Deposit amount
    WITHDRAWL = 500 # Expected Withdrawl amount
    TRANSNUM = 102 # expected transaction number 
    TYPE = "deposit"

    # The setup method creates three transactions
    def setUp(self):
        self.transaction1 = Transaction("deposit", TestTransaction.DEPOSIT,"")
        self.transaction2 = Transaction("deposit", TestTransaction.DEPOSIT,"")

        
        # The test_constructor method tests the constructor
    def test_constructor(self):
        print("\nTesting the constructor")
        self.assertEqual(self.transaction1.getAmount(), TestTransaction.DEPOSIT)
        self.assertEqual(self.transaction1.getTNumber(), TestTransaction.TRANSNUM)
        self.assertEqual(self.transaction1.getTType(), TestTransaction.TYPE)
        print("\nThe first transaction: ", self.transaction1.__str__())
        print("\nThe second transaction: ", self.transaction2.__str__())
        


    # The test_constructor method tests the constructor when called without parameters
    def test_constructorNoParameters(self):
        print("\nTesting the constructor with no parameters")
        print("Enter 1 - deposit for the type")
        print("Enter 2000 for the amount")

        # create a new transaction
        test = Transaction()

        # test to check the new transaction's ampint and transaction type
        self.assertEqual(test.getAmount(), TestTransaction.DEPOSIT)
        self.assertEqual(test.getTType(), TestTransaction.TYPE)



    # Test the __eq__ special method
    def test_eq(self):
        print("\nTesting the equal special method")
        copyTrans = copy.deepcopy(self.transaction1)
        self.assertTrue(self.transaction1, copy)


    # Second test of the __eq__ special method
    def test_eq_2(self):
        print("\nSecond test of the equal special method")
        self.assertFalse(self.transaction1 == self.transaction2)


    # Test the __ne__ special method
    def test_ne(self):
        print("\nTesting the not equal special method ")
        self.assertTrue(self.transaction1 != self.transaction2)


    # Second test of the __ne__ special method
    def test_ne_2(self):
        print("\nSecond test of the not equal special method")
        self.assertFalse(self.transaction1 != self.transaction1)

   
    # Test the __add__ special method
    def test_add(self):
        addTest = self.transaction1.__add__(self.transaction2)
        print("\nTesting the addition special method")
        self.assertEqual(addTest, 4000)

    # Test the __sub__ special method
    def test_sub(self):
        subTest = self.transaction1 - self.transaction2
        subActual = self.transaction1.__sub__(self.transaction2)
        print("\nTesting the subtraction special method")
        self.assertEqual(subTest, subActual)



    # Test the __sum__ special method
    def test_sum(self):
        listTransactions = [self.transaction1.getAmount(), self.transaction2.getAmount()]
        sumTest = sum(listTransactions)
        
        print("\nTesting the sum special method")
        self.assertEqual(sumTest, (TestTransaction.DEPOSIT +TestTransaction.DEPOSIT))
 

    # Test the getAmount method 
    def test_getAmount(self): 
        expected = 2000
        actual = self.transaction1.getAmount()
        print("\nTesting the get amount method")
        self.assertEqual(expected, actual)


    # Test the getttype  method
    def test_getTtype(self):
        expected = "deposit"
        actual = self.transaction1.getTType()
        print("\nTesting the get transaction type method")
        self.assertEqual(expected,actual)


    # Test the getDate method 
    def test_getDate(self): 
        expected = str(datetime.date.today())
        actual = self.transaction2.getDate()
        print("\nTesting get date method")
        self.assertEqual(expected,actual)

    
    # Test the transaction number get method
    def test_getTnum(self):
        expected = 115
        actual = self.transaction1.getTNumber()
        print("\nTesting get transaction number method")
        self.assertEqual(expected, actual)




if __name__ == '__main__':
    unittest.main()
