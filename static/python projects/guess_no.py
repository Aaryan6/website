# No. is 18
# no. of guesses 9
# show which guesses left
# if no. of guesses has lost print game over
import random
the_number = random.randint(1,100)
no_of_guesses = 0
print("No. of guesses is limited (9 times)")
while (no_of_guesses<9):
    inp = int(input("Enter number : "))
    no_of_guesses=no_of_guesses+1
    if no_of_guesses==9 and inp!=the_number:
        print("You have lost of all chance...")
        print("The number is",the_number)
        print("GAME OVER")
    elif inp>the_number:
        print("Your number is greater... , please try again")
        print("You have",9-no_of_guesses,"chance left")
    elif inp<the_number:
        print("Your number is lower... , please try again")
        print("You have", 9 - no_of_guesses, " chance left")
    elif inp==the_number:
        print("Yes, this is right number")
        print("YOU WIN")
        break

    # Quiz is complete... , congratulation