import random
print('Pls input your name:')
name=input()
print("Hello {} ! Ready to play?".format(name))
print()
print("I will guess a number within 1 to 100 and you will have to guess it!")
life=3
number=random.randrange(0,100)
print()
print("I have guessed my number, Now its your turn to think what I am thinking")
print()
user1=int(input("What do you think it is ?:"))
print()
if user1==number:
    print("Whoah!You are excellent at reading others Mind ")
    print()
    print("You win !!!!")
elif user1>number:
    print("Let me give you a hint! The number is lesser than you think!")
    life-=1
    print('You now have only {} chances left'.format(life))
    print()
    user2=int(input("What do you think the number is ?:")) 
    print()
    if user2==number:
        print("Whoah!You are excellent at reading others Mind ")
        print()
        print("You win !!!!")
    elif number%2==0:
        print('Let me give you a hint! The number is Even!')
        life-=1
        print('You now have only {} chances left'.format(life))
        user3=int(input("What do you think the number is ?:")) 
        print()
        if user3==number:
            print("Whoah!You are excellent at reading others Mind ")
            print()
            print("You win !!!!")       
        else:
            x=number%10 
            y=number//10
            s=x+y
            print("Let me give you a last hint! The sum of the digits of the number is {}".format(s))
            print()
            life-=1
            print('You now have only {} chances left'.format(life))
            print()
            user4=int(input("Give it a last shot ! What is the number?:"))
            if user4==number:
                print("Whoah!You are excellent at reading others Mind ")
                print()
                print("You win !!!!")           
            else:
                print("You lose! You are a very bad guesser!")
                print()
    elif number%2==1:
        print('Let me give you a hint! The number is odd!')
        life-=1
        print('You now have only {} chances left'.format(life))
        print()
        user3=int(input("What do you think the number is ?:")) 
        print()
        if user3==number:
            print("Whoah!You are excellent at reading others Mind ")
            print()
            print("You win !!!!")       
        else:
            x=number%10 
            y=number//10
            s=x+y
            print("Let me give you a last hint! The sum of the digits of the number is {}".format(s))
            print()
            life-=1
            print('You now have only {} chances left'.format(life))
            print()
            user4=int(input("Give it a last shot ! What is the number?:"))
            if user4==number:
                print("Whoah!You are excellent at reading others Mind ")
                print()
                print("You win !!!!")           
            else:
                print("You lose! You are a very bad guesser!")
                print()
elif user1<number:
    print("Let me give you a hint! The number is greater than you think!")
    life-=1
    print('You now have only {} chances left'.format(life)) 
    print()
    user2=int(input("what do you think the number is ?:"))
    print()
    if user2==number:
        print("Whoah!You are excellent at reading others Mind ")
        print()
        print("You win !!!!")
    elif number%2==0:
        print('Let me give you a hint! The number is Even!')
        life-=1
        print('You now have only {} chances left'.format(life))
        print()
        user3=int(input("What do you think the number is ?:")) 
        print()
        if user3==number:
            print("Whoah!You are excellent at reading others Mind ")
            print()
            print("You win !!!!")       
        else:
            x=number%10 
            y=number//10
            s=x+y
            print("Let me give you a last hint! The sum of the digits of the number is {}".format(s))
            print()
            life-=1
            print('You now have only {} chances left'.format(life))
            print()
            user4=int(input("Give it a last shot ! What is the number?:"))
            if user4==number:
                print("Whoah!You are excellent at reading others Mind ")
                print()
                print("You win !!!!")           
            else:
                print("You lose! You are a very bad guesser!")
                print()
    elif number%2==1:
        print('Let me give you a hint! The number is odd!')
        life-=1
        print('You now have only {} chances left'.format(life))
        print()
        user3=int(input("What do you think the number is ?:")) 
        print()
        if user3==number:
            print("Whoah!You are excellent at reading others Mind ")
            print()
            print("You win !!!!")       
        else:
            x=number%10 
            y=number//10
            s=x+y
            print("Let me give you a last hint! The sum of the digits of the number is {}".format(s))
            print()
            life-=1
            print('You now have only {} chances left'.format(life))
            print()
            user4=int(input("Give it a last shot ! What is the number?:"))
            if user4==number:
                print("Whoah!You are excellent at reading others Mind ")
                print()
                print("You win !!!!")           
            else:
                print("You lose! You are a very bad guesser! Better luck next time!!")
                print()
print('The original number was:',number)