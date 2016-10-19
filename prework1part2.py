# -*- coding: utf-8 -*-
   
#%% Exercice A
 
def donuts(count):
    
    if count<10:
        result="Number of donuts: "+str(count)
    else:
        result="Number of donuts: many"
    
    return result  
    
print donuts(4)
print donuts(10)
print donuts(44)

#%% Exercice B

def both_ends(s):

    if len(s)>1:
        result=s[:2]+s[len(s)-2:]
    else:
        result=""
        
    return result

print both_ends("aa")
print both_ends("test")
print both_ends("test2")

#%% Exercice C

def fix_start(s):
    
    if len(s)>1:
        result="".join([s[0],s[1:].replace(s[0],"*")])
    else:
        result=s
    
    return result
    
print fix_start("azerty")
print fix_start("azertyazertyu")
print fix_start("azaabb")
print fix_start("a")

#%% Exercice D

def mix_up(a, b):
      
    return " ".join([b[:2]+a[2:],a[:2]+b[2:]])
      
print mix_up("mix","pod")
print mix_up("dog","dinner")
print mix_up("az","er")

#%% Test Exercices A / B / C / D

def test(got, expected):

    prefix = 'OK' if got == expected else ' X'
    # !r prints a Python representation of the strings (complete with quotes)
    print ' {} got: {!r} expected: {!r}'.format(prefix, got, expected)

    return
    
def main():
    print 'donuts'
    # Each line calls donuts, compares its result to the expected for that call.
    test(donuts(4), 'Number of donuts: 4')
    test(donuts(9), 'Number of donuts: 9')
    test(donuts(10), 'Number of donuts: many')
    test(donuts(99), 'Number of donuts: many')

    print
    print 'both_ends'
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')

    print
    print 'fix_start'
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')

    print
    print 'mix_up'
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')
    
    return
    
main()

#%% Exercice D bis

def verbing(s):
    
    if len(s)>2:
        if s[len(s)-3:]=="ing":
            s=s+"ly"
        else:
            s=s+"ing"
    
    return s

print verbing("swiming")
print verbing("ar")
print verbing("art")
print verbing("swim")

#%% Exercice E

def not_bad(s):
    
    if -1<s.find("not") and s.find("not")<s.find("bad"):
        s=s[:s.find("not")]+"good"+s[s.find("bad")+3:]
    
    return s
    
print not_bad("This dinner is not that bad!")

#%% Exercice F

def front_back(a, b):
    
    result=a[:int((len(a)+1)/2)]+b[:int((len(b)+1)/2)]+a[int((len(a)+1)/2):]+b[int((len(b)+1)/2):]
    
    return result
    
print front_back("azerty","qsdfg")

#%% Test Exercices D bis / E / F

def main():
    print 'verbing'
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')
    
    print
    print 'not_bad'
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print
    print 'front_back'
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')

main()
