class Solution:
    def romanToInt(self, s: str) -> int:
        tens=1
        total=0
        l=len(s)
        refer={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for i in range(l-1,-1,-1):
            if i!=l-1 and ((s[i]=='I' and (s[i+1]=='V' or s[i+1]=='X')) or
                (s[i]=='X' and (s[i+1]=='L' or s[i+1]=='C')) or 
                (s[i]=='C' and (s[i+1]=='D' or s[i+1]=='M'))):
                    ele=refer[s[i+1]]//refer[s[i]]
                    ele=refer[s[i+1]]//ele
                    print(ele)
                    total-=ele
                    print('0')
            else:
                total+=refer[s[i]]
        return total
                
