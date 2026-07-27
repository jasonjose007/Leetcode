class Solution {
public:
    int bitwiseComplement(int n) {
    if(n==0) return 1;
       string b=bitset<32>(n).to_string();
       int pos=b.find('1');
       string bin = b.substr(pos);
       for(int i=0;bin[i];i++){
        if(bin[i]=='0') bin[i]='1';
        else bin[i]='0';
       }

       bitset<64> bits(bin); 
       
    
    unsigned long decimalValue = bits.to_ulong();
    return decimalValue;
    }
};