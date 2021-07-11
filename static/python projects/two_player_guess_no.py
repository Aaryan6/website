import random
def play(a,b):
    guess = int(input(f"Guess the number between {a} and {b}: "))
    chance = 1
    while guess != random_no:
        if  guess < random_no:
            guess = int(input("Enter bigger number : "))
        elif guess > random_no:
            guess = int(input("Enter lower number : "))
        chance+=1
    print(f"Your guess are {chance}")
    return chance
if __name__ == '__main__':
    print("---Guess The Number---")
    a = int(input("Enter First number for number generate (a) : "))
    b = int(input("Enter Second number for number generate (b) : "))
    random_no = random.randint(a, b)
    print("Player 1's Turn-----")
    g1 = play(a,b)
    print("Player 2's Turn-----")
    g2 = play(a,b)

    if g1 < g2:
        print("Winner is Player 1")
    elif g1 > g2:
        print("Winner is Player 2")
    else:
        print("Macth is Tie!")

