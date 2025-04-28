def game():
    import random
    choices = ["rock", "paper", "scissors"]
    print("Choose any:", ', '.join(choices[:3]))

    def computerchoice():
        return random.choice(choices)
    
    def userchoice():
        return input("Enter your choice : ").lower()
    
    def check(user, comp):
        if user == comp:
            print("It's a tie!")
        elif (user == "rock" and comp == "scissors") or (user == "paper" and comp == "rock") or (user == "scissors" and comp == "paper"):
            print("User wins!")
        elif (comp == "rock" and user == "scissors") or (comp == "paper" and user == "rock") or (comp == "scissors" and user == "paper"):
            print("Computer wins!")
        else:
            print("Sorry invalid input.")
    comp = computerchoice()
    user = userchoice()
    print(f"computer has choosen : {comp}")
    check(user, comp)
game()