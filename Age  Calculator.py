
print("Answer the following questions to know how long you have lived...")

name = input("Enter Your Name : ")

print("What is your age ?", name, '?')

age = int(input("age : "))

days = age*365                       #Not Accurate
minute = age*525948                  #Not Accurate
second = age*31556926                #Not Accurate

print(name, 'has been lived for', days, 'days', minute, 'minutes', second, 'seconds')

print("You Lived too Long SINE!!!!")

print("Sayonara")

