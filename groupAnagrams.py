class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n=[]
        rtn=[]
        for st in strs:
            sorted(st)
            if sorted(st) in n:
                rtn[n.index(sorted(st))].append(st)
            else:
                n.append(sorted(st))   
                rtn.append([st])
        return rtn
