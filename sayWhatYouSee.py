# Say What You See is a way of transforming a number based on its spoken
# description. For example:
#
# 12 -> "One One, One Two" -> 1112
# 21114 -> "One Two, Three Ones, One Four" -> 123114
# 1111111111 -> "Ten Ones" -> 101
#
# Write a function that will do this given an array of integers. It should omit
# the 'middle step' and simply return an array of corresponding integers.

def  say_what_you_see(input_numbers):
    output = []

    # Consider each input number,
    for number in input_numbers:
        string = str(number)
        number_string = ""

        # Start with the first number
        last_char = string[0]
        count = 1

        # Already keeping track of first number
        for letter in string[1:]:
            if letter == last_char:
                count += 1
            else:
                # Add to building string and reset metrics
                number_string += str(count) + last_char
                count = 1
                last_char = letter

        # Don't forget to add the final number!
        letter = string [-1]
        if letter == last_char:
            number_string += str(count) + letter
        else:
            number_string += "1" + letter

        # This number is complete
        output.append(int(number_string))

    # All numbers considered
    return output

print say_what_you_see([12, 21114, 1111111111]) == [1112, 123114, 101]
