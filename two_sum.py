class Solution(object):
    def twoSum(self, nums, target):
        length = len(nums)
        for i in range(0,length -1):
            for j in range(i+1,length):
                if ( i != j and (nums[i] + nums[j] ) == target ):
                    return [i,j]
        return []
