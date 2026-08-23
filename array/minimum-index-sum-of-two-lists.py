# Minimum Index Sum of Two Lists
# Difficulty: Easy
# Topics: Array, Hash Table, String

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list1_map = {string: i for i, string in enumerate(list1)}
        min_sum = float('inf')
        result = []
        
        for j, string in enumerate(list2):
            if string in list1_map:
                i = list1_map[string]
                curr_sum = i + j
                if curr_sum < min_sum:
                    min_sum = curr_sum
                    result = [string]
                elif curr_sum == min_sum:
                    result.append(string)
                    
        return result