from random import shuffle
print('Welcome to the quiz of Osku')

with open("countrytxt.txt") as f:
    lines = f.readlines()
    
shuffle(lines)
numRight = 0
wrong = []

Game = input("You want to play 'Countries' or 'Capitals'?")

if Game == "Countries":

    
    for line in lines[:10]:
        question, rightAnswer = line.strip().split("\t")
        answer = input(question + ' ')
        if answer == rightAnswer:
            print('100% right!')
            numRight += 1
        else:
            print('No, the answer is %s.' % rightAnswer)
            wrong.append(question)
    
    print('\nYou got %d right' % (numRight))
    if (wrong):
        print('These still needs more practice: ')
        for q in wrong:
            print(q)
        
else:             
    
    for line in lines[:10]:
        rightAnswer, question = line.strip().split("\t")
        answer = input(question + ' ')
        if answer == rightAnswer:
            print('100% right!')
            numRight += 1
        else:
            print('No, the answer is %s.' % rightAnswer)
            wrong.append(question)
        
    print('\nYou got %d right' % (numRight))
    if (wrong):
        print('These still needs more practice: ')
        for q in wrong:
            print(q)