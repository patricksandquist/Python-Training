# We are given 3 strings: str1, str2, and str3. Str3 is said to be a shuffle of
# str1 and str2 if it can be formed by interleaving the characters of str1 and
# str2 in a way that maintains the left to right ordering of the characters from
# each string.

def is_shuffled(str1, str2, str3):
    if len(str1) + len(str2) != len(str3):
        return False
    if not str1 or not str2 or not str3:
        return str1 + str2 == str3

    if str1[0] != str3[0] and str2[0] != str3[0]:
        return False

    if str1[0] == str3[0] and is_shuffled(str1[1:], str2, str3[1:]):
        return True
    if str2[0] == str3[0] and is_shuffled(str1, str2[1:], str3[1:]):
        return True

    return False

# Time complexity is O(n) where n is the length of str3.

print is_shuffled("abc", "def", "dabecf") == True
print is_shuffled("abc", "def", "dbaecf") == False
print is_shuffled("abc", "def", "dabecff") == False
print is_shuffled("abc", "", "abc") == True
print is_shuffled("", "", "") == True
