import itertools
import pandas as pd
import numpy as np
import os
import src.processing as processing

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
    n_games = []

    for folder in filename:
        if folder == 'cards_win/' or folder == 'tricks_win/':
            results[folder], g_num = processing.sum_games(f'{data}{folder}', True)
        elif folder == 'cards_draw/' or folder == 'tricks_draw/':
            results[folder], g_num = processing.sum_games(f'{data}{folder}', False)
        n_games.append(g_num)
    results['n'] = n_games[0]
    return results