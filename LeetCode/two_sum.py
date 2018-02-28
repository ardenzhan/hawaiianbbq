# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

def twoSum(nums, target):
  """
  :type nums: List[int]
  :type target: int
  :rtype: List[int]
  """
  for num in nums:
    remaining_nums = nums[nums.index(num)+1:]
    if (target - num) in remaining_nums:
      return [nums.index(num), nums.index(num)+1+remaining_nums.index(target-num)]

print twoSum([2,7,11,15], 9)
print twoSum([3,2,4], 6)
print twoSum([3,3], 6)

# Solutions
# https://leetcode.com/articles/two-sum/

