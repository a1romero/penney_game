# automations project

# Penney’s Game Simulation

This project simulates a version of Penney’s Game played with cards in order to determine the optimal starting sequences. A full explanation of the game can be found [here.] (https://en.wikipedia.org/wiki/Penney%27s_game) 

Variation 1: The player whose sequence appeared receives all of the cards in the pile, the pile is cleared, and the game continues until the deck is exhausted. Any remaining cards at the end of the game are discarded. The player with the most cards in their pile wins.
Variation 2: The player whose sequence appeared receives a point for winning the “trick”. The card pile is cleared, and the game continues until the deck is exhausted. Any remaining cards at the end of the game are discarded. The player who won the most tricks wins the game.

Files included:
data: Stores win results for Player 2 for each play (iteration). Each file is titled by a number representing the play pattern converted into a number using base 2.
data_variation_1: Stores win results for Player 2 for game plays on variation 1.
data_variation_2: Stores win results for Player 2 for game plays on variation 2.
src
penney_game.py: contains all of the functions necessary to run the simulation. The run_simulation() function generates a specified number of games under a specified variation and returns the finished heatmap.
.ipynb: a file which runs the code from penney_game.py

## How it works

The run_simulation() function takes in the number of games the user would like to play, as well as which variation the user wants. Winning by number of cards is variation 1, winning by number of tricks is variation 2. This function also allows the user to set a random seed. 

The decks are generated by shuffling an array of 26 zeros and 26 ones. The winner of each game is determined by iterating through the deck searching for the specified sequences. The results are recorded and saved in binary and separated based on which sequence was used for player 1 and for player 2. In the binary sequences, player 2 wins are recorded as zeros while player 1 wins are recorded as ones. The sequences are saved in the data_variation folder of whichever variation was specified. 

When the simulation has run through the specified number of games for each player 1 / player 2 pairing, a heatmap is generated showing the percentage of games won by player 2 for each pairing. Two digits are displayed on each box, but the full ratio can be seen by hovering over the box. Darker red boxes represent lower win ratios for player 2, while darker green boxes represent higher win ratios for player 2.

## Group work Distribution Write Up:
**Simulation Team**:

Evan: Helped with initial deck creation and simulation. Created a wrapper function that plays a specified number of games by calling our deck generation function and our function that determines the winner based on the inputted deck. 

Cynthia: Wrote simulation function: randomly generates user-specified number of card decks, represented by a string.

**Data Management Team**:
Paola: Wrote and debugged determine_winner() function. Focused on iterating through the play pattern given by the simulation team and determining who won the round for specific variation. 

Al: Added code to determine_winner() to return and save an array as a .npy file. Wrote code to iterate over the stored arrays and find the win percentage. Coded a combined function to export a win percentage array.

Mary: Tested determine_winner()  function. Wrote function to run all combinations. Helped combine all functions in one .py file so heatmap can be generated with one line of code. Checked final probabilities and corrected labeling issues with heatmap.  

**Visualization Team**:
Arianna: Wrote the create_heatmap() function and tested it on sample data.
