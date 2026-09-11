# Unique 3-Digit Even Numbers
# Difficulty: Easy
# Topics: Array, Hash Table, Recursion, Enumeration

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        digit_counts = [0] * 10
        for d in digits:
            digit_counts[d] += 1
            
        ans = 0
        for num in range(100, 1000, 2):
            d1 = num // 100
            d2 = (num // 10) % 10
            d3 = num % 10
            
            c0 = c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = 0
            
            if d1 == 0: c0 += 1
            elif d1 == 1: c1 += 1
            elif d1 == 2: c2 += 1
            elif d1 == 3: c3 += 1
            elif d1 == 4: c4 += 1
            elif d1 == 5: c5 += 1
            elif d1 == 6: c6 += 1
            elif d1 == 7: c7 += 1
            elif d1 == 8: c8 += 1
            elif d1 == 9: c9 += 1
            
            if d2 == 0: c0 += 1
            elif d2 == 1: c1 += 1
            elif d2 == 2: c2 += 1
            elif d2 == 3: c3 += 1
            elif d2 == 4: c4 += 1
            elif d2 == 5: c5 += 1
            elif d2 == 6: c6 += 1
            elif d2 == 7: c7 += 1
            elif d2 == 8: c8 += 1
            elif d2 == 9: c9 += 1
            
            if d3 == 0: c0 += 1
            elif d3 == 1: c1 += 1
            elif d3 == 2: c2 += 1
            elif d3 == 3: c3 += 1
            elif d3 == 4: c4 += 1
            elif d3 == 5: c5 += 1
            elif d3 == 6: c6 += 1
            elif d3 == 7: c7 += 1
            elif d3 == 8: c8 += 1
            elif d3 == 9: c9 += 1
            
            if (digit_counts[0] >= c0 and
                digit_counts[1] >= c1 and
                digit_counts[2] >= c2 and
                digit_counts[3] >= c3 and
                digit_counts[4] >= c4 and
                digit_counts[5] >= c5 and
                digit_counts[6] >= c6 and
                digit_counts[7] >= c7 and
                digit_counts[8] >= c8 and
                digit_counts[9] >= c9):
                ans += 1
                
        return ans