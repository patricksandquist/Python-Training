# Generate all permutations of a given string.
def permutations(str):
    if len(str) < 2:
        return [str]

    output = []
    lower_perms = permutations(str[1:])
    letter = str[0]

    for perm in lower_perms:
        for i in range(len(perm) + 1):
            output.append(perm[:i] + letter + perm[i:])

    return output

print permutations("ABC").sort() == ["ABC", "BAC", "BCA", "ACB", "CAB", "CBA"].sort() # order doesn't matter
print permutations("AB").sort() == ["AB", "BA"].sort() # order doesn't matter
print permutations("dogs").sort() == [
  "dogs", "sgod", "gsod", "ogsd",
  "dosg", "sgdo", "gsdo", "ogds",
  "dsgo", "sdgo", "gdso", "osdg",
  "dsog", "sdog", "gdos", "osgd",
  "dgso", "sodg", "gods", "odgs",
  "dgos", "sogd", "gosd", "odsg"
].sort() # order doesn't matter
