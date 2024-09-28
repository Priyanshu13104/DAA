from collections import defaultdict
from collections import Counter
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

def frequency_map(s:str)->dict:
#     f = defaultdict(int)
#     for x in s:
#         f[x] += 1
#     return f

    f = Counter(s)
    return f


print(frequency_map('Priyanshu'))



