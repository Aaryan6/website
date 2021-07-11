while True:
    inp = input("Enter what you want 1. list , 2.dictionary , 3.set\n")
    n = int(input("Enter number : "))
    if inp=="1":
        lis = [ i for i in range(1,n+1)]
        print(lis)
    elif inp=="2":
        di = { i for i in range(1,n+1)}
        print(di)
    elif inp=="3":
        se = (i for i in range(1,n+1))
        for item in se:
            print(item)