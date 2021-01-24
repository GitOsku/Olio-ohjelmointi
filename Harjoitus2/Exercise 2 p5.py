def kysymykset():
    name = input("Give your full name pls")
    grade = int(input("Give your grade 1 - 10"))
    return (grade)

def main():
    summa = 0
    index = 0
    running = True
    while running == True:
        summa += kysymykset() 
        index += 1
        running = bool(input("Jatketaanko True/False?"))
    print (summa / index)

#kun kysyy True or False lyö vaan enter ja saat vastauksen.

main()