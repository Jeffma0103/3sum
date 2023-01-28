class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        if len(nums) < 3:
            return []
        else:
            for i in range(len(nums)-2):
                if i > 0 and nums[i-1] == nums[i]:
                    continue
                else:
                    j = i+1
                    k = len(nums) - 1
                    while j < k:
                        sum_nums = nums[i] + nums[j] + nums[k]
                        if sum_nums > 0:
                            k -= 1
                        elif sum_nums < 0:
                            j += 1
                        else:
                            res.append([nums[i],nums[j],nums[k]])
                            j += 1
                            while nums[j-1] == nums[j] and j < k:
                                j += 1
            return res