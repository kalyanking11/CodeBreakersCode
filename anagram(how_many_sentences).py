# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 16:29:59 2020

@author: kalya
"""

def anagrams(wordset, sentences):
    d = {}
    sorted_set = ["".join(sorted(word)) for word in wordset]
    print(sorted_set)
    for i in sorted_set:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    print(d)
    res = []
    for s in sentences:
        word = s.split(' ')
        print(word)
        count = 1
        for i in word:
            if "".join(sorted(i)) in d and d["".join(sorted(i))]>1:
                count *= d["".join(sorted(i))]
        res.append(count)
    return res
            
print(anagrams(['the','bats','tabs','in','cat','act'],['cat the bats']))
print(anagrams(['star','tars','stay','tay','seed','dees','eesd','rast','date','ate'],['ate date stay','rast tay star']))
        