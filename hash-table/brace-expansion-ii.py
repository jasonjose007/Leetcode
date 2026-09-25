# Brace Expansion II
# Platform: LeetCode
# Difficulty: Hard
# Topics: Hash Table, String, Backtracking, Stack, Breadth-First Search, Sorting

"""
This solution uses a recursive descent parsing approach with a stack to evaluate the expression according to the order of operations (concatenation over union). It tracks brace nesting levels to correctly isolate comma-separated groups and inner expressions, recursively solving them into sets of strings. Due to the nested expansions and combinations of string sets, the time and space complexity are exponential in the worst-case length of the expression.
"""

class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def parse(s: str) -> set[str]:
            stack = [[]]
            level = 0
            curr = []
            
            i = 0
            while i < len(s):
                c = s[i]
                if c == '{':
                    if level == 0:
                        if curr:
                            stack[-1].append(curr)
                            curr = []
                    else:
                        curr.append(c)
                    level += 1
                    if level > 1:
                        pass
                elif c == '}':
                    level -= 1
                    if level == 0:
                        stack[-1].append(parse("".join(curr)))
                        curr = []
                    else:
                        curr.append(c)
                elif c == ',':
                    if level == 0:
                        if curr:
                            stack[-1].append(curr)
                            curr = []
                        stack.append([])
                    else:
                        curr.append(c)
                else:
                    if level == 0:
                        curr.append(c)
                    else:
                        curr.append(c)
                i += 1
            
            if curr:
                stack[-1].append(curr)
                
            res = set()
            for group in stack:
                if not group:
                    continue
                prod = {''}
                for item in group:
                    if isinstance(item, list):
                        chars = "".join(item)
                        prod = {a + chars for a in prod}
                    else:
                        prod = {a + b for a in prod for b in item}
                res.update(prod)
            return res

        return sorted(list(parse(expression)))