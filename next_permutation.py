"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers. If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order). The replacement must be in place and use only constant extra memory.
Given an array of integers nums of size n, find the next permutation.
"""

def solve(n, nums):
    pivot = 0
    for i in range(n-1, 0, -1):
        if nums[i] > nums[i-1]:
            pivot = i
            break
    if pivot == 0:
        return sorted(nums)
    
    swap = n-1

    while nums[pivot-1] >= nums[swap]:
        swap -= 1
    
    nums[swap], nums[pivot - 1] = nums[pivot - 1], nums[swap]

    nums[pivot:] = sorted(nums[pivot:])
    return nums
