def getdate():
    import datetime
    return datetime.datetime.now()

def write():
    Cn = int(input("Choose the Client Code\n"
                   "1 for Sandeep\n"
                   "2 for Amit\n"
                   "3 for Sunil\n"
                   "Enter Your Code Here : "))
    if Cn==1:
        Plan = input("Choose Diet Or Exercise? D/E : ")
        Plan = Plan.capitalize()
        if Plan == "D":
            with open("Sandeep.txt", "a") as HF:
                a = input("Enter Food and quantity : ")
                time = str(getdate())
                HF.write("[" + time + "]" + ":  " + a + "\n")
                print("\n Diet Plan Added Successfully")

        if Plan == "E":
            with open("Sandeep2.txt", "a") as HF:
                a = input("Enter the Gym Plan : ")
                time = str(getdate())
                HF.write("[" + time + "]" + ": " + a + "\n")
                print("\n Gym Plan Added Successfully")

    if Cn==2:
        Plan = input("Choose Diet Or Exercise? D/E : ")
        Plan = Plan.capitalize()
        if Plan == "D":
            with open("Amit.txt", "a") as HF:
                a = input("Enter Your Food Items : ")
                time = str(getdate())
                HF.write("[" + time + "]" + ": " + a + "\n")
                print("\n Diet Plan Added Successfully")

        if Plan == "E":
            with open("Amit2.txt", "a") as HF:
                a = input("Enter Your GYM plan : ")
                time = str(getdate())
                HF.write("[" + time + "]" + ": " + a + "\n")
                print("\n Gym Plan Added Successfully")

    if Cn == 3:
        Plan = input("Choose Diet Or Exercise? D/E : ")
        Plan = Plan.capitalize()
        if Plan == "D":
            with open("Sunil.txt", "a") as HF:
                a = input("Enter Your Food Items : ")
                time = str(getdate())
                HF.write("[" + time + "]" + ": " + a + "\n")
                print("\n Diet Plan Added Successfully")

        if Plan == "E":
            with open("Sunil2.txt", "a") as HF:
                a = input("Enter Your GYM plan : ")
                time = str(getdate())
                HF.write("[" + time + "]" + ": " + a + "\n")
                print("\n Gym Plan Added Successfully")

def read():
    Cn = int(input("Choose the Client Code\n"
                   "1 for Sandeep\n"
                   "2 for Amit\n"
                   "3 for Sunil\n"
                   "Enter Your Code Here : "))

    if Cn==1:
        Plan = input("Diet or Exercise? D/E : ")
        Plan = Plan.capitalize()
        if Plan == "D":
            with open("Sandeep.txt") as HF:
                a = HF.read()
                print("\nHere is your food log:\n" + a + "\nThanks!!")

        if Plan == "E":
            with open("Sandeep2.txt") as HF:
                a = HF.read()
                print("\n Here is your Gym log : \n " + a + "\nThanks!!")

    if Cn == 2:
        Plan = input("Diet or Exercise? D/E : ")
        Plan = Plan.capitalize()
        if Plan == "D":
            with open("Amit.txt") as HF:
                a = HF.read()
                print("\nHere is your food log:\n" + a + "\nThanks!!")

        if Plan == "E":
            with open("Amit2.txt") as HF:
                a = HF.read()
                print("\n Here is your Gym log : \n " + a + "\nThanks!!")

    if Cn == 3:
        Plan = input("Food or Exercise? D/E : ")
        Plan = Plan.capitalize()
        if Plan == "D":
            with open("Sunil.txt") as HF:
                a = HF.read()
                print("\nHere is your food log:\n" + a + "\nThanks!!")

        if Plan == "E":
            with open("Sunil2.txt") as HF:
                a = HF.read()
                print("\n Here is your Gym log : \n " + a + "\nThanks!!")


print("----Welcome to Health Management System----\n")

purp = input("Retrieve or Write? R/W : ")
purp = purp.capitalize()

if purp == "R":
    read()
elif purp == "W":
    write()