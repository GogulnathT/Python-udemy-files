input('Press ENTER to start the hilo guessing game')

guesses = 1
high = 1000
low = 1

while True :
    guess = low + (high - low)// 2
    high_low = input("My guess is {}. If it is higher enter h, lower enter l and correct enter c : ".format(guess)).casefold()

    if high_low == 'h' :
        low = guess
    elif high_low == 'l' :
        high = guess
    elif high_low == 'c' :
        print("I have guessed the answer correctly in {} guesses".format(guesses))
        break
    else :
        print("Please enter h,l or c")

    guesses = guesses + 1
    #this is the longhand version, the augmented assignment version of the above statement would be like :
    # guesses+=1, here the value of 'guesses' will be evaluated only once. Both these statements are different only in
    #python, whereas in langs like cpp and java they are the same
    
