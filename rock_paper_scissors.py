import random

print("================================\nRock Paper Scissors Lizard Spock\n================================\n\n1) ✊\n2) ✋\n3) 🖖\n4) 🦎\n5) ✌️\nPick a number: 2\n\nYou chose: ✋\nCPU chose: ✊\nThe player won!")
player_score = 0
computer_score = 0

while player_score < 3 and computer_score < 3:
    choice = int(input("Pick a number: "))
    if choice not in [1, 2, 3, 4, 5]:
        print("Invalid choice. Please choose a number between 1 and 5.")
        continue
    computer = random.randint(1, 5)
    if choice == computer:
        player = "tie"
        print("It's a tie!")
    elif (choice == 1 and computer == 3) or (choice == 2 and computer == 1) or (choice == 3 and computer == 2) or (choice == 1 and computer == 4) or (choice == 4 and computer == 3) or (choice == 3 and computer == 5) or (choice == 5 and computer == 4) or (choice == 4 and computer == 2) or (choice == 2 and computer == 3) or (choice == 3 and computer == 1):
        player = "win"
        print("You win!")
        player_score += 1
    else:
        player = "lose"
        print("You lose!")
        computer_score += 1

if player_score == 3:
    print("Congratulations! You are the winner!")

else:
    print("The computer is the winner")