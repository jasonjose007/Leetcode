# Kth Smallest Amount With Single Denomination Combination
# Difficulty: Hard
# Topics: Array, Math, Binary Search, Bit Manipulation, Combinatorics, Number Theory

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        import math
        
        coins = sorted(list(set(coins)))
        filtered_coins = []
        for c in coins:
            if not any(c % x == 0 for x in filtered_coins):
                filtered_coins.append(c)
        coins = filtered_coins
        n = len(coins)
        
        limit = min(coins) * k
        subsets = []
        
        def dfs(idx, current_lcm, count):
            if idx == n:
                if count > 0:
                    subsets.append((current_lcm, 1 if count % 2 == 1 else -1))
                return
            
            dfs(idx + 1, current_lcm, count)
            
            g = math.gcd(current_lcm, coins[idx])
            next_lcm = (current_lcm * coins[idx]) // g
            if next_lcm <= limit:
                dfs(idx + 1, next_lcm, count + 1)
                
        dfs(0, 1, 0)
        
        low = 1
        high = limit
        ans = limit
        
        while low <= high:
            mid = (low + high) // 2
            count = 0
            for lcm, sign in subsets:
                count += (mid // lcm) * sign
            if count >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans