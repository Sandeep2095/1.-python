print("How many stars you want to draw")

Star = int(input("Enter Any Integer Value : "))

direction = int(input("Type 1 or 0 : "))
Pattern = bool(direction)

if Pattern:
    for i in range(1, Star+1):
        for j in range(1, i+1):
            print("*", end="")
        print()
elif not Pattern:
    for i in range(Star, 0, -1):
        for j in range(1, i+1):
            print("*", end="")
        print()