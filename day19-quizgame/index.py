class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

class Question:
    def __init__(self, text, choices, correct_choice):
        self.text = text
        self.choices = choices
        self.correct_choice = correct_choice

    def display(self):
        print(self.text)
        for i, choice in enumerate(self.choices):
            print(f"{i + 1}. {choice}")

    def check_answer(self, answer):
        if answer == self.correct_choice:
            return True
        return False

# Sample questions
questions = [
    Question("What is the capital of France?", ["London", "Paris", "Berlin", "Madrid"], 2),
    Question("Who painted the Mona Lisa?", ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Michelangelo"], 1),
    Question("What is the largest planet in our solar system?", ["Mercury", "Venus", "Saturn", "Jupiter"], 4)
]

players = []
leaderboard = {}

def add_player():
    name = input("Enter your name: ")
    player = Player(name)
    players.append(player)

def display_leaderboard():
    sorted_scores = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
    print("Leaderboard:")
    for i, (name, score) in enumerate(sorted_scores):
        print(f"{i+1}. {name}: {score}")

def play_game():
    add_player()
    for question in questions:
        print()
        question.display()
        answer = int(input("Enter your answer (1-4): "))
        if question.check_answer(answer):
            print("Correct answer!")
            players[-1].score += 1
        else:
            print("Wrong answer!")

    leaderboard[players[-1].name] = players[-1].score
    print(f"\nYour score: {players[-1].score}")
    display_leaderboard()

# Main program loop
while True:
    print("\n--- Quiz Game ---")
    print("1. Play Game")
    print("2. Exit")
    choice = int(input("Enter your choice (1-2): "))
    if choice == 1:
        play_game()
    elif choice == 2:
        break
    else:
        print("Invalid choice. Please try again.")
