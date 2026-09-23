class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s+=f"{i}|-|"
        return s
    def decode(self, s: str) -> List[str]:
        l=[]
        st=""
        return s.split("|-|")[:-1]
        for i in range(len(s)):
            if s[i] == "-":
                
                l.append(s[i+2:i+2+int(s[i+1])])

        return l