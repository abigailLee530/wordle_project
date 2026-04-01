# Wordle Solver Bot (Python)

## Overview
This project implements an automated **Wordle solver** using logic-based filtering techniques.

The solver mimics the rules of Wordle by narrowing down a list of possible words based on feedback from each guess:
- **Green** letters (correct position)
- **Yellow** letters (correct letter, wrong position)
- **Grey** letters (not in the word)

It can play the game, display its internal decision-making process, and simulate multiple games to evaluate performance.

---

## Features
- Automatically plays and solves Wordle puzzles  
- Implements accurate **Wordle feedback rules** (green, yellow, grey)  
- Includes a **debug mode** to visualise the solving process  
- Simulates multiple games to calculate **average performance**  
- Uses a dynamic candidate filtering approach  

---

## How It Works
The solver maintains a list of possible candidate words and progressively filters them:

1. Start with a full word list  
2. Make a guess (randomly selected from candidates)  
3. Apply filtering rules:
   - Remove words containing invalid (grey) letters  
   - Enforce correct positions for green letters  
   - Enforce position constraints for yellow letters  
4. Repeat until the correct word is found or attempts are exhausted  

---

## Modes

Play Mode: Simulates a standard Wordle game with up to 6 guesses.
Debug Mode: Shows internal solver logic and remaining candidate words after each guess.
Simulation Mode: Runs multiple games and calculates the average number of guesses.

---

## Key Concepts Demonstrated
- Algorithm design and optimisation
- Constraint-based filtering
- Simulation and performance analysis
- List manipulation and state management

---

## Possible Improvements
- Replace random guessing with frequency-based strategies
- Add a graphical interface or web-based version
- Track win rate and distribution of guesses
- Experiment with hard coding the first few guesses with words that contain common letters and see if this produces a better average guess rate

---

## Author
Abigail Lee
