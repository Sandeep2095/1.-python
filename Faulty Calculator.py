print("Welcome to Calculator")
print("\n Choose Your Operation"
      "\n + for Addition"
      "\n - for Subtraction"
      "\n * for Multiplication"
      "\n / for Division")


Op = input("Chose Your Operator : ")

n1 = int(input("Enter First Number : "))

n2 = int(input("Enter Second Number : "))

if Op == "+":
    if n1 == 56 and n2 == 9:
      print("Your Answer is : 77")
    else:
      print("Your Answer is : ", n1+n2)

elif Op == "*":
    if n1 == 45 and n2 == 3:
      print("Your Answer is : 555")
    else:
      print("Your Answer is : ", n1*n2)

elif Op == "/":
    if n1 == 56 and n2 == 6:
      print("Your Answer is : 4")
    else:
      print("Your Answer is : ", n1/n2)

#for Subtraction
elif Op == "-":
    print("Your Answer is : ", n1-n2)

