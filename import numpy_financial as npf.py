""" USE  $ pip install numpy-financial TO GET MODULE  """

import numpy_financial as npf 


""" USE  $ pip install numpy TO GET MODULE """

import numpy as np

#Simple interest 
principal = int(input("enter principal amount: ")) # Principal Amount 
annual_rate = float(input("enter annual interest rate: ")) # yearly rate of interest 
t = int(input("enter number of years: ")) # TIME 
amount =  int(principal * (1 + annual_rate * t)) # FORMULA TO FOLLOW 
print("Total payment amount (Principal + Interest): $" + str(amount)) # OUTPUT DATA 