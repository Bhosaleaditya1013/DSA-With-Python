class Solution:
    
    def twoSum(self,listofnum,target):
        checker = {}

        for i in range(len(listofnum)):
            first = listofnum[i]
            second = target- first

            if second in checker:
                return[checker[second], i]

            checker[first]= i



print(Solution().twoSum([2,7,11,15], 9))
