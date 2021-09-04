n = 18

guess = 1
print("You have 5 guess to try")
while (guess <= 5):
    Try_1 = int(input("Your Number : "))
    if Try_1>18:
        print("You have entered greater number")
    elif Try_1<18:
        print("You have entered smaller number")
    else:
        print("You won the Game!!!")
        print("Number of guesses you took to Finish are  : ", guess)
        break

    print("No. of guesses left :", 5-guess)
    guess = guess + 1

if guess > 5:
    print("GAME OVER !!!")
