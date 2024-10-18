import itertools
import pandas as pd
import numpy as np
import os
import processing

def shuffle_deck(seed:None):
    '''Generates a single shuffled deck'''
    rng = np.random.default_rng(seed = seed)
    deck = np.ndarray.flatten((np.stack((np.ones(26), np.zeros(26)), axis= 0).astype(int)))
    rng.shuffle(deck)
    return ''.join(map(str, deck))

def play_n_games(n, data):
    for i in range(n):
        deck = shuffle_deck(i)
        processing.play_one_deck(data = 'data/', deck = deck)

    filename = ['cards_win/', 'cards_draw/', 'tricks_win/', 'tricks_draw/']
    results = {}
    for folder in filename:
        if folder == 'cards_win/' or folder == 'tricks_win/':
            results[folder] = sum_games(f'{data}{folder}', True)
        elif folder == 'cards_draw/' or folder == 'tricks_draw/':
            results[folder] = sum_games(f'{data}{folder}', False)
    return results

def sum_games(data = 'data/'):
    '''Take all of the arrays in the /data folder, and add them together/divide by number of files to get the average'''
    files = [file for file in os.listdir(data) if os.path.isfile(os.path.join(data, file))] # iterate through /data directory, only process files
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