# Evaluate the Bracket Pairs of a String
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Hash Table, String

"""
The algorithm converts the `knowledge` pairs into a hash map for $O(1)$ lookups and iterates through the string $s$ sequentially using a boolean flag to track whether it is inside a bracket pair. Characters inside brackets are accumulated into a key to be looked up in the map (defaulting to `'?'`) upon encountering `')'`, while characters outside are directly appended to the output list. 

Both the time and space complexity are **$O(N + M)$**, where $N$ is the length of $s$ and $M$ is the total length of characters across all pairs in `knowledge`, needed for the single-pass traversal and storing the map and result.
"""

class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d = dict(knowledge)
        ans = []
        in_bracket = False
        cur_key = []
        
        for ch in s:
            if ch == '(':
                in_bracket = True
                cur_key = []
            elif ch == ')':
                in_bracket = False
                ans.append(d.get("".join(cur_key), '?'))
            else:
                if in_bracket:
                    cur_key.append(ch)
                else:
                    ans.append(ch)
                    
        return "".join(ans)