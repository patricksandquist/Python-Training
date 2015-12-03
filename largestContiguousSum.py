# Given an array of integers (positive and negative) find the largest continuous sum.
def lcs(arr):
    if len(arr) == 0:
        return 0

    maxSum = currentSum = 0

    for num in arr:
        currentSum += num
        if currentSum > maxSum:
            maxSum = currentSum
        if currentSum < 0:
            currentSum = 0
    return maxSum

print lcs([5, 3, -7, 6]) == 8
print lcs([5, 3, -7, 6, 4]) == 11
print lcs([5]) == 5
print lcs([]) == 0

# Time complexity is O(n) and space complexity is O(1)
