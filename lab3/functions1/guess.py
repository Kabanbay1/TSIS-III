def guess_the_number():
    from random import randint
    l=randint(1, 20)
    a=0
    name=input("Hello! What is your name?\n")
    print("Well, "+name+", I am thinking of a number between 1 and 20.\n")
    r=int(input("Take a guess.\n"))
    while r!=l:
        if r<l:
            print("Your guess is too low.\n")
            r=int(input("Take a guess.\n"))
            a+=1
        elif r>l:
            print("Your guess is too high.\n")
            r=int(input("Take a guess.\n"))
            a+=1
    print("Good job, "+name+"! You guessed my number in "+str(a)+ " guesses!")