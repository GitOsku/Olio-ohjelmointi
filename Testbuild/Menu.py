from History import History
from progress import Checker
from Datastash import Stash
import os


class User():
    
    #if you want to switch user you gotta restart the program 
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.loggedin = False
        
    def getuser(self):
        if self.loggedin:
            return self.username
        else:
            print("Not logged in")
        
    def register(self):
        f = open("registry.txt", "a") #opens textfile 
        userinfo = str(self.username + self.password) # makes a string 
        f.write(userinfo) #writes it into file
        
        #creates a folder for the user
        
        parent_dir = "C:/Users/Oskari\Desktop/Oliokoodi/Endproject/"
        path = os.path.join(parent_dir, self.username)
        
        try:
            os.mkdir(path)
        except OSError as error:
             print("Folder already exists.")
        
        #Creates text files in the userfolder    
             
        f = open(self.username + "/Bench.txt", "a")
        f = open(self.username + "/Deadl.txt", "a")
        f = open(self.username + "/Squat.txt", "a")
     
    #checks if userinfo is in the registry file
    def login(self):
        f = open("registry.txt", "r")
        userinfo = str(self.username + self.password)
        line = f.readline()
        if userinfo in line:
            print("Logged in as %s " % self.username)
            self.loggedin = True
        else:
            print("Login failed")
        f.close()         

def Menu():
    
        
     username = input("Enter username: ")
     password = input("Enter password: ")
        
     user = User(username,password)
     reg = input("Do you want to login or register new user?\nPress 1 to login 2 to register.\n")
     
     if reg == "1":
         user.login()
     elif reg == "2":
         user.register()
    
     while True:
                
        choice = input("What you option you want to use?\n1 = history\n2 = progress\n3 = main\n4 = quit\n")
    
        if choice == "1":
            History(user.getuser())
        elif choice == "2":
            Checker.check(user.getuser())
        elif choice == "3":
            Stash.Adder(user.getuser())
        elif choice == "4":
            break
        else: 
            print("\nEnter a valid nubmer")
    
Menu()