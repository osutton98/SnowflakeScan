# SnowflakeScan
Write a scanner that can be used as the first phase of a Snowflake compiler. The scanner takes the source code of a Snowflake program as input and generates a list of tokens. The scanner should be written as a method that returns a list of tokens (your choice of data structure) and has an input parameter of the source code, which can be either a string containing the file name, a string containing the full input source code, a File object, an array of strings or any other suitable format. Write a simple main program to test your scanner and display the resulting list of tokens in any easily understandable way.
The scanner must remove the white space and comments from the input and return a list of the tokens. You can define token objects as you see fit, but they must contain the row and column of the source code where the object originated.
Comments in the Snowflake language have two formats:
• A single hash or pound sign, #, which starts a comment until the end of the line.
• A hash followed by an exclamation point, #!, which starts a comment until !#
The Snowflake language contains variables that consist of upper and lower case letters and numerical digits. Variables must start with a letter and are case insensitive. The source language may contain quote strings that start and end with the ‘single quote’ character. The case of string constants must be preserved. Quote strings may not extend past the end of the line.
The scanner must accept the following punctuation characters. Any other characters should be flagged as syntax errors. Tokens should be created from the single punctuation characters.
= equal sign
; semicolon
{ left curly bracket } right curly bracket | vertical bar
Single quotes are used to start and end a string constant. A single token should be created for the string without including the quotes.
If your scanner detects a syntax error, it must produce a reasonable error message that indicates the location of the error in the source code file.
#Hints
Hints on creating a scanner
The first step in creating a scanner is to draw an FSA diagram. Create a Mealy machine by assigning actions to each of the arrows. Convert the circle and arrow drawing to two tables, one specifying the new state given the current state and input symbol, the other specifying the action to be taken given the current state and input symbol.
You will need to read the input one character at a time.
In Java, this can be done with the read() method of a BufferedReader. java.io.BufferedReader inFile = new java.io.BufferedReader(new java.io.FileReader(“snow.txt”));
In C++ you can use the getc function. You will probably want to cast the return value to a char after checking for an end of file.
You will probably want to group the input characters to use a single index into the state table for similar characters. In Java, you can tell is a character is a
letter number whitespace in C++: letter number
Character.isLetter( char )
Character.isDigit( char )
Character.isWhitespace( char )
int isalpha ( int c );
int isdigit ( int c );
A general outline of the scanner might be:
state = 0
while not EOF
read a character
assign inIndex depending on the type of input character action = actionTable[state, inIndex];
state = stateTable[state, inIndex];
switch ( action )
case 0: Do this
case 1: Do that