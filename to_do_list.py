# do to list
def to_do_list():
    
    # My Tasks Lists
    tasks=["Study","Coding","Sleep","Play Games"]

    print("Enter 1: To add Task")
    print("Enter 2: To remove Task")
    print("Enter 3: To view Tasks")
    print("Enter 4: Quit")

    while True:
        
        no=int(input("Enter a number from 1 to 4 :"))

        if no==1:
            print("Add Task")
            list=input("enter task :")
            tasks.append(list)
        
        elif no==2:
            print("Remove Task")
            list=input("Enter task to remove")
            if list in tasks:
                tasks.remove(list)
            else:
                print("Invalid Task")
                
        elif no==3:
            print("Your Tasks")
            print(tasks)
        
        elif no==4:
            print("Quitted")
            break
  
        else:
            print("Invalid")
        
to_do_list()


