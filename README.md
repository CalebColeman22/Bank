# Bank
This assignment was the first project for my Software Security class (CSEC 323). The whole premise of this assignment was to implement an extremely simple bank
software that supported simple transactions and account management. Principles such as Defensive Programming and Least Privilege are used to code the program for
security purposes. More can be done for the program, but here are the parameters given to my group:


The Transaction class has the following attributes:
1. Day – the day of the month (1 – 31).
2. Month – the month (1 – 12).
3. Year – the year (≥ 2022).
4. Amount – the amount of the transaction (positive for a deposit, negative for a transfer or withdrawal).
5. Transaction number – the transaction number, a monotonically increasing integer, starting at 100.
6. Transaction Type – Deposit, Withdrawal, Interest, Transfer, Penalty.

The Transaction class must support the following actions:
1. Create a transaction:
a. Prompt the system for the date.
b. Prompt the user for the transaction amount.
c. Set the transaction type.
d. Assign the next available transaction number to the transaction and increment the next available
  transaction variable.
2. Display the details of a transaction:
a. Display the date of the transaction.
b. Display the amount of the transaction.
c. Display the transaction number of the transaction.
d. Display the type of the transaction.

The BankAccount class has the following attributes:
1. An overdraft fee of $20.00.
2. Interest rate of 7.5%.
3. A first name (Max 25 characters, no special characters).
4. A last name (Max 40 characters, no special characters).
5. A unique account number, a monotonically increasing integer, starting at 1000.
6. A data structure to store the account’s transactions (I refer to this as a “list”, you can select any
  appropriate structure).
7. A counter (initialized to 0) for number of times the account is overdrawn.
8. A balance.
