# wordle-solver
Simple CLI utility to help you solve Wordle puzzles.

## Requirements 📦
Requires Python 3.x, as well as package requirements listed in `requirements.txt`.

To install required packages (after cloning and navigating to project directory):
`pip install -r requirements.txt`

**Note:** doing this in a virtual or conda environment is recommended.
## Installation and run instructions
`git clone https://github.com/cjporteo/wordle-solver.git`
`cd wordle-solver`
`python wordle.py`

## Syntax for entering clues
 - 🟢 **Green** (right letter, right place): enter letter in upper case, e.g. `A`
 - 🟡 **Yellow** (right letter, wrong place): enter letter in lower case, followed by an asterisk, e.g. `a*`
 - ⚫ **Black** (letter is not in word): enter letter in lower case, with no asterisk, e.g.`a`

### Example
![](https://raw.githubusercontent.com/cjporteo/wordle-solver/main/readme_assets/example.png)
`b O U r n*`

## Sample usage ⌨️
Candidate words are provided in a random order, but arranged to give priority to words with a higher number of unique letters, with the idea that these will lead to more insightful clues.

For this sample exercise, the first candidate word is always the one chosen as the next guess. This is done for simplicity, but isn't required.

![](https://raw.githubusercontent.com/cjporteo/wordle-solver/main/readme_assets/app_1.png)<br /> <br /> 
![](https://raw.githubusercontent.com/cjporteo/wordle-solver/main/readme_assets/phone_1.png)<br /> <br /> 
![](https://raw.githubusercontent.com/cjporteo/wordle-solver/main/readme_assets/app_2.png)<br /> <br /> 
![](https://raw.githubusercontent.com/cjporteo/wordle-solver/main/readme_assets/phone_2.png)<br /> <br /> 
![](https://raw.githubusercontent.com/cjporteo/wordle-solver/main/readme_assets/app_3.png)<br /> <br /> 
![](https://raw.githubusercontent.com/cjporteo/wordle-solver/main/readme_assets/phone_3.png)<br /> <br /> 
![](https://raw.githubusercontent.com/cjporteo/wordle-solver/main/readme_assets/app_4.png)<br /> <br /> 
![](https://raw.githubusercontent.com/cjporteo/wordle-solver/main/readme_assets/phone_4.png)<br /> <br /> 
![](https://raw.githubusercontent.com/cjporteo/wordle-solver/main/readme_assets/app_5.png)<br /> <br /> 
![](https://raw.githubusercontent.com/cjporteo/wordle-solver/main/readme_assets/phone_5.png)<br /> <br /> 
## Some implementation details 👓

 - There's no guarantee that the word list used in this exercise is 1:1 with the one used on Wordle's backend. This means that this utility might sometimes suggest candidate words that aren't considered valid by Wordle. It's also possible (but highly unlikely) that a target word in Wordle might not be included in our word list.
 - Ordering of candidate words only considers number of unique letters (words with more unique letters are prioritized). In the future, a letter scoring system could be implemented to give further priority to words with common letters so that our guesses can be more reductive.

## What's next? ⏱️
I'd like to build upon this utility and develop it into an analysis piece, hopefully being able to concretely outline strong Wordle guessing strategies (probably using Monte-Carlo and minimax trees to achieve this, not quite sure).

Also, wrapping this utility into a frontend service would be another good next step.

> Written with [StackEdit](https://stackedit.io/).
