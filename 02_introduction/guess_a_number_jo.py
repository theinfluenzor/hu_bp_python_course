from random import randint


tries = 7
idiottry = 2
count = 0
rnd_nr = randint(1, 100)

while tries > 0 and idiottry > 0:
    tries -= 1
    count += 1
    try:
        guessed_nr = int(raw_input('Please enter an integer between 1 and 99. You have ' + str(tries) +' tries left :'))
        if guessed_nr not in range(1, 100):
            idiottry -= 1
            print 'The number should honestly be between 1 and 99 ;)'
            continue
    except:
        idiottry -= 1
        print 'Come on, it is not that complicated! I want an integer'
        continue

    if guessed_nr == rnd_nr:
        print "You're a hero !! " + str(guessed_nr) + ' was right. You only needed ' + str(count) + ' tries.'
        ask = raw_input('Do you want to play again ? Enter: Yes ')
        if ask == 'Yes':
            tries = 7
            idiottry = 2
            count = 0
            rnd_nr = randint(1, 100)
            continue
        else:
            print 'I interpret that as a No.'
            break
        break
    elif guessed_nr > rnd_nr:
        print 'That was too euphoric ;) Your number is too high.'
    elif guessed_nr < rnd_nr:
        print 'Not enough.'

if idiottry <= 0:
    print "You are too stupid !! You're not allowed to play again."


