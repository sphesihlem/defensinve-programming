print("Defensive demo ")

try:
  num1 = int(input("Enter the 1st number : "))
  print("This is the number", num1)
except ValueError:
  print( " Opps that's not a number ")

except KeyboardInterrupt:
  print("Done")

# We need to help the user to recover from their mistake 

number = input("Enter a number : ")

# Block until number is a numeric value 
while number.isnumeric()==False:
    print(number, "is not a number Try again !!!")
    number = input("Enter a number : ")

 # Here number will a numeric 
print(int(number) + 2) 
