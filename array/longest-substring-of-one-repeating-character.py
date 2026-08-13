# Longest Substring of One Repeating Character
# Difficulty: Hard
# Topics: Array, String, Segment Tree, Ordered Set

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        tree = [None] * (4 * n)
        
        def merge(left, right):
            l_max, l_pchar, l_plen, l_schar, l_slen, l_sz = left
            r_max, r_pchar, r_plen, r_schar, r_slen, r_sz = right
            
            res_sz = l_sz + r_sz
            res_pchar = l_pchar
            res_plen = l_plen + r_plen if l_plen == l_sz and l_pchar == r_pchar else l_plen
            res_schar = r_schar
            res_slen = r_slen + l_slen if r_slen == r_sz and r_schar == l_schar else r_slen
            
            res_max = l_max if l_max > r_max else r_max
            if l_schar == r_pchar:
                combined = l_slen + r_plen
                if combined > res_max:
                    res_max = combined
                
            return [res_max, res_pchar, res_plen, res_schar, res_slen, res_sz]

        def build(node, start, end):
            if start == end:
                tree[node] = [1, s[start], 1, s[start], 1, 1]
                return
            mid = (start + end) // 2
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)
            tree[node] = merge(tree[2 * node], tree[2 * node + 1])

        def update(node, start, end, idx, val):
            if start == end:
                tree[node] = [1, val, 1, val, 1, 1]
                return
            mid = (start + end) // 2
            if idx <= mid:
                update(2 * node, start, mid, idx, val)
            else:
                update(2 * node + 1, mid + 1, end, idx, val)
            tree[node] = merge(tree[2 * node], tree[2 * node + 1])

        build(1, 0, n - 1)
        
        ans = []
        for char, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, char)
            ans.append(tree[1][0])
            
        return ans