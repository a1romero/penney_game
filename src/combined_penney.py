from dataclasses import dataclass
from typing import Callable
import numpy as np
from numpy import random

np.random.seed(43)

def sim_penney(n: int):
    # n = num of matches/outputs to produce
    game_decks = []

    for i in range(n): # simulate n many game decks  
        # create black/red decks
        black = np.full(
          shape = 26,
          fill_value = "0",
          dtype = str
        )
    
        red = np.full(
          shape = 26,
          fill_value = "1",
          dtype = str
        )

        # combine
        deck = np.concatenate((black, red))
        # shuffle to randomize
        random.shuffle(deck)

        # turn deck into string to be parsed
        deck_string = "".join(deck)

        # add gamedeck to list of decks
        game_decks.append(deck_string)

    return game_decks # return all games simulated

import itertools

def determine_winner(play_pattern, p1_test_seq, p2_test_seq,variation=1):
    '''
    This function determines the winner for each P1 & P2 sequence combination for the inputted play pattern.
    Note that black cards are represented by 0 and red cards are represented by 1. For example, 000, 010, and 111 
    represent BBB, BRB, and RRR respectively. **CONFIRM WITH GROUP!**
    '''
    # Define all possible sequences of length 3
    possible_sequences = ['000', '001', '010', '011', '100', '101', '110', '111']
    
    # Store results for each pair of sequences
    play_results = {}

    # Create all pairs of sequences for Player 1 and Player 2
    # combinations = itertools.product(possible_sequences, repeat=2)

    # for p1_seq, p2_seq in combinations:
    
    p1_seq = p1_test_seq
    p2_seq = p2_test_seq
    # If Player 1 and Player 2 have the same sequence, ***
    if p1_seq == p2_seq:
        play_results[(p1_seq, p2_seq)] = None # Ask what we would do in this case
    
    print('(' + p1_seq + ', ' + p2_seq + ')')

    # Initalize index and win counts for each pair
    i = 0
    pile = 0
    p1_cards = 0
    p2_cards = 0
    
    p1_tricks = 0
    p2_tricks = 0
    
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



    if variation == 1:
        print('P1 Cards: '+ str(p1_cards))
        print('P2 Cards: '+ str(p2_cards))
        if p1_cards > p2_cards:
            print("Player 1 wins!")
            # Add point to final score
        else:
            print("Player 2 wins!")
            # Add point to final score
    else:
        print('P1 Tricks: '+ str(p1_tricks))
        print('P2 Tricks: '+ str(p2_tricks))
        if p1_tricks > p2_tricks:
            print("Player 1 wins!")
            # Add point to final score
        else:
            print("Player 2 wins!")
            # Add point to final score
    print("")
    # return play_results

def play_game(n: int, var: int):
    '''
    Wrap the previous functions to run all combinations of sequences.
    '''
    deck = sim_penney(n)
    possible_sequences = ['000', '001', '010', '011', '100', '101', '110', '111']

    for p1_seq, p2_seq in itertools.product(possible_sequences, repeat=2):
        print(f"Testing sequences: P1: {p1_seq}, P2: {p2_seq}")
        for play_pattern in deck:
            determine_winner(play_pattern, p1_seq, p2_seq, variation=var)


