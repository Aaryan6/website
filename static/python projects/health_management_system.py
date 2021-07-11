

def getdate():
    import datetime
    return datetime.datetime.now()

def getadd(n):
    if n=="nikky":
        c = int(input("Enter 1 for Food and 2 for Exercise : "))
        if c==1:
            value = input("Enter your Food : ")
            with open("nikky_food.txt","a") as f:
                f.write(str(getdate())+" : "+value+"\n")
            print("Item added suscessfully")
        elif c==2:
            value = input("Enter your Exercise : ")
            with open("nikky_exercise.txt","a") as f:
                f.write(str(getdate())+" : "+value+"\n")
            print("Item added suscessfully")
    elif n=="abhi":
        c = int(input("Enter 1 for Food and 2 for Exercise : "))
        if c==1:
            value = input("Enter your Food : ")
            with open("abhi_food.txt","a") as f:
                f.write(str(getdate())+" : "+value+"\n")
            print("Item added suscessfully")
        elif c==2:
            value = input("Enter your Exercise : ")
            with open("abhi_exercise.txt","a") as f:
                f.write(str(getdate())+" : "+value+"\n")
            print("Item added suscessfully")
    elif n=="harshit":
        c = int(input("Enter 1 for Food and 2 for Exercise : "))
        if c==1:
            value = input("Enter your Food : ")
            with open("harshit_food.txt","a") as f:
                f.write(str(getdate())+" : "+value+"\n")
            print("Item added suscessfully")
        elif c==2:
            value = input("Enter your Exercise : ")
            with open("harshit_exercise.txt","a") as f:
                f.write(str(getdate())+" : "+value+"\n")
            print("Item added suscessfully")

def getshow(n):
    if n=="nikky":
        c = int(input("Enter 1 for Food and 2 for Exercise : "))
        if c==1:
            print("Your Items :")
            with open("nikky_food.txt") as f:
                for i in f:
                    print(i,end="")
        elif c==2:
            print("Your Items :")
            with open("nikky_exercise.txt") as f:
                for i in f:
                    print(i,end="")
    elif n=="abhi":
        c = int(input("Enter 1 for Food and 2 for Exercise : "))
        if c==1:
            print("Your Items :")
            with open("abhi_food.txt") as f:
                for i in f:
                    print(i,end="")
        elif c==2:
            print("Your Items :")
            with open("abhi_exercise.txt") as f:
                for i in f:
                    print(i,end="")
    elif n=="harshit":
        c = int(input("Enter 1 for Food and 2 for Exercise : "))
        if c==1:
            print("Your Items :")
            with open("harshit_food.txt") as f:
                for i in f:
                    print(i,end="")
        elif c==2:
            print("Your Items :")
            with open("harshit_exercise.txt") as f:
                for i in f:
                    print(i,end="")

while True:
    print()
    a = int(input("Enter 1 for the Add and 2 for the Show : "))
    if a==1:
        b = input("Enter Name in this [ nikky , abhi , harshit ] : ")
        getadd(b)
    elif a==2:
        b = input("Enter Name in this [ nikky , abhi , harshit ] : ")
        getshow(b)
    else :
        print("Please Enter valid Input")