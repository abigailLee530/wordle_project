#program to run a wordle game and solve the word

import random as rnd

text = open('wordle_words.txt')
pos_words = text.read().split("\n")
filtered = pos_words


#Prints all the the words from the wordle word bank
def print_words():
    for word in pos_words:
        print(word)

#Picks the next guess from remaining possible words 
def pick_next_guess():
    guess = rnd.choice(filtered)
    return guess
    
#Picks the target word that the bot will try to guess   
def pick_target_word():
   word = rnd.choice(pos_words)
   return word

#Filters out the grey letters and the words that contain these letters 
def filter_grey(target, guess):
    grey = []
    new_filtered = []
    for letter in guess:
        if letter not in target and letter not in grey:
            grey.append(letter)
    
    for word in filtered:
        for letter in grey:
            if letter in word:
                new_filtered.append(word)
                break
   
    for word in new_filtered:
        filtered.remove(word)                

#filters out the guessing nopt containing the yellow letters or containing the yellow letters in the same position
def filter_yellow(target, guess):
    yellow = []
    new_filtered = []
    
    for i in range(0,5):
        if guess[i] != target[i] and guess[i] in target:
            yellow.append(i)
    
    for word in filtered:
        for index in yellow:
            #print(word, index)
            if guess[index] not in word or guess[index] == word[index]:
                new_filtered.append(word)
                break
    
    for word in new_filtered:
        filtered.remove(word)

#filters out the words not contianing the green letters at the correct index
def filter_green(target, guess):
    green = []
    for i in range(0, 5):
        if guess[i] == target[i]:
            green.append(i)
    
    new_filtered = []
    for word in filtered:
        for index in green:
            if target[index] != word[index]:
                new_filtered.append(word)
                break
    
    for word in new_filtered:
        filtered.remove(word)

#simulates a round of wordle showing the bots working
def show_play():
    target = pick_target_word()
    guess = pick_next_guess() 
    while guess != target:
        print("Guess: " + guess)
        print(target)
        filter_green(target, guess)
        filter_yellow(target, guess)
        filter_grey(target, guess)
        
        print(filtered)
        print()
        guess = pick_next_guess()
    print("Correct! The word is: " + guess)
    print("Check: "+target)
            
#simulates a round of wordle as the user sees it            
def play():
    target = pick_target_word()
    guess = pick_next_guess()
    index = 1
    while guess != target and index <=6 :
        print("Guess " + str(index) +": " + guess)
        filter_green(target, guess)
        filter_yellow(target, guess)
        filter_grey(target, guess)
        guess = pick_next_guess()
        index+=1
    print("Guess " + str(index) +": " + guess)
    print("Correct! The word is: " + guess)



#show_play()
play()