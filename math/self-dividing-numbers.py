# Self Dividing Numbers
# Difficulty: Easy
# Topics: Math

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def is_self_dividing(n: int) -> bool:
            temp = n
            while temp > 0:
                d = temp % 10
                if d == 0 or n % d != 0:
                    return False
                temp //= 10
            return True
        
        return [x for x in range(left, right + 1) if is_self_dividing(x)]