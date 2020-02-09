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