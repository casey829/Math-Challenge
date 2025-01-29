# Math Quiz Game

This project is a simple command-line math quiz game implemented in Python. It generates random arithmetic problems for the user to solve and tracks the total time taken to complete all problems.

## Features

. Randomly generates arithmetic problems using addition (+), subtraction (-), multiplication (*), and division (/).

. Ensures division problems always yield integer results.

. Allows the user to answer a total of 10 questions.

. Tracks the number of incorrect answers.

. Measures the total time taken to complete the quiz.

## How It Works

1. The program starts after the user presses Enter.

2. It generates a random math problem and prompts the user to input their answer.

3. If the answer is incorrect, the user is prompted to try again, and the incorrect answer count increases.

4. Once all questions are answered correctly, the program displays the total time taken to complete the quiz.

## Code Breakdown

### Constants

. OPERATORS: A list of supported arithmetic operators (+, -, *, /).

. MIN_OPERAND and MAX_OPERAND: Define the range for randomly generated operands (2 to 15).

. TOTAL_PROBLEMS: The number of math problems in the quiz (10).

## Functions

generate_problem()

Generates a random math problem by:

. Selecting two random operands within the specified range.

. Selecting a random operator from the list.

. Constructing an expression string and evaluating its answer using eval().

. Ensures division problems produce integer results by validating left % right == 0.

## Main Logic

. The user starts the quiz by pressing Enter.

. The for loop iterates through the number of problems (TOTAL_PROBLEMS).

. For each problem:

   . The user is presented with the expression.

   . The program waits for the correct answer.

    . If the answer is incorrect, the user is prompted again, and the incorrect count (wrong) increments.

. After the quiz, the program calculates and displays the total time taken.

## Requirements

. Python 3.6 or later

## How to Run

1. Copy the code into a Python file (e.g., math_quiz.py).

2. Run the script using the following command:

python math_quiz.py

3. Follow the on-screen instructions to complete the quiz.

## Example Output

Press enter to start!
____________
Question #1: 12 / 3 = 4
Question #2: 7 + 6 = 13
...
_________
Good job you finished in 45.67 seconds!

## Notes

. The program uses eval() to evaluate the math expression. While it is safe in this context due to controlled input, avoid using eval() with untrusted input in real-world applications.

. The quiz ensures the user provides the correct answer before proceeding to the next question.

## Future Improvements

. Provide a summary of the user's performance, including the number of incorrect attempts.

. Allow users to configure the number of problems and operand range.

