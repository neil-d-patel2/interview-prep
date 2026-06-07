#Variables are dynamically types, the following is a completely fine operation.

n = 0

n = "abc"

this is because python determines types at runtime. 

Multiple assignments: (The following is completely valid)

n,m = 0, "abc"

Increment:

n += 1 (cannot do n++, unlike other languages. This is due to the python interpreter)

None is the same as null in other languages

if statements:

if n > 2:
    print(n)
elif:
    n *= 9
else:
    n += 2

However: Parentheses needed for multi-line conditions

if (n > 2 && n < 5):
    print("Success")

In python, && == and 

In python, or == ||





















