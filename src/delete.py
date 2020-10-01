# lucky = []  
lucky = [1]
# lucky = [1,1,2,2, 2]


def find_lucky(lst):
    return max([ num if num == lst.count(num) else -1 for num in lst])    
print(find_lucky(lucky))


# def find_lucky(lst):
#     max_num = []
#     if len(lst) > 1:
#         for num in lst:
#             if num == lst.count(num):
#                 # print(num, lst.count(num))
#                 max_num.append(num)
#             else:
#                 print(num, lst.count(num))
#                 max_num.append(-1)     
#     else:
#         print("error")
#     return max(max_num)

# print(find_lucky(lucky))