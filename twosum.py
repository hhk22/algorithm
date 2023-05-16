

# 1. hashmap을 이용한 구조. O(2n) = O(n) --> O(n) 도 가능한구조. 

nums = [2, 3, 5, 7]
target = 7


# O(2n)
def twosum_n(nums, target):
    hashmap = {}
    for idx, num in enumerate(nums):
        hashmap[num] = idx

    for idx, num in enumerate(nums):
        target_num = target - num
        if target_num in hashmap and hashmap[target_num] > idx:
            return [idx, hashmap[target_num]]


# O(n)
def twosum_2n(nums, target):
    hashmap = {}
    for idx, num in enumerate(nums):
        if num in hashmap:
            return [hashmap[num], idx]
        else:
            hashmap[target - num] = idx


twosum_2n(nums, target) == [0, 2]






