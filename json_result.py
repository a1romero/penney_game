import itertools
import pandas as pd
import numpy as np
import os
import processing
import json

### ChatGPT code 

# Example dictionary with an 8x8 NumPy array (np.object)
data = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "matrix": np.array([
        [1, 2, 3, 4, 5, 6, 7, 8],
        [9, 10, 11, 12, 13, 14, 15, 16],
        [17, 18, 19, 20, 21, 22, 23, 24],
        [25, 26, 27, 28, 29, 30, 31, 32],
        [33, 34, 35, 36, 37, 38, 39, 40],
        [41, 42, 43, 44, 45, 46, 47, 48],
        [49, 50, 51, 52, 53, 54, 55, 56],
        [57, 58, 59, 60, 61, 62, 63, 64]
    ], dtype=np.object)  # NumPy array of type np.object
}

# Convert NumPy array to a Python list
data["matrix"] = data["matrix"].tolist()

# Write dictionary with converted NumPy array to JSON file
with open('data_with_numpy_array.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)


###



def results_for_viz():
    """
    Reformats results of simulations for heatmap visualization.
    """
    ex = {
        "cards": [
            [1, 2, 3, 4, 5, 6, 7, 8],
            [9, 10, 11, 12, 13, 14, 15, 16],
            [17, 18, 19, 20, 21, 22, 23, 24],
            [25, 26, 27, 28, 29, 30, 31, 32],
            [33, 34, 35, 36, 37, 38, 39, 40],
            [41, 42, 43, 44, 45, 46, 47, 48],
            [49, 50, 51, 52, 53, 54, 55, 56],
            [57, 58, 59, 60, 61, 62, 63, 64]
        ],
        "tricks": [
            [1, 2, 3, 4, 5, 6, 7, 8],
            [9, 10, 11, 12, 13, 14, 15, 16],
            [17, 18, 19, 20, 21, 22, 23, 24],
            [25, 26, 27, 28, 29, 30, 31, 32],
            [33, 34, 35, 36, 37, 38, 39, 40],
            [41, 42, 43, 44, 45, 46, 47, 48],
            [49, 50, 51, 52, 53, 54, 55, 56],
            [57, 58, 59, 60, 61, 62, 63, 64]
        ],
        "card_ties": [
            [1, 2, 3, 4, 5, 6, 7, 8],
            [9, 10, 11, 12, 13, 14, 15, 16],
            [17, 18, 19, 20, 21, 22, 23, 24],
            [25, 26, 27, 28, 29, 30, 31, 32],
            [33, 34, 35, 36, 37, 38, 39, 40],
            [41, 42, 43, 44, 45, 46, 47, 48],
            [49, 50, 51, 52, 53, 54, 55, 56],
            [57, 58, 59, 60, 61, 62, 63, 64]
        ],

        "trick_ties": [
            [1, 2, 3, 4, 5, 6, 7, 8],
            [9, 10, 11, 12, 13, 14, 15, 16],
            [17, 18, 19, 20, 21, 22, 23, 24],
            [25, 26, 27, 28, 29, 30, 31, 32],
            [33, 34, 35, 36, 37, 38, 39, 40],
            [41, 42, 43, 44, 45, 46, 47, 48],
            [49, 50, 51, 52, 53, 54, 55, 56],
            [57, 58, 59, 60, 61, 62, 63, 64]
        ],
        "n": 5
    }

    if not os.path.exists('results'):
        os.makedirs('results')
    # Writing dictionary with 8x8 array to a JSON file
    with open(os.path.join('results.json'), 'w') as json_file:
        json.dump(ex, json_file, indent=4)

if __name__ == '__main__':
    # print(play_n_games(5, 't_data/'))
    results_for_viz()
