# -*- coding: utf-8 -*-

#%% Exercice A 

def match_ends(words):

    result=0
    for word in words:
        if len(word)>1:
            if word[0]==word[len(word)-1]:
                result=result+1
    
    return result 

print match_ends(["aa", "tree", "catc"])

#%% Exercice B

def front_x(words):
    
    l1 = []
    l2 = []
    for wd in words:
        if wd[0]=="x":
            l1.append(wd)
        else:
            l2.append(wd)
    l1.sort()
    l2.sort()
    return l1 + l2

print front_x(["af","xvb","gh","xaze","fghj","xcv"])


#%% Exercice C

def sort_last(tuples):

    def lastelmt(item):
        return item[-1]

    tuples.sort(key = lastelmt)
    
    return tuples

print sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2), (0,9,0)])

#%% Test Exercices A / B / C

def test(got, expected):
    
    prefix = 'OK' if got == expected else ' X'
    # !r prints a Python representation of the strings (complete with quotes)
    print ' {} got: {!r} expected: {!r}'.format(prefix, got, expected)

def main():
    
    print 'match_ends'
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print
    print 'front_x'
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
        ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
        ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
        ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])
    
    print
    print 'sort_last'
    test(sort_last([(1, 3), (3, 2), (2, 1)]),
         [(2, 1), (3, 2), (1, 3)])
    test(sort_last([(2, 3), (1, 2), (3, 1)]),
         [(3, 1), (1, 2), (2, 3)])
    test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)])

main()

#%% Exercice D

def remove_adjacent(nums):
    
    if len(nums)>0:
        result=[nums[0]]
        for i in range (1,len(nums)):
            if result[len(result)-1]!=nums[i]:
                result.append(nums[i])
    else:
        result=[]
  
    return result
         
print remove_adjacent([1,1,3,2,3,3,4,5,2,2,7])
print remove_adjacent([])
 
#%% Exercice E

def linear_merge(list1, list2):
    
    result=[]
    i=0
    j=0
    while i<len(list1) or j<len(list2):
        if i==len(list1):
            result.extend(list2[j:])
            j=len(list2)
        elif j==len(list2):
            result.extend(list1[i:])
            i=len(list1)
        else:
            if list1[i]<list2[j]:
                result.append(list1[i])
                i+=1
            else:
                result.append(list2[j])
                j+=1

    return result

print linear_merge([1,3,5,7],[2,4,6]) 

#%% Test Exercices A / B / C / D / E

def main():

    print 'remove_adjacent'
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([]), [])

    print
    print 'linear_merge'
    test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
        ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
        ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
        ['aa', 'aa', 'aa', 'bb', 'bb'])

main()
