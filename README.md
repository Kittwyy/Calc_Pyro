# Simple Calculator with Tkinter

This is a simple calculator application built using Python and the Tkinter library. It allows users to perform basic arithmetic calculations, including addition, subtraction, multiplication, division, and square root.

## Features

*   Basic arithmetic operations (+, -, \*, /)
*   Square root calculation > Maybe some day
*   Clear entry functionality
*   Error handling for invalid input
*   Keyboard input for digits and operators > Not Working yet, working on it (maybe)
*   Equals button for calculation
*   C button for clearing the input

## How to Run

1.  Make sure you have Python installed on your system.
2.  Save the code as a `.py` file (e.g., `calculator.py`).
3.  Open a terminal or command prompt.
4.  Navigate to the directory where you saved the file.
5.  Run the application by executing the command: `python calculator.py`

## Usage

*   Enter numbers and operators using the buttons or keyboard.
*   Press the "=" button to calculate the result.
*   Press the "C" button to clear the input field.
*   Use the keyboard to enter numbers (0-9) and operators (+, -, \*, /, .).
*   Press Enter to calculate the result.
*   Press Escape to clear the input.

## Code Explanation

The code uses the `tkinter` and `ttk` (themed Tkinter) libraries for the graphical user interface.

*   `calculate()` function: Evaluates the expression in the entry field using `eval()`. Includes a nested try-except block to handle square root calculations using `math.sqrt()`.  Handles errors by displaying a humorous message.
*   `clear()` function: Clears the entry field.
*   `key_press()` function: Binds keyboard input to the entry field, allowing digits and operators to be entered directly.  Also handles Enter for calculation and Escape for clear.
*   The code creates buttons for numbers, operators, "=", and "C" and arranges them in a grid layout.
*   Button commands are linked to the respective functions (`calculate`, `clear`, and inserting numbers/operators into the entry field).

## Disclaimer

The use of `eval()` can be risky if you're accepting arbitrary input from users, as it can potentially execute malicious code.  For a more robust and secure calculator, consider using a safer parsing method for mathematical expressions.  This example is for educational purposes and demonstrates basic Tkinter functionality.  This is not intended for production environments.
