# There is an array of non-negative integers.
# A second array is formed by shuffling the elements of the first array and deleting a random element.
# Given these two arrays, find which element is missing in the second array.

def missingNumber(arr1, arr2):
    if len(arr2) == 0:
        return arr1[0]
    return sum(arr1) - sum(arr2)

print missingNumber([4, 4, 2, 6, 0, 3], [6, 4, 2, 3, 4]) == 0
print missingNumber([4, 4, 2, 6, 0, 3], [6, 4, 2, 3, 0]) == 4
print missingNumber([4], []) == 4
