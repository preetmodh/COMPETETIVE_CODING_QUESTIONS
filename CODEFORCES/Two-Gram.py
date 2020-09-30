# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 12:00:22 2020

@author: PREET MODH
"""
from itertools import combinations
from collections import Counter

n=int(input())
s=input()
res = [s[x:y] for x, y in combinations(range(len(s) + 1), r = 2) if len(s[x:y]) == 2]
#print(list(combinations(range(len(s)))))
a=Counter(res)
print(a.most_common(1)[0][0])