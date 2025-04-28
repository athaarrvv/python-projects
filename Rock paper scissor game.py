def game():
    import random
    choices = ["rock", "paper", "scissors"]
    print("Choose any : ", ", ".join(choices[:3]))
    def computerchoice():
        return random.choice(choices)
    def userchoice():
        return input("Enter Your Choice : ").lower()
    def check(user, computer):
        if user == computer:
            print("It's a tie!")
        elif (user == "rock" and computer == "scissors") or \
            (user == "paper" and computer == "rock") or \
            (user == "scissors" and computer == "paper"):
            print("user wins!")
        elif (computer == "rock" and user == "scissors") or \
            (computer == "paper" and user == "rock") or \
            (computer == "scissors" and user == "paper"):
            print("user wins!")
        else:
            print("Invalid Input!")
    user = userchoice()
    computer = computerchoice()
    print(f"Computer pulled out : {computer}")
    check(user, computer)
game()
