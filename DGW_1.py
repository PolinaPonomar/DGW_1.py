#a, b = input().split('\40')
#a = int(a)
#b = int(b)
a = 9
b = 2

def foo_2a(a,b):print(a>b)
#print(a>b)
foo_2a(a,b)

def foo_3a(a,b): return a > b

# def foo_3a():
#
#     if a > b:
#         c = 1
#     else:
#         c = 0
#     print(c)
#     return(c)
foo_3a(a,b)

def foo_3b(a,b): return a if foo_3a(a,b) else b

# def foo_3b():
#     if c == 1:
#         max = a
#     else:
#         max = b
#     print(max)
foo_3b(a,b)

print( a, '>', b) if foo_3a(a,b) else print( b, '>', a)

flag = False
def foo_3aNew():
    global c
    if a > b:
        c = 1
    elif a < b:
        c = 0
    else:
        flag = True
    print(c)
    print(flag)
foo_3aNew()

def foo_3bNew():
    global max
    if c == 1:
        max = a
        print(max)
    elif c == 0:
        max = b
        print(max)
    else:
        flag = True
        print('Числа равны')
        print(flag)
    foo_3bNew()