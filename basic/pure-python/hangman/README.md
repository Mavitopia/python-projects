@ -0,0 +1,33 @@
# Hangman Game - ![Python](https://img.shields.io/badge/python-3.13.1-blue)

A simple **Python Hangman game** where the player tries to guess a randomly generated word before the hangman is fully drawn.  
Includes ASCII-art stages, input validation, and a dynamic game loop.

---

## Features

- Random word selection using the `random_word` module.
- **ASCII-art hangman** stages that update with each incorrect guess.    
- Input validation to accept **only single alphabetic letters**.   
- Clear win/loss messages with the secret word revealed at the end.  
- Easy-to-read and well-commented code.

---

## Requirements

- Python 3.x  
- `random-word` library: install via pip

```bash
pip install random-word
```
## How to Run

1. Clone or download the project repository.  
2. Open a terminal and navigate to the project folder.  
3. Run the game:

```bash
python hangman.py