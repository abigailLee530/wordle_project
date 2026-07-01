"""
Wordle API Client
Author: Abigail Lee
Date: 02-07-2026
Description: Provides a thin wrapper around the external Wordle-checking API
             (https://wordle-api.vercel.app/api/wordle). Submits guesses via
             HTTP POST requests and parses the returned per-letter feedback
             (in_word, correct_idx) into grey/yellow/green index lists that
             can be consumed by the candidate-filtering logic in the solver.
"""

import requests

url = "https://wordle-api.vercel.app/api/wordle"

def guess(word):
    """
    Submit a guess to the Wordle API and return the raw response.

    Args:
        word (str): The 5-letter word to guess.

    Returns:
        dict: The parsed JSON response from the API, containing at minimum:
            - "was_correct" (bool): Whether the guess matched the target word.
            - "character_info" (list): Per-letter scoring info, where each
              item has a "char" and a "scoring" dict with "in_word" and
              "correct_idx" boolean flags.
    """
    data = {"guess": word}
    response = requests.post(url, json=data)
    return response.json()
    

def formatResponse(response_dict):
    """
    Convert a raw API response into grey/yellow/green index lists.

    Classifies each letter position in the guess based on the API's
    scoring:
        - Green:  letter is in the word AND in the correct position.
        - Yellow: letter is in the word BUT in the wrong position.
        - Grey:   letter is not in the word.

    Args:
        response_dict (dict): The response dict returned by guess(),
            expected to contain "was_correct" and "character_info".

    Returns:
        tuple[list[int], list[int], list[int]] | None:
            A tuple of (grey, yellow, green) index lists, where each list
            contains the 0-based positions in the guess matching that
            category. Returns None if the guess was already correct
            (i.e. no filtering is needed).
    """
    if response_dict.get("was_correct"):
        return None

    chars = response_dict.get("character_info")
    
    grey = []
    yellow = []
    green = []
    index = 0
    
    for item in chars:
        
        scores = item.get("scoring")
        
        if scores.get("in_word") == True and scores.get("correct_idx") == True:
            green.append(index)
        
        elif scores.get("in_word") == True and scores.get("correct_idx") == False:
            yellow.append(index)
        
        else:
            grey.append(index)
        
        index+=1
    return grey, yellow, green
