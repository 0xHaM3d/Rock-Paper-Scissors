import random


class RockPaperScissors:

    def __init__(self, name):
        self.choices = ['rock', 'paper', 'scissors']
        self.player_name = name

    def get_player_choice(self):
        player_choice = input(f'Please enter your choice: ({self.choices}) ')
        if player_choice.lower() in self.choices:
            return player_choice.lower()
        
        print(f"Invalid choice, Please select from {self.choices}")
        return self.get_player_choice()
    
    def computer_choice(self):
        return random.choice(self.choices)

    def decide_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "tie"
        
        winner_combinations = [
            ('rock', 'scissors'),
            ('scissors', 'paper'),
            ('paper', 'rock')
        ]
        
        if (player_choice, computer_choice) in winner_combinations:
            return "player"
        
        return "computer"

    def play(self):
        player_choice = self.get_player_choice()
        computer_choice = self.computer_choice()

        print(f"Computer choice: {computer_choice}")

        return self.decide_winner(player_choice, computer_choice)


if __name__ == '__main__':
    game = RockPaperScissors('Hamed')

    player_wins = 0
    computer_wins = 0

    for i in range(1, 11):
        print(f"\n--- Round {i} ---")
        result = game.play()

        if result == "player":
            print("You won this round!")
            player_wins += 1
        elif result == "computer":
            print("Computer won this round!")
            computer_wins += 1
        else:
            print("This round is a tie.")

    print("\n============================")
    print("       FINAL RESULTS")
    print("============================")
    print(f"Player wins:   {player_wins}")
    print(f"Computer wins: {computer_wins}")
    print(f"Ties:          {10 - (player_wins + computer_wins)}")
    print("============================")