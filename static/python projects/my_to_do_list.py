# make To_Do_List
# add work
# delete work
while True:
    file_w = open("to_do_list.txt", "a")
    file_r = open("to_do_list.txt", "r")
    file_name = "to_do_list.txt"
    print("\nEnter 1 for the Add : ")
    print("Enter 2 for the Show : ")
    o = int(input("Enter here : "))
    if o == 1:
        inp = input("Enter your Task : ")
        file_w.write(inp+"\n")
        print("Done...\n")
    elif o == 2:
        file_read = file_r.readlines()
        for i in file_read:
            print(i,end="")
    print()
    file_r.close()
    file_w.close()