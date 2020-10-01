"""
In order to solve this challenge you will need to [review the rules of Roman
Numerals](https://www.mathsisfun.com/roman-numerals.html).

Given a Roman Numeral (as a string), convert it to an integer. Your input is
guaranteed to be a Roman Numeral value from 1 to 3999.

Example 1:

Input: "IV"
Output: 4

Example 2:

Input: "XII"
Output: 12

Example 3:

Input: "MCMLXXXIV"
Output: 1984
"""
def roman_to_integer(roman):
    # input: roman numerals in range 1-3999 as a str.
    # create a POR (point of reference: key, roman numeral, value, numeric eqivalent)
    value = { 
        'M': 1000, 
        'D': 500, 
        'C': 100, 
        'L': 50, 
        'X': 10, 
        'V': 5, 
        'I': 1
    } 

    # Initialize previous character and answer
    p = 0
    ans = 0
    # Traverse through all characters 
    n = len(roman)  
    for i in range(n-1, -1, -1): 
        # If greater than or equal to previous, 
        # add to answer  
        if value[roman[i]] >= p: 
            ans += value[roman[i]] 
        # If smaller than previous   
        else: 
            ans -= value[roman[i]] 
        # Update previous 
        p = value[roman[i]] 
   
    # Iterate roman numerals and grab the value pair 
    # return: int, the converted alpha-numeric value
    return ans

# Another Way
# roman_numerals = {'I': 1, 'V': 5, 'X': 10,
#                       'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     result = 0
#     for i, c in enumerate(roman):
#         if (i+1) == len(roman) or roman_numerals[c] >= roman_numerals[roman[i+1]]:
#             result += roman_numerals[c]
#         else:
#             result -= roman_numerals[c]
#     return result

# def roman_to_integer(roman):
#     total = 0
#     for i in range(len(roman)):
#         if i + 1 < len(roman) and mapping[roman[i]] < mapping[roman[i + 1]]:
#             diff = mapping[roman[i + 1] - mapping[roman[i]]
#             total += diff
#             i += 2
#         else:
#             total += mapping[roman[i]]
#             i += 1
#     return total


if __name__=='__main__':
    # roman = "MCMLXXXIV"  #1984
    # roman = "XII"  # 12
    roman = "MMMCMXCIX"  # 3999
    print(roman_to_integer(roman))