class Solution:
    def romanToInt(self, s: str) -> int:
        mapy={
            "I":1,
            "V":5,"X":10,"L":50,"C":100,"D":500,"M":1000
        }
        val=0
        for i in range(len(s)):
            if (i+1<len(s) and mapy[s[i+1]]>mapy[s[i]]):
                val-=mapy[s[i]]
            else:
                val+=mapy[s[i]]
        return val

            