# Given an input string, reverse all the words.
def reverser(str):
    words = str.split()
    return " ".join(words[::-1])

# Time complexity is O(n).

print reverser("Hello world!") == "world! Hello"
print reverser("Hello    world!") == "world! Hello"
print reverser("My name is Patrick!") == "Patrick! is name My"
print reverser("") == ""
