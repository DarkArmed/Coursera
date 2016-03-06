"""
Student code for Word Wrangler game
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    ans = list1[:1]
    for elem in list1[1:]:
        if elem != ans[-1]:
            ans.append(elem)
    return ans

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    ans = []
    idx1, idx2 = 0, 0
    while idx1 < len(list1) and idx2 < len(list2):
        if list1[idx1] < list2[idx2]:
            idx1 += 1
        elif list1[idx1] > list2[idx2]:
            idx2 += 1
        else:
            ans.append(list1[idx1])
            idx1 += 1
            idx2 += 1
    return ans

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing those elements that are in
    either list1 or list2.

    This function can be iterative.
    """
    ans = []
    idx1, idx2 = 0, 0
    while idx1 < len(list1) and idx2 < len(list2):
        if list1[idx1] > list2[idx2]:
            ans.append(list2[idx2])
            idx2 += 1
        else:
            ans.append(list1[idx1])
            idx1 += 1
    ans.extend(list1[idx1:])
    ans.extend(list2[idx2:])
    return ans

def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    if len(list1) < 2:
        return list1
    mid = len(list1) / 2
    return merge(merge_sort(list1[:mid]), merge_sort(list1[mid:]))

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    if len(word) == 0:
        return ['']
    ans = []
    for elem in gen_all_strings(word[1:]):
        ans.append(elem)
        for idx in range(len(elem) + 1):
            ans.append(elem[:idx] + word[0] + elem[idx:])
    return ans

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    url = codeskulptor.file2url(filename)
    netfile = urllib2.urlopen(url)
    return [line.strip() for line in netfile.readlines()]

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
run()


