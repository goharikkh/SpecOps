 #1
class Solution(object):
    def removeDuplicates(self, nums):
        i = 1
        for j in range(1, len(nums)):
            if nums[j] != nums[j - 1]:
                nums[i] = nums[j]
                i += 1
        return i

 #2
def merge_sort(nums1, nums2, m, n):
    for x in range(m, m + n):
        nums1[x] = nums2[x - m]
    return nums1.sort()


#3
class Solution(object):
    def containsDuplicate(self, nums):
        nums = sorted(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False


#4



#5
def missing_number(nums):
    n = len(nums)
    return abs((n * (n + 1) // 2) - sum(nums))

print(missing_number([1, 5, 4, 3, 0]))


#6
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        new_arr = []
        string = ''
        for x in nums:
            if x == 1:
                string += "1"
            if x == 0:
                new_arr.append(len(string))
                string = ''
        new_arr.append(len(string))
        return max(new_arr)



#7
def arrayPairSum(nums):
    nums.sort()
    return sum([nums[x] for x in range(0, len(nums), 2)])

#8
def primeFactors(n):
    c = 2
    rec = 0
    while n > 1:
        if n % c == 0:
            n /= c
            rec = c
        else:
            c = c + 1
    return rec


n = 600851475143
print(primeFactors(n))


#9
