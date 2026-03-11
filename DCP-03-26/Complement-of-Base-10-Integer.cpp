1class Solution {
2public:
3    int bitwiseComplement(int n) {
4    if(n==0) return 1;
5       string b=bitset<32>(n).to_string();
6       int pos=b.find('1');
7       string bin = b.substr(pos);
8       for(int i=0;bin[i];i++){
9        if(bin[i]=='0') bin[i]='1';
10        else bin[i]='0';
11       }
12
13       bitset<64> bits(bin); 
14       
15    
16    unsigned long decimalValue = bits.to_ulong();
17    return decimalValue;
18    }
19};