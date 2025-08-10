class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = []
        dire = []
        n = len(senate)
        
        for i in range(n):
            if senate[i] == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        
        r_inx = 0
        d_inx = 0
        while r_inx < len(radiant) and d_inx < len(dire):
            r = radiant[r_inx]
            d = dire[d_inx]
            
            if r < d:
                radiant.append(r + n)
            else:
                dire.append(d + n)           
            r_inx += 1
            d_inx += 1
        
        return "Radiant" if len(radiant) > len(dire) else "Dire"
