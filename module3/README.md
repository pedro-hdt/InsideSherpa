# JPMC Summer Internship SEP: InsideSherpa Module 3

## Tasks

Task 1 – Get all the unique merchant IDs in the file and return in a SET. Run the test provided to validate.

Task 2- Return the total number of transactions marked as fraudulent. Run the test provided to validate.

Task 3 – Expanding on Task 2 two, allow the caller of the method to pass in a flag (true/false) to get total number of transactions which either are fraudulent or not fraudulent.

Task 4 – Return all fraudulent transactions for Merchant XXX (pass in variable). Run test provided to validate.

Task 5 – Return all fraudulent transactions based on variables provided by method caller (merchant ID and fraudulent payment flag). Run test provided to validate.

Task 6 – Return a List of all transactions sorted by amount. Create a test to validate the list.

Task 7 – Return the % of fraudulent transactions carried out by men. Run test provided to validate.

Task 8 – Produce a Set of Strings of customer IDs who have equals or higher number of fraudulent transactions (based on variable passed into method). Create a test to validate
NOTE: Change the return type for the method used for task 8 from Set<Transaction> to Set<String> and adjust the test accordingly

Task 9 – Using a map – return the Customer IDs with total number of fraudulent transaction. Create a test to validate

Task 10 – Using a map – return the Merchant IDs with total amount of the fraudulent transactions. Create a test to validate

Bonus task – write a small model which returns the probability (value between 0 and 1) that the passed in transaction might be a fraudulent one.

## Solution

* This module is specific in what it asks, so the solution follows the format closely, and makes
extensive use of the Stream interface together with a functional programming approach.
* This makes for succinct, yet readable code, and requires very little computation of intermediate values.
As such, no detailed explanation of task solutions is included here.
* The bonus task seemed interesting but was **not** attempted. Some ideas were included as comments in the respective
code section.

## Instructions

```
gradlew build
gradlew run
```

