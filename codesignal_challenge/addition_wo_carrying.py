"""
A little boy is studying arithmetic. 
He has just learned how to add two integers, written one below another, column by column. 
But he always forgets about the important part - carrying.

Given two integers, your task is to find the result which the little boy will get.

Note: The boy had learned from this site, so feel free to check it out too if you are not familiar 
with column addition.

Example

For param1 = 456 and param2 = 1734, the output should be
additionWithoutCarrying(param1, param2) = 1180.

   456
  1734
+ ____
  1180
The boy performs the following operations from right to left:

6 + 4 = 10 but he forgets about carrying the 1 and just writes down the 0 in the last column
5 + 3 = 8
4 + 7 = 11 but he forgets about the leading 1 and just writes down 1 under 4 and 7.
There is no digit in the first number corresponding to the leading digit of the second one, 
so the boy imagines that 0 is written before 456. 
Thus, he gets 0 + 1 = 1.
"""

def additionWithoutCarrying(param1, param2):
    
    len_param1 = len(str(param1))
    len_param2 = len(str(param2))
    diff = len_param2 - len_param1
    # input1, input2: int
    grotesque_answer = ''
    if len_param1 == len_param2:
        for i in range(len_param1):
            added_total = int(str(param1)[i]) + int(str(param2)[i])
            grotesque_answer += str(added_total)[-1]
    elif len_param1 < len_param2:
        # do some math starting with len_param1 first
        for i in range(len_param2 - 1):
            abc = int(str(param1)[i]) + int(str(param2)[i + diff])
            grotesque_answer += str(abc)[-1]
        return str(param2)[:diff] + grotesque_answer
    else:
        for i in range(len_param1 - 1):
            abc = int(str(param2)[i]) + int(str(param1)[i + -diff])
            grotesque_answer += str(abc)[-1]
        return str(param1)[:-diff] + grotesque_answer


    return grotesque_answer
    # else:
        # pass
        # do more math excpet starting with len_param2


    # return int(sum_)

    # print(str(param1)[0])
    # grotesque_answer = param1 + param2
    # print(param1)
    # return: bath math, call it 'grotesque_answer'
    # return sum_


if __name__ == '__main__':
    # param1 =  456
    # param2 = 1734
    param1 = 99999
    param2 = 0
    # print(additionWithoutCarrying(param1, param2))  # grotesque_answer = 1180
    print(additionWithoutCarrying(param1, param2))  # grotesque_answer = 10