################################
# Your Name: Sunny Gurung
# Your Section: 1ICE
# Your Student ID Number: 02220242
################################
# REFERENCES
# https://www.w3schools.com/python/
# https://www.geeksforgeeks.org/python-program-implement-rock-paper-scissor-game/
# the problem
################################
# SOLUTION
# Your Solution Score:49903
# Put your number here: 2
################################

#Define a function to calculate the score after every round
def calculate_score(My_choice, outcome):
    player_score = 0

    if My_choice == 'rock':
        player_score += 1
    elif My_choice == 'paper':
        player_score += 2
    elif My_choice == 'scissors':
        player_score += 3

    if outcome == 'lose':
        player_score += 0
    elif outcome == 'draw':
        player_score += 3
    elif outcome == 'win':
        player_score += 6

    return player_score

#Define a function to calculate my total score
def calculate_total_score(input_file):
    My_total_score = 0

    print("Input and Outcome of each round:")
    with open(input_file, 'r') as file:
        for line in file:
            My_choice, outcome = line.strip().split()
            My_choice = 'rock' if My_choice == 'A' else 'paper' if My_choice == 'B' else 'scissors'
            outcome = 'lose' if outcome == 'X' else 'draw' if outcome == 'Y' else 'win'
            print(f"\nI chose: {My_choice} \nOutcome: {outcome}")
            player_score = calculate_score(My_choice, outcome)
            My_total_score += player_score

    return My_total_score

#Reading the file provided
input_file = 'input_2_cap1.txt'
My_total_score = calculate_total_score(input_file)

print("\nMy total score:", My_total_score)