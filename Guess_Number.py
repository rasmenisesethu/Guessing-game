attempts= 0

secrect_number = 3

Guessed_number = int(input("Please enter a number : "))

if Guessed_number != secrect_number:
    print("Sorry try again")
elif Guessed_number > secrect_number:
    print ("You guessed too high")
elif Guessed_number < secrect_number:
    print (" You guessed too low")
else:
    print ("Congratulations You have WON!")
