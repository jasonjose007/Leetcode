1char* addBinary(char* a, char* b) {
2    int lenA = strlen(a);
3    int lenB = strlen(b);
4    
5    int maxLen = (lenA > lenB ? lenA : lenB);
6    char* result = (char*)malloc(maxLen + 2);  // +1 for carry, +1 for '\0'
7    
8    int i = lenA - 1;
9    int j = lenB - 1;
10    int k = maxLen;
11    int carry = 0;
12    
13    result[k + 1] = '\0';  // null terminator
14    
15    while (k >= 0) {
16        int sum = carry;
17        
18        if (i >= 0) sum += a[i--] - '0';
19        if (j >= 0) sum += b[j--] - '0';
20        
21        result[k--] = (sum % 2) + '0';
22        carry = sum / 2;
23    }
24    
25    return (result[0] == '0') ? result + 1 : result;
26}