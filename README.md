<center>
    <img src="https://miro.medium.com/v2/resize:fit:1400/1*ATpj03GPME7bumMPBXoEPw.jpeg" alt="python logo" width="400"/>
</center>

# Number_Guesser_Game
This is the implementation of the number guesser game.

## Overview
This game is designed for user to guess a number within an specific range. The program generates a random number within that range so that the user should guess that number. With any incorrect guess, user loses score and receives a hint from the program untill either the user loses all of the scores or guesses the correct number.

## Directory Structure
```
Number_Guesser_Game/
|-- src/
| |-- main.py
| |-- main.ipynb
| |-- scripts/
| | |-- tools.py
|-- README.md
```

## How to Run
 1. Navigate to the main project directory(`Number_Guesser_Game`)
 2. Add the current directory to the `PYTHONPATH` and run `main.py`:
 ```
 export PYTHONPATH=$PYTHONPATH:$(pwd)
 python src/main.py
 ```
