# Accounts Merge
# Platform: LeetCode
# Difficulty: Medium
# Topics: Array, Hash Table, String, Depth-First Search, Breadth-First Search, Union-Find, Sorting

"""
This solution uses the **Disjoint Set Union (Union-Find)** algorithm with path compression, mapping unique emails to IDs and unioning all emails that appear together in the same account to identify connected components. Afterwards, it groups the emails by their root representative, sorts each group lexicographically, and pairs them with their corresponding account name. 

Where $N$ is the total number of emails across all accounts, the **time complexity is $O(N \log N)$** (dominated by sorting the emails within each component) and the **space complexity is $O(N)$** to store the mappings, Union-Find parents, and merged components.
"""

class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        parent = {}

        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j

        email_to_name = {}
        email_to_id = {}
        id_count = 0

        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in email_to_id:
                    email_to_id[email] = id_count
                    parent[id_count] = id_count
                    email_to_name[email] = name
                    id_count += 1
                union(email_to_id[account[1]], email_to_id[email])

        import collections
        components = collections.defaultdict(list)
        for email, email_id in email_to_id.items():
            root_id = find(email_id)
            components[root_id].append(email)

        res = []
        for root_id, emails in components.items():
            name = email_to_name[emails[0]]
            res.append([name] + sorted(emails))

        return res