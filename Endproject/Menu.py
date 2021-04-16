from History import History
from progress import progress

def Menu():
    
    choice = input("What you option you want to use?\n1 = history\n2 = progress\n3 = main\n")

    if choice == "1":
        History()
    elif choice == "2":
        progress()
    else:
        Main()
    
Menu()
    