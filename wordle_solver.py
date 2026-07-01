"""
Wordle Solver Bot
Author: Abigail Lee
Date: 02-07-2026
Description: Automatically plays and solves Wordle using logic-based filtering.
             Guesses and feedback are retrieved via calls to an external
             Wordle-checking API, which returns per-letter scoring (in_word,
             correct_idx) that is parsed into grey/yellow/green index lists.
             Includes modes for debugging and player view.
             Includes simulation methods to find average number of attempts.
"""

import random as rnd
import api
from collections import Counter

# Load the list of possible Wordle words from file
text = open('wordle_words.txt')
word_bank = text.read().split("\n")

# List of candidate words remaining after applying filtering rules
candidate_words = word_bank.copy()



def print_word_bank():
    """
    Display all words in the Wordle word bank.
    Useful for verifying the dataset or debugging.
    """
    for word in word_bank:
        print(word)


def pick_next_guess():
    """
    Select the next guess randomly from the remaining candidate words.
    """
    if(len(candidate_words) ==0):
        return "word not in word bank"
    else:
        return rnd.choice(candidate_words)
    
def filter_candidates(guess, grey_positions, yellow_positions, green_positions):
    """
    Filters the candidate_word list, removing words that do not fit all of the green
    yellow and grey rules.
    
    """
    #Tracks the number of allowed instance of a letter in the target word
    counts = Counter()

    for idx in yellow_positions + green_positions:
        counts[guess[idx]]+=1
    
    words_to_remove = []
    
    #Determine if a word in the candidate_word list is valid according to the green, yellow and grey rules
    for word in candidate_words:
        if not isValid(word, guess, grey_positions, yellow_positions, green_positions, counts):
            words_to_remove.append(word)
    
    # Remove invalid words from candidate list
    for word in words_to_remove:
        candidate_words.remove(word)
        

def isValid(word, guess, grey_positions, yellow_positions, green_positions, counts):
    """
    Determines whether a word in the candidate_word list is still valid given
    the information returned from the api call.
    
    Word remains in candidate_word list if it satisfys the green, yellow and grey rules
    else it is removed.
    
    """
    
    # Filter out words that do not satisfy the green letter rules
    for idx in green_positions:
        if guess[idx] != word[idx]:
            return False
    
    # Filter out words that do not satisfy the yellow letter rules
    for idx in yellow_positions:
        if guess[idx] not in word or guess[idx] == word[idx]:
            return False
    
    # Filter out words that do not satisfy the grey letter rules
    for idx in grey_positions:
        letter = guess[idx]
        allowed = counts[letter] 
        
        #Letter is not in target word
        if allowed == 0:
            if letter in word:
                return False
        
        # If letter occurs more times then allowed, then word is invalid 
        elif word.count(letter) > allowed:
            return False
        
    return True
    

def show_play():
    """
    Simulate a Wordle game while showing the solver's internal process:
    - Displays each guess 
    - Shows remaining candidate words after filtering
    - Useful for debugging or demonstration purposes
    """
    g = pick_next_guess()
    response = api.guess(g)              
    correct = response.get("was_correct")
    current_attempts = 1

    while not correct and current_attempts <= 6:
        print("Guess " + str(current_attempts) + ": " + g)
        
        grey, yellow, green = api.formatResponse(api.guess(g))

        filter_candidates(g, grey, yellow, green)

        print("Remaining candidate words:", candidate_words)
        print()
        
        g = pick_next_guess()
        if(g == "word not in word bank"):
            print(g)
            return
        
        response = api.guess(g)          
        correct = response.get("was_correct")
        current_attempts += 1

    if current_attempts <= 6:
        print("Guess " + str(current_attempts) + ": " + g)
        print("Correct! The word is: " + g)
    
    else:
        print("Word not found")


def play():
    """
    Simulate a Wordle game from a player's perspective:
    - Maximum of 6 guesses
    - Applies filtering rules after each guess
    """
    global candidate_words
    candidate_words = word_bank.copy()  # Reset candidate words for each game
    
    g = pick_next_guess()
    response = api.guess(g)
    correct = response.get("was_correct")
    current_attempts = 1

    while not correct and current_attempts <= 6:
        print("Guess " + str(current_attempts) + ": " + g)
        
        grey, yellow, green = api.formatResponse(api.guess(g))
        filter_candidates(g, grey, yellow, green)
        g = pick_next_guess()
        
        if(g == "word not in word bank"):
            print(g)
            return
        
        response = api.guess(g)   
        correct = response.get("was_correct")
        current_attempts += 1
    
    print("Guess " + str(current_attempts) + ": " + g)
    
    if(current_attempts <=6):
        print("Correct! The word is: " + g)
    else:
        print("Word not found")


def simulate_single_game():
    """
    Simulate a single Wordle game without printing output.
    Returns the total number of attempts taken to guess the target word.
    
    Resets the candidate words list at the start of each simulation to ensure
    independent, accurate results.
    """
    global candidate_words
    candidate_words = word_bank.copy()  # Reset candidate words for this game

    g = pick_next_guess()
    response = api.guess(g)
    correct = response.get("was_correct")
    current_attempts = 1

    while not correct and current_attempts <= 6:
        
        grey, yellow, green = api.formatResponse(api.guess(g))
        filter_candidates(g, grey, yellow, green)

        g = pick_next_guess()
        
        if(g == "word not in word bank"):
            print(g)
            return -1
        
        response = api.guess(g)
        correct = response.get("was_correct")
        current_attempts += 1

    return current_attempts


def simulate_multiple_games(n):
    """
    Simulate 'n' Wordle games and calculate the average number of guesses needed.
    
    Calls simulate_single_game() for each game and tracks attempts.
    Prints the average guesses over all simulations.
    
    Parameters:
        n (int): The number of games to simulate.
    """
    total_attempts = 0

    for i in range(n):
        attempt = simulate_single_game()
        if attempt == -1:
            return
        total_attempts += attempt

    average_guesses = total_attempts / n
    print("The average number of guesses over",n, "simulated games is:",average_guesses, "attempts.")   
      
        

#Uncomment to play
play()

# Uncomment to see internal solver process
#show_play()

#Uncomment to simulate 100 game plays to find the average number of attempts needed to guess the word.
#simulate_multiple_games(100)

