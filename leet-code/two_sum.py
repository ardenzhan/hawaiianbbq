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
  hash_map = {}
  for i in range(len(nums)):
    complement = target - nums[i]

    if complement in hash_map:
      return (hash_map[complement], i)
    
    hash_map[nums[i]] = i

# Solutions
# https://leetcode.com/articles/two-sum/

