import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    user = user.lower()  # Ensure the user input is lowercase
    if user not in ['r', 'p', 's']:
        return "Invalid choice. Please choose 'r' for rock, 'p' for paper, or 's' for scissors."

    computer = random.choice(['r', 'p', 's'])
    choices = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}

    print(f"Your choice: {choices[user]}")
    print(f"Computer's choice: {choices[computer]}")

    if user == computer:
        return "It's a tie"
    if is_win(user, computer):
        return "You won!"
    return "You lost!"

# r > s, s > p, p > r
def is_win(player, opponent):
    return (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r')

print(play())