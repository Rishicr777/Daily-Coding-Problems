# Find the Largest Range Among the given Array
#O(n) time/ O(n) Space

def largestRange(Array):
  bestRange = []
  longestLength = 0
  nums = {}
  
  for num in Array:
    nums[num] = True
  
  #Check for the value in hastable is false
  
  for num in Array:
    if not nums[num]:
      continue
    nums[num] = False
    currentLength = 1
    left = num - 1
    right = num + 1
    while left in nums:
      nums[left] = False
      currentLength += 1
      left -= 1
    while right in nums:
      nums[right] = False
      currentLength += 1
      right += 1
    if currentLength > longestLength:
      longestLength = currentLength
      bestRange = [left + 1, right - 1]
  return bestRange

print(largestRange([1,11,3,0,15,5,2,4,10,7,12,6]))      

