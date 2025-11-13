# Functional Style Programming 

# Without Functions 

a = 10
b = 5

# math operations 
print(a+b)
print(a-b)
print(a*b)
print(a/b)

print("=" * 10)

a = 20
b = 10

# Repeat math operations 
print(a+b)
print(a-b)
print(a*b)
print(a/b)

print("=" * 10)

a = 300
b = 100

# Repeat math operations 
print(a+b)
print(a-b)
print(a*b)
print(a/b)

print("=" * 10)

# With Functions 
def math_ops():
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)

a = 10
b = 5
math_ops()
print("=" * 10)
a = 20
b = 10
math_ops() # calling function multiple times
print("=" * 10)
a = 300
b = 100
math_ops() # calling function multiple times