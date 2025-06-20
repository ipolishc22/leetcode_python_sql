# 15. 3Sum
#
# Time complexity: O(n^2 )
# Space complexity: O(1) or O(n) depending on the sorting algorithm 

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()

        for index, value in enumerate(nums):
            if index > 0 and value == nums[index-1]:
                continue

            left = index + 1
            right = len(nums) - 1

            while left < right:

                threeSum = value + nums[left] + nums[right]

                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    res.append([value, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1

        return res