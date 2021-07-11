import random

swg = ["snake", "water", "gun"]
chance = 0
ply = 0
comp = 0
while chance < 10:
    user = input("What you choose s for Snake , w for Water , g for Gun ? : \n")
    computer = random.choice(swg)
    if user == computer:
        print("Tie")
    elif user == "s" and computer == "water":
        print("Player is Win")
        ply=ply+1
    elif user=="w" and computer=="gun":
        print("Player is Win")
        ply =ply+1
    elif user=="g" and computer=="snake":
        print("Player is Win")
        ply =ply+1
    elif user=="g" and computer=="water":
        print("Computer is Win")
        comp=comp+1
    elif user=="s" and computer=="gun":
        print("Computer is Win")
        comp = comp + 1
    elif user=="w" and computer=="snake":
        print("Computer is Win")
        comp = comp + 1
    chance = chance + 1
    print(f"You have {10-chance} chance left\n")
print("GAME OVER")
if ply > comp:
    print(f"Player is Win the Game : {ply}")
    print(f"Computer : {comp}")
elif ply < comp:
    print(f"Computer is Win the Game : {comp}")
    print(f"Player : {ply}")
else:
    print(f"Game is Tie - Player {ply} : Computer {comp}")