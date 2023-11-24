import random

while True:
    user_action=input("Enter a choice(rock,paper,scisssors):")
    possible_actions=["rock","paper","scissors"]
    computer_action=random.choice(possible_actions)
    print(f"\n Your choice {user_action},computer choice {computer_action}.\n")


    if user_action==computer_action:
        print(f"Both players select {user_action}.it's a tie!")
    elif user_action=="rock":
        if computer_action=="scissors":
            print("rock beat scissors!you win!")
        else:
            print("paper beat rock!you lose.")
    elif user_action=="paper":
        if computer_action=="rock":
            print("paper beat rock!you win!")
        else:
            print("scissors beat paper!you lose.")
    elif user_action=="scissors":
        if computer_action=="paper":
            print("scissors beat paper!you win!")
        else:
            print("rock beat scissors!you lose.")


    play_again=input("do you want to play another round?(y/n:)")
    if play_again !="y":
        print("thanks for playing...!")
        break