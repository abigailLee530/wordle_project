# Wordle Solver Bot (Python)

## Overview
This project implements an automated **Wordle solver** using logic-based filtering techniques.
The solver mimics the rules of Wordle by narrowing down a list of possible words based on feedback from each guess:
- **Green** letters (correct position)
- **Yellow** letters (correct letter, wrong position)
- **Grey** letters (not in the word)

It can play the game, display its internal decision-making process, and simulate multiple games to evaluate performance.

Guess validation and feedback are retrieved from an external Wordle-checking API rather than being generated locally, so the solver is tested against a real word-checking service.

---

## Features
- Automatically plays and solves Wordle puzzles  
- Retrieves guess feedback from an external **Wordle API**  
- Implements accurate **Wordle feedback rules** (green, yellow, grey)  
- Includes a **debug mode** to visualise the solving process  
- Simulates multiple games to calculate **average performance**  
- Uses a dynamic candidate filtering approach  

---

## How It Works
The solver maintains a list of possible candidate words and progressively filters them:
1. Start with a full word list  
2. Make a guess (randomly selected from candidates)  
3. Submit the guess to the Wordle API and receive per-letter scoring (whether each letter is in the word and/or in the correct position)  
4. Parse the API response into grey, yellow, and green index lists  
5. Apply filtering rules:
   - Remove words containing invalid (grey) letters  
   - Enforce correct positions for green letters  
   - Enforce position constraints for yellow letters  
6. Repeat until the correct word is found or attempts are exhausted  

---

## Modes
- Play Mode: Simulates a standard Wordle game with up to 6 guesses.
- Debug Mode: Shows internal solver logic and remaining candidate words after each guess.
- Simulation Mode: Runs multiple games and calculates the average number of guesses.

---

## External API

This project uses a third-party Wordle-checking API to validate guesses and provide letter-by-letter feedback, rather than implementing the checking logic locally.

- **API used:** [wordle-api](https://wordle-api.vercel.app/api/wordle) (created by another developer, not authored by me)
- **Usage:** Guesses are submitted via POST request; the API returns whether the guess was correct, plus per-letter scoring (`in_word`, `correct_idx`) for each character
- **Integration:** A wrapper module (`api.py`) handles requests to the API and parses the response into grey/yellow/green index lists consumed by the solver's filtering logic

Credit for the Wordle-checking API itself goes to its original author; this project only consumes it.

---

## Key Concepts Demonstrated
- Algorithm design and optimisation
- Constraint-based filtering
- API integration and response parsing
- Simulation and performance analysis
- List manipulation and state management

---

## Possible Improvements
- Replace random guessing with frequency-based strategies
- Track win rate and distribution of guesses
- Experiment with hard coding the first few guesses with words that contain common letters and see if this produces a better average guess rate
- Add error handling / retries for API request failures

---

## Author
Abigail Lee
