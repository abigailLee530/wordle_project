"""
Wordle Solver Bot
Author: Abigail Lee
Date: 2026-03-13
Description: Automatically plays and solves Wordle using logic-based filtering.
             Includes modes for debugging and player view.
             Includes simulation methods to find average number of attempts.
"""

import random as rnd
import api

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




def filter_grey_letters(guess, grey_positions):
    """
    Remove words that contain letters not present in the target word (grey letters).
    Implements Wordle's 'grey' filtering rule.
    """

    words_to_remove = []

    # Mark candidate words containing grey letters for removal
    for word in candidate_words:
        for index in grey_positions:
            if guess[index] in word:
                words_to_remove.append(word)
                break

    # Remove invalid words from candidate list
    for word in words_to_remove:
        candidate_words.remove(word)


def filter_yellow_letters(guess, yellow_positions):
    """
    Remove words that violate 'yellow letter' rules:
    - Must contain the letter
    - Must not have the letter in the same position as in the guess
    """
    
    words_to_remove = []

    # Filter out words that do not satisfy yellow letter rules
    for word in candidate_words:
        for idx in yellow_positions:
            if guess[idx] not in word or guess[idx] == word[idx]:
                words_to_remove.append(word)
                break

    for word in words_to_remove:
        candidate_words.remove(word)


def filter_green_letters(guess, green_positions):
    """
    Remove words that do not match confirmed green letters:
    - Letters correctly guessed in the correct positions
    """

    words_to_remove = []

    # Remove words that do not match green letter positions
    for word in candidate_words:
        for idx in green_positions:
            if guess[idx] != word[idx]:
                words_to_remove.append(word)
                break

    for word in words_to_remove:
        candidate_words.remove(word)


def show_play():
    """
    Simulate a Wordle game while showing the solver's internal process:
    - Displays each guess and the target word
    - Shows remaining candidate words after filtering
    - Useful for debugging or demonstration purposes
    """
    g = pick_next_guess()
    correct = api.isCorrect(g)
    current_attempts = 1

    while not correct and current_attempts <= 6:
        print("Guess " + str(current_attempts) + ": " + g)
        
        grey, yellow, green = api.formatResponse(api.guess(g))

        filter_green_letters(g, green)
        filter_yellow_letters(g, yellow)
        filter_grey_letters(g, grey) 

        print("Remaining candidate words:", candidate_words)
        print()
        
        g = pick_next_guess()
        if(g == "word not in word bank"):
            print(g)
            return
        correct = api.isCorrect(g)
        current_attempts += 1

    print("Correct! The word is: " + g)


def play():
    """
    Simulate a Wordle game from a player's perspective:
    - Maximum of 6 guesses
    - Applies filtering rules after each guess
    """
    global candidate_words
    candidate_words = word_bank.copy()  # Reset candidate words for each game
    
    g = pick_next_guess()
    correct = api.isCorrect(g)
    current_attempts = 1

    while not correct and current_attempts <= 6:
        print("Guess " + str(current_attempts) + ": " + g)
        
        grey, yellow, green = api.formatResponse(api.guess(g))

        filter_green_letters(g, green)
        filter_yellow_letters(g, yellow)
        filter_grey_letters(g, grey)

        g = pick_next_guess()
        if(g == "word not in word bank"):
            print(g)
            return
        
        correct = api.isCorrect(g)
        current_attempts += 1

    print("Guess " + str(current_attempts) + ": " + g)
    print("Correct! The word is: " + g)


def simulate_single_game_attempts():
    """
    Simulate a single Wordle game without printing output.
    Returns the total number of attempts taken to guess the target word.
    
    Resets the candidate words list at the start of each simulation to ensure
    independent, accurate results.
    """
    global candidate_words
    candidate_words = word_bank.copy()  # Reset candidate words for this game

    g = pick_next_guess()
    correct = api.isCorrect(g)
    current_attempts = 1

    while not correct and current_attempts <= 6:
        
        grey, yellow, green = api.formatResponse(api.guess(g))

        filter_green_letters(g, green)
        filter_yellow_letters(g, yellow)
        filter_grey_letters(grey)

        g = pick_next_guess()
        if(g == "word not in word bank"):
            print(g)
            return
        correct = api.isCorrect(g)
        current_attempts += 1


    return attempts


def simulate_multiple_games(n):
    """
    Simulate 'n' Wordle games and calculate the average number of guesses needed.
    
    Calls simulate_single_game_attempts() for each game and tracks attempts.
    Prints the average guesses over all simulations.
    
    Parameters:
        n (int): The number of games to simulate.
    """
    total_attempts = 0

    for i in range(n):
        total_attempts += simulate_single_game_attempts()

    average_guesses = total_attempts / n
    print("The average number of guesses over",n, "simulated games is:",average_guesses, "attempts.")   
      
        

#Uncomment to play
play()

# Uncomment to see internal solver process
#show_play()

#Uncomment to simulate 1000 game plays to find the average number of attempts needed to guess the word.
#simulate_multiple_games(1000)

