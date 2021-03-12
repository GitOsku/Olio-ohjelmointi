from random import shuffle
print('Welcome to the quiz of Osku')

with open("capitaltxt.txt") as f:
    lines = f.readlines()
    
shuffle(lines)
numRight = 0
wrong = []



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