"""
JPMC Virtual SEP - InsideSherpa - Module 2
Pedro Teixeira - O734271

sanctions module
"""

import numpy as np
from math import log


def distance(str1: str, str2: str):
    """
    Naive Implementation of Levenshtein Distance

    According to this video: 
    https://www.youtube.com/watch?time_continue=584&v=We3YDTzNXEk&feature=emb_logo
    """

    # ignore case
    str1 = str1.lower()
    str2 = str2.lower()

    m = len(str1)
    n = len(str2)
    dists = np.zeros((m+1, n+1))
    dists[0] = np.arange(n+1)
    dists[:, 0] = np.arange(m+1)

    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                dists[i, j] = dists[i-1, j-1]
            else:
                add = dists[i, j-1]
                delete = dists[i-1, j]
                replace = dists[i-1, j-1]

                dists[i, j] = min(add, delete, replace) + 1

    return int(dists[m, n]), m, n


def basic_similarity(str1: str, str2: str):
    """
    Computes the basic similarity score according to the discussion on the Jupyter notebook
    """
    d, l1, l2 = distance(str1, str2)
    return 1 - (d / max(l1, l2))


def log_similarity(str1: str, str2: str):
    """
    Computes the basic similarity score according to the discussion on the Jupyter notebook

    log_20 is used.  
    """
    d, l1, l2 = distance(str1, str2)
    score = 1 - (d / max(l1, l2))

    if score == 0:
        return 0

    return 1 / (1 - log(score, 20))


def screen_name(search_name: str, sanctions_list: str, threshold=0.75, similarity_function=log_similarity):
    """
    Screens the given name against the given list of sanctioned names,
    returning a list of names together with their similarity scores if 
    those are at least as large as the threshold.    
    """
    sanctioned_names = None
    with open(sanctions_list, 'r') as f:
        # need to remove newline char at end of each name
        # there should be no empty lines in the input file
        sanctioned_names = [x[:-1] for x in f.readlines()]

    hits = []
    for sanctioned_name in sanctioned_names:
        score = similarity_function(sanctioned_name, search_name)
        if score >= threshold:
            hits.append((sanctioned_name, round(score * 100)))

    # sort the list of hits before returning
    hits.sort(key=lambda x: x[1], reverse=True)

    return hits
