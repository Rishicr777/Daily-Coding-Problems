# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

def findPairs(list1, k):
  for i in range(0, len(list1)):
    if k - list1[i] in list1:
      return True
  
  return False


A = [1, 4, 45, 6, 10, 8]
n = 18
print(findPairs(A, n))












