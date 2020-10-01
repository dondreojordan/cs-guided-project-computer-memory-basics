"""
Given a list of integers `lst`, any integer with a frequency that is equal 
to its value is considered a **lucky integer**.

Write a function that returns the lucky integer from the array. 
If the array contains multiple lucky integers, return the largest one. 
If there are no lucky integers return -1.

**Example 1**:

Input: arr = [2,3,3,3,4]
Output: 3

**Example 2**:

Input: arr = [1,2,2,3,3,3,4,4,4,4]
Output: 4

**Example 3**:

Input: arr = [1,1,2,2,2]
Output: -1
"""
def find_lucky(array):
    # input: a list
    # iterate, count, and find max() the number occurrences or each element in array
    lucky_num = 0
    for i, element in enumerate(array):
        if array.count(element[i]):
            print() 
    # return: highest lucky number or the incrementally highest number appearing the most, 
    # else, int(-1)
    # return pass

if __name__ == '__main__':
    array = [2,3,3,3,4]
    print(find_lucky(array))
