#1
def push_pop(target, n):
    lst = []
    for i in range(1, n):
        if i in target:
            lst.append('push')
        else:
            lst.append('push' 'pop')
    return lst


print(push_pop([1, 2, 5], 5))

#2
class Solution(object):
    def intersection(self, arr1, arr2):
        lst = []
        for i in arr1:
            if i in arr2:
                lst.append(i)
        return list(set(lst))

#3

#4
class Solution(object):
    def sortArrayByParity(self, nums):
        odd,even = [],[]
        for num in nums:
            if num%2==0:
                even.append(num)
            else:
                odd.append(num)
        return even+odd

#5
class Solution(object):
    def sumOfUnique(self, nums):
        sum = 0
        for i in nums:
            if nums.count(i) == 1:
                sum += i
        return sum


#6
# 7
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split()[-1])
#8
def palindrom(str):
    tmp = ""
    for char in str:
        char = char.lower()
        if char.isalnum():
            tmp += char
    return tmp[::-1] == tmp


print(palindrom('A man, a plan, a canal: Panama'))

#9

#10
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        try:
            return [nums.index(target), len(nums) - nums[::-1].index(target)-1]
        except:
            return [-1, -1]
        
