# Basic Calculator II
# Platform: LeetCode
# Difficulty: Medium
# Topics: Math, String, Stack

"""
This solution uses a stack-based algorithm to evaluate the mathematical expression by iterating through each character and keeping track of the `current_number` and the most recent preceding `operator`. When a new operator is reached (or at the end of the string), addition and subtraction push numbers directly to the stack (with negative signs for subtraction), while multiplication and division immediately pop the last number from the stack, perform the operation with the `current_number`, and push the result back. Finally, the sum of all elements in the stack is returned, resulting in a **$O(n)$ time complexity** and **$O(n)$ space complexity** for iterating through the string and storing values in the stack.
"""

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_number = 0
        operator = '+'
        n = len(s)
        
        for i, char in enumerate(s):
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            
            if (not char.isdigit() and char != ' ') or i == n - 1:
                if operator == '+':
                    stack.append(current_number)
                elif operator == '-':
                    stack.append(-current_number)
                elif operator == '*':
                    stack.append(stack.pop() * current_number)
                elif operator == '/':
                    prev = stack.pop()
                    if prev < 0:
                        stack.append(-(-prev // current_number))
                    else:
                        stack.append(prev // current_number)
                
                operator = char
                current_number = 0
                
        return sum(stack)