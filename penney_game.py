import itertools
import pandas as pd
import numpy as np
import pickle

def determine_winner(play_pattern, #p1_test_seq, p2_test_seq,
                     variation=1):
    '''
    This function determines the winner for each P1 & P2 sequence combination for the inputted play pattern.
    Note that black cards are represented by 0 and red cards are represented by 1. For example, 000, 010, and 111 
    represent BBB, BRB, and RRR respectively. **CONFIRM WITH GROUP!**
    '''
    # Define all possible sequences of length 3
    possible_sequences = ['000', '001', '010', '011', '100', '101', '110', '111']
    
    # Store results for each pair of sequences
    p2_wins = pd.DataFrame(columns=possible_sequences, index=possible_sequences)

    # Create all pairs of sequences for Player 1 and Player 2
    combinations = itertools.product(possible_sequences, repeat=2)

    for p1_seq, p2_seq in combinations:
    
        #p1_seq = p1_test_seq
        #p2_seq = p2_test_seq
        # If Player 1 and Player 2 have the same sequence, ***
        if p1_seq == p2_seq:
            p2_wins.at[p1_seq, p2_seq] = None # Ask what we would do in this case
        
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
                p2_wins.at[p1_seq, p2_seq] = 0
                # Add point to final score
            else:
                print("Player 2 wins!")
                # Add point to final score
                p2_wins.at[p1_seq, p2_seq] = 1
        else:
            print('P1 Tricks: '+ str(p1_tricks))
            print('P2 Tricks: '+ str(p2_tricks))
            if p1_tricks > p2_tricks:
                print("Player 1 wins!")
                # Add point to final score
                p2_wins.at[p1_seq, p2_seq] = 0
            else:
                print("Player 2 wins!")
                # Add point to final score
                p2_wins.at[p1_seq, p2_seq] = 1
        print("")
        p2_wins_arr = p2_wins.to_numpy()
        file_name = f'data/{str(int(play_pattern, 2))}.npy' # convert the string to a binary number in base 2
        np.save(file_name,p2_wins_arr, allow_pickle=True)
    return p2_wins

# Example: Testing with a random 52-bit binary string
test_play = '1100110101011011101110001010100111101010101101010110'
# results = determine_winner(test_play,'000','111',variation=2)
