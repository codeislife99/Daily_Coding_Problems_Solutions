from itertools import *
from collections import *
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
    
        self.ans = []
        self.nums = nums
        self.c = Counter(self.nums)
        self.p = [0 for _ in range(len(self.nums))]
        self.permute(0,self.p)
        return self.ans
        
    def permute(self,i,p):
        if i == len(self.nums):
            self.ans.append(p)
        for key in self.c.keys():
            if self.c[key]>0:
                self.c[key] -= 1
                p[i] = key
                self.permute(i+1,list(p))
                self.c[key] += 1
                