1class Solution:
2    def isValid(self, s: str) -> bool:
3        i=0
4        a=[]
5        for i in range(len(s)):
6            if s[i]=='('or s[i]=='['or s[i]=='{':
7                a.append(s[i])
8            else:
9                if not a:
10                    return False
11                top=a.pop()
12                if s[i]==')'and top!='(':
13                    return False
14                if s[i]==']'and top!='[':
15                    return False
16                if s[i]=='}'and top!='{':
17                    return False
18        return len(a)==0   