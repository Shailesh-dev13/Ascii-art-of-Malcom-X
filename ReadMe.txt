Project Title

Algorithmic Generation of ASCII Art Using Nested For-Loops and Conditional Logic

Project Description

This project demonstrates how complex ASCII art can be generated using pure Python programming logic, 
without relying on any external libraries or image-processing tools.The ASCII image is produced by iterating over a 
fixed grid of rows and columns using nested for loops.
Each character position is determined using conditional (if-elif-else) statements based on row and column indices.

The goal of this project is to showcase:

>Strong understanding of loop control
>Use of logical constructs
>Ability to design a custom algorithm


 Objectives

>To generate a structured ASCII image programmatically
>To use nested loops for grid traversal
>To apply conditional logic for character selection

 How the Code Works

1. Grid Definition

"height = 23
width = 55"

-Defines the total number of rows and columns
-Represents the ASCII canvas

2. Nested Loop Structure

"for row in range(height):
    for col in range(width):"

-Outer loop iterates row-by-row
-Inner loop iterates column-by-column
-Each iteration corresponds to one character position

3. Character Assignment Logic

"char = " " "

-Default character is space
-Changed conditionally based on (row, col)

Example:

"if row == 0:
    if col == 31:
        char = "#"
    elif 32 <= col <= 38:
        char = "@" "

This logic:
-Mimics pixel placement
-Builds the ASCII image step-by-step
-Demonstrates control flow and decision making

4. Output Rendering

"print(char, end='')
print()"

-Prints characters without moving to a new line
-After each row, moves to the next line

Algorithm

>Initialize height and width of the ASCII canvas
>Loop through each row
>Loop through each column
>Assign a character based on row and column conditions
>Print characters sequentially to form each line
>Repeat until the full ASCII image is generated


 Key Concepts Used

>Nested for loops
>if-elif-else statements
>Logical conditions
>Grid-based traversal
>Character rendering

Run using:

python mal.py

The ASCII image will be printed in the terminal

 Conclusion

This project successfully demonstrates how complex ASCII art can be generated using only Python loops and logical constructs.
It highlights problem-solving skills, algorithm design, and strict adherence to academic constraints.