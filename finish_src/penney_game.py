import itertools
import pandas as pd
import numpy as np
import os
import plotly.graph_objects as go

def determine_winner(play_pattern, variation, data_file = 'data/'):
    '''
    This function determines the winner for each P1 & P2 sequence combination for the inputted play pattern.
    Note that black cards are represented by 0 and red cards are represented by 1. For example, 000, 010, and 111 
    represent BBB, BRB, and RRR respectively.
    
    Once the winners have been determined for a given combination, the results are recorded and saved in an array *for player 2*.
    So it will be 1 if player 2 wins, and 0 if player 2 loses. The files are saved as numpy arrays to the /data folder.

    Parameters:
    play_pattern: takes in a binary string which represents the deck play pattern (52-digits in length)
    variation: takes in the kind of variation for the game. An input 1, represents the card count variation and 2 represents 
    the trick count variation
    data_file: takes in data folder path where play results are to be saved
    '''
    # Define all possible sequences of length 3
    possible_sequences = ['000', '001', '010', '011', '100', '101', '110', '111']

    if variation != 1 and variation != 2:
        raise(Exception('Please choose either variation = 1 or variation = 2.'))
    
    # Store results for each pair of sequences
    p2_wins = pd.DataFrame(columns=possible_sequences, index=possible_sequences)

    # Create all pairs of sequences for Player 1 and Player 2
    combinations = itertools.product(possible_sequences, repeat=2)

    for p1_seq, p2_seq in combinations:
    

        # If Player 1 and Player 2 have the same sequence, return None
        if p1_seq == p2_seq:
            p2_wins.at[p1_seq, p2_seq] = None
        
        # Initalize index and win counts for each pair
        i = 0
        pile = 0
        p1_cards = 0
        p2_cards = 0
        
        p1_tricks = 0
        p2_tricks = 0
        
        # Iterate through the play pattern
        while i <= len(play_pattern) - 3:

            # Fetch 3-card sequence
            current_seq = play_pattern[i:i + 3]
            
            # Check if Player 1's sequence matches
            if current_seq == p1_seq:
                if variation == 1:
                    # Collect all the cards up to the sequence (3 cards)
                    p1_cards += (pile + 3)
                    pile = 0
                elif variation == 2:
                    # Player 1 wins a trick
                    p1_tricks += 1
                # Reset the pile and move pointer
                i += 3
            # Check if Player 2's sequence appears
            elif current_seq == p2_seq:
                if variation == 1:
                    # Collect all the cards up to the sequence (3 cards total)
                    p2_cards += (pile + 3)
                    pile = 0
                elif variation == 2:
                    # Player 2 wins a trick
                    p2_tricks += 1
                # Reset the pile and move pointer
                i += 3
            else:
                i += 1
                pile += 1

    # Count the Player 2 wins
        if variation == 1:
            if p1_cards > p2_cards:
                p2_wins.at[p1_seq, p2_seq] = 0
                # Add point to final score
            else:
                # Add point to final score
                p2_wins.at[p1_seq, p2_seq] = 1
        else:

            if p1_tricks > p2_tricks:
                # Add point to final score
                p2_wins.at[p1_seq, p2_seq] = 0
            else:
                # Add point to final score
                p2_wins.at[p1_seq, p2_seq] = 1
        p2_wins_arr = p2_wins.to_numpy()
        if variation == 1:
            variation_path = 'data_variation_1/'
        else:
            variation_path = 'data_variation_2/'
        file_name = f'{data_file}{variation_path}{str(int(play_pattern, 2))}.npy' # convert the string to a binary number in base 2
        np.save(file_name,p2_wins_arr, allow_pickle=True)
    return p2_wins


def sum_games(data = 'data/'):
    '''Take all of the arrays in the /data folder, and add them together/divide by number of files to get the average'''
    files = [file for file in os.listdir(data)] # iterate through /data directory
    games_total = None # where the sum of the games is going
    for file in files:
        file_path = os.path.join(data,file) # get file name and directory
        game = np.load(file_path, allow_pickle=True) # load the file
        if games_total is None:
            games_total = game # initialize games_total sum array
        else:
            games_total += game
    num_games = len(files)
    return np.divide(games_total, num_games) # divide each individual element by the number of games played

def shuffle_deck(seed:None):
    '''Generates a single shuffled deck'''
    rng = np.random.default_rng(seed = seed)
    deck = np.ndarray.flatten((np.stack((np.ones(26), np.zeros(26)), axis= 0).astype(int)))
    rng.shuffle(deck)
    return ''.join(map(str, deck))

def play_n_games(n, data, seed=None, variation=1):
    '''Plays the specified number of games.'''
    if variation == 1:
        variation_path = 'data_variation_1/'
    else:
        variation_path = 'data_variation_2/'
    
    for i in range(n):
        deck = shuffle_deck(seed=seed)
        arr = determine_winner(play_pattern = deck, variation = variation, data_file = data)
    
    print(f'{n} games played with variation {variation}.')
    done_array = sum_games(data=f'{data}{variation_path}')

    return done_array

def create_heatmap(array):
    '''
    This function takes in an 8x8 array and makes a heatmap using plotly.go. The heatmap displays the win ratios for the 
    2nd player, who will choose their pattern based on what the 1st player chose. The heatmap is scaled so that percentages 
    under 0.5 show up orange while those over 0.5 are green, with the midpoint 0.5 being yellow. The top left to bottom
    right diagonal should be None values which will show up grey, since these are matches that wouldn't occur (ex. RRR v RRR).
    From top down (and right to left), the order of the sequences is 'RRR', 'RRB', 'RBR', 'RBB', 'BRR', 'BRB', 'BBR', 'BBB'.

    Parameters: 
    array: an 8x8 array with numbers between 0 and 1 representing the percentage of games that payer 2 won
    '''

    fig = go.Figure(data = go.Heatmap(
                   z = array, colorscale = 'Fall_r', # 'RdYlGn' or 'RdBu' or 'Oranges' or 'Fall_r'
                   hovertemplate = "%{y}:%{x} win ratio <br />%{z}", name = "", # the name part stops 'trace=0' from popping up
                   text=array, texttemplate='%{text:.2f}',  
                   x = ['RRR', 'RRB', 'RBR', 'RBB', 'BRR', 'BRB', 'BBR', 'BBB'], 
                   y = ['BBB', 'BBR', 'BRB', 'BRR', 'RBB', 'RBR', 'RRB', 'RRR'],
                   hoverongaps = False))
    fig.update_layout(
        title = 'Penny Game: Player Two Win Ratio',  #this is the percentage of games that player 2 wins
        title_x = 0.5,
        title_y = 0.9,
        title_font_size = 25,
        xaxis = dict(
            title = 'Player Two Choice'  
        ),
        yaxis = dict(
            title = 'Player One Choice'
        ),
        width = 600,
        height = 600
        )
    fig.update_traces(
        xgap = 1, ygap = 1
        )

    fig.show()
    return None

def run_simulation(n_games, data='data/', seed=None, variation=1):
    '''
    This function runs the entire simulation process: 
    shuffles the deck, plays the specified number of games,
    calculates the average results, and creates a heatmap.

    Parameters:
    n_games: Number of games to play.
    data: Directory to save/load game data.
    seed: Seed for random number generation.
    variation: Game variation (1 or 2).
    '''
    done_array = play_n_games(n_games, data, seed, variation)
    create_heatmap(done_array)