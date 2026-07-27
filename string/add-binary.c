char* addBinary(char* a, char* b) {
    int lenA = strlen(a);
    int lenB = strlen(b);
    
    int maxLen = (lenA > lenB ? lenA : lenB);
    char* result = (char*)malloc(maxLen + 2);  // +1 for carry, +1 for '\0'
    
    int i = lenA - 1;
    int j = lenB - 1;
    int k = maxLen;
    int carry = 0;
    
    result[k + 1] = '\0';  // null terminator
    
    while (k >= 0) {
        int sum = carry;
        
        if (i >= 0) sum += a[i--] - '0';
        if (j >= 0) sum += b[j--] - '0';
        
        result[k--] = (sum % 2) + '0';
        carry = sum / 2;
    }
    
    return (result[0] == '0') ? result + 1 : result;
}