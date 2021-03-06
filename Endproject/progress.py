def progress(f1):
    lines = f1.readlines()
    
    #kg\n deletes the kg when checking the file and split into variables at ","
    
    date, reps, weights = lines[0].strip(" kg\n").split(",")
    date, reps2, weights2 = lines[-1].strip(" kg\n").split(",")
    
    #load turns notepad file texts to integrer and then improvements compares the most recent input to first input
    
    load1 = int(eval(reps)*int(weights))
    load2 = int(eval(reps2)*int(weights2))
    improvement = load2/load1
    weightImprovement = int(weights2)/int(weights)
    
    print("Load improvement in %: ", improvement)
    print("Weight compared to start in %: ", weightImprovement)
    
# checks files and then compares how much progress has been made
def check():
    for i in range(3):
        if i == 0:
            f1 = open("Squat.txt")
            progress(f1)
            f1.close()
        if i == 1:
            f1 = open("Bench.txt")
            progress(f1)
            f1.close()
        if i == 2:
            f1 = open("Deadl.txt")
            progress(f1)
            f1.close()
        

