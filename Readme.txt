Name: Jinesh Modi
UTA ID: 1001622464

Programming Language Used: Python

Code Structure:
All the files contains proper commenting.
It contains 5 files:
1) "maxconnect4.py" - it is the main file for running the program
2) "MaxConnect4Game.py" - It contains the game structure
3) "AlphaBetaDecision.py" - It is implements the alpha-beta algorithm
4) "ExecutionTime.xlsx" - It contains the table of depth limit vs runtime
5) "Eval_explanation.txt" - It contains description of eval function

Few changes are made in "MaxConnect4Game.py":
1) Added a function for eval
2) "checkPieceCount" also returns piece count apart from calculating it
3) Added depth limit variable in init function

Changes are made in "maxconnect4.py":
1) Changed a bit in main function to read depth limit
2) Modified one-move function
3) Added logic in interactive function

Added new file "AlphaBetaDecision.py" it contains 4 functions:
1) "AlphaBetaDecision" - It is main function to start alpha-beta
2) "MaxValue" - Finds maximum value from it's immediate children
3) "MinValue" - Finds minimum value from it's immediate chlidren
4) "Successors" - It finds the immediate successors of a given state

How to run the code?
The supporting files "MaxConnect4Game.py", "AlphaBetaDecision.py", input file and output file should be in same folder in which "maxconnect4.py" is in.
Run program using exactly following format for one-move game format:
"python maxconnect4.py one-move input1.txt output1.txt 4"
In above line "input1.txt" is the input file, it can be any name, "output1.txt" is the output file, it can be any name and "4" is the depth limit.
Run program using exactly following format for interactive game format:
"python maxconnect4.py interactive input1.txt computer-first 4"
In above line "input1.txt" is the input file, it can be any name, "computer-first" is the flag that who plays first, it can also be "human-first" and "4" is the depth limit.
No additional compile command is required, it is compatible with Omega's python version 2.4.3 and will run smoothly on it.