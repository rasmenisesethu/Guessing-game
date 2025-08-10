attempts= 0

secrect_number = 3

while True:
    try: 
        
        Guessed_number = int(input("Please enter a number : "))
        attempts += 1

        if Guessed_number > secrect_number:
            print ("You guessed too high")
        elif Guessed_number < secrect_number:
            print (" You guessed too low")
        else:
            print ("Congratulations You have WON!")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
