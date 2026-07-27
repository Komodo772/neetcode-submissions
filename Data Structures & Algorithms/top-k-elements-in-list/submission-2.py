class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        klist = [[]for i in range(len(nums)+1)]

        for i in nums:
            hashmap[i] = 1 + hashmap.get(i, 0)
        
        for n, c in hashmap.items():
            klist[c].append(n)

        print(klist)
        res = []

        for i in range(len(klist)-1,0,-1):
            for c in klist[i]:
                res.append(c)
                if len(res) >= k:
                    return res

        ##return klist
                