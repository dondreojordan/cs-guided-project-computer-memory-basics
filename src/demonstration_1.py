"""
Given a string, implement a function that returns the string with all lowercase
characters.

Example 1:

Input: "LambdaSchool"
Output: "lambdaschool"

Example 2:

Input: "austen"
Output: "austen"

Example 3:

Input: "LLAMA"
Output: "llama"

*Note: You must implement the function without using the built-in method on
string objects in Python. Think about how character encoding works and explore
if there is a mathematical approach that you can take.*
"""
def to_lower_case(letters):
    # Create a dictionary, k,v, k: Capital dec rep; v: lower case dec rep
    key = list(range(65, 90))  # "*" is the unpacking function for range()
    value = list(range(97, 122))  
    ascii_table = dict(zip(key, value))
    # print(ascii_table)
    lowercase = []
    for letter in letters:
    #     # Get number that represents letter in ASCII.
        if ord(letter) in ascii_table:
            letter_converted_lc = chr(ascii_table[ord(letter)])
            lowercase.append(letter_converted_lc)
        else:
            lowercase.append(letter)
    return lowercase      
    # if number is not within DEC lowercase range, find value and use key
    # print the letter representation 

# Another Way
# def to_lower_case(string):
#     st = ''
#     for char in string:
#         if ord(char) < 91:
#             st += chr(ord(char) + 32)
#         else:
#             st += char
#     return st

# Another Way
# def to_lower_case(string):
#     return "".join(chr(ord(s)+32) if 65 <= ord(s) <= 96 else s for s in string)

# Another Way
# COPY LECTURE CODE HERE

if __name__ == '__main__':
    letters = "ABCabcsDF"
    print(to_lower_case(letters))