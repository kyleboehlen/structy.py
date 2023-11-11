def max_value(nums):
  max_value = nums[0]
  for i in range(1, len(nums)):
    if nums[i] > max_value:
      max_value = nums[i]
      
  return max_value