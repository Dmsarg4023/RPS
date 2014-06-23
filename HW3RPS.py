def choice():
    """returns choice in lowercase"""
    choice = raw_input("Enter a choice: ")
    return choice.lower()

def compare(choice1, choice2):
    """rock, paper, scissors match evaluator"""
    if choice1 == choice2:
        print("It is a tie!")
    elif choice1 == 'rock':
        if choice2 == 'scissors':
            print('Rock wins!')
        elif choice2 == 'paper':
            print('Paper Wins!')
    elif choice1 == 'paper':
        if choice2 == 'scissors':
            print('scissors wins!')
        elif choice2 == 'rock':
            print('rock wins!')
    elif choice1 == 'scissors':
        if choice2 == 'paper':
            print('scissors wins!')
        elif choice2 == 'rock':
            print('rock wins!')
    else:
        print("something is wrong.")
rounds = int(raw_input("Enter number of rounds: "))
counter = 0
while counter !+ 3:    
    choice1 = choice()
    choice2 = choice()
    compare(choice1, choice2)
    counter += 1
    
