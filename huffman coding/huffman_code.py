# def frequency_map(s:str)->dict:
#     f = dict()
#     for x in s:
#         if x not in f:
#             f[x] = 1
#         else:
#             f[x] += 1
#
#     return f


# default dict
from collections import defaultdict

def frequency_map(s:str)->dict:
    f = defaultdict(int)
    for x in s:
        f[x] += 1
    return f

print(frequency_map('Priyanshu'))



