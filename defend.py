print("Defensive demo ")

# Numbers 

try:
  num1 = int(input("Enter the 1st number"))
except ValueError:
  print("Opps that's not a number ")
