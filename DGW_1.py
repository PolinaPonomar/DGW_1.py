#a, b = input().split('\40')
#a = int(a)
#b = int(b)
a = 2
b = 7

def foo_2a():
    print(a>b)
foo_2a()
def foo_3a():
    global c
    if a > b:
        c = 1
    else:
        c = 0
    print(c)
foo_3a()
def foo_3b():
    global max
    if c == 1:
        max = a
    else:
        max = b
    print(max)
foo_3b()
print( max, '>', b) if max==a else print( max, '>', a)
