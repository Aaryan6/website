while True:
    ank= int(input("Enter no. for choose rows and column : "))
    chooseno = int(input("Enter 0 or 1 : "))
    bull= bool(chooseno)
    if bull == True:
        for i in range(0,ank+1):
         print(i*"* ")
    else:
        for j in range(ank,0,-1):
         print(j*"* ")