# Challenge Summary

<!-- Description of the challenge -->

Write a function called validate brackets
representing whether or not the brackets in the string are balanced There are 3 types of brackets:
Round Brackets : ()
Square Brackets : []
Curly Brackets : {}
Arguments: string
Return: boolean

## Whiteboard Process

<!-- Embedded whiteboard image -->

![whiteboard](../validate_brackets/stack-queue-brackets.png)

## Approach & Efficiency

<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

Utitlize the isEmpty method.

-   declare a validate_bracket function that takes string input.
-   declare a dictionary with all opening brackets as keys and closing brackets as values.
-   loop through the string and if there is a dictionary key <-- append
    \*else if stack is empty <-return false.
-   temp to store the closing popped bracket.
-   if the temp doesn't match the value of the key <- return False.
    Return False if the stack is empty and there is a closing bracket left.
-   else return True

Big O
time: O(n) one for loop through the whole string
space: O(n) storing every bracket

## Solution

<!-- Show how to run your code, and examples of it in action -->
