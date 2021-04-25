def History(username):
    
    #opens 3 files 
    
    f1 = open(username + "/Squat.txt", "r")
    f2 = open(username + "/Bench.txt", "r")
    f3 = open(username + "/Deadl.txt", "r")
    
    while True:
    
        choice = input("What history you want to open?\n1 = Squat\n2 = Bench\n3 = Deadl\n4 = Menu")
        
        #prints wanted file entirely
        
        if choice == "1":
            lines = f1.readlines()
            for i in lines:
                print(i)
            
        elif choice == "2":
            lines = f2.readlines()
            for i in lines:
                print(i)
            
        elif choice == "3":
            lines = f3.readlines()
            for i in lines:
                print(i)
        elif choice == "4": 
            break
        
        else: 
            print("\nEnter a valid nubmer")