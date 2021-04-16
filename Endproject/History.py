def History():
    
    #opens 3 files 
    
    f1 = open("Squat.txt", "r")
    f2 = open("Bench.txt", "r")
    f3 = open("Deadl.txt", "r")
    
    print("Squat:")
    
    lines = f1.readlines()
    for i in lines:
        print(i)
    
    print("Bench:")
    
    lines = f2.readlines()
    for i in lines:
        print(i)
        
    print("Deadlift:")
    
    lines = f3.readlines()
    for i in lines:
        print(i)
    
