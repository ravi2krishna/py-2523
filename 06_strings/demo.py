# Strings 

# define single line strings 
s1 = "hello"
print(s1)

s2 = 'hello'
print(s2)

s3 = '''hello''' # not recommended, as it's a single line string 
print(s3)

s4 = """hello""" # not recommended, as it's a single line string 
print(s4)

# define multi line strings  
# define_python = "Python is a high-level, general-purpose programming language. 
#         Its design philosophy emphasizes code readability 
#         with the use of significant indentation."
# print(define_python)

define_python = """Python is a high-level, general-purpose programming language. 
        Its design philosophy emphasizes code readability 
        with the use of significant indentation."""
print(define_python)

define_python = '''Python is a high-level, general-purpose programming language. 
        Its design philosophy emphasizes code readability 
        with the use of significant indentation.'''
print(define_python)

# need a single quote in a string -> double quotes 
question = "how are you ?"
# answer = 'i'm fine'
answer = "i'm fine"
print(answer)

# need a double quote in a string -> single quotes 
question = "how are you ?"
# answer = "i"m fine"
answer = 'i"m fine'
print(answer)

# need both single & double quote in a string -> triple quotes 
question = "how are you ?"
answer = '''i"m fine i'm fine'''
print(answer)

# Accessing Strings 
text = "python"
print(text)

# Access characters using index 
# Positive Index
print(text[0])
print(text[1])

# Negative Index
print(text[-1])
print(text[-2])

# print(text[10]) # IndexError: string index out of range

# Access all characters 
print(text[0])
print(text[1])
print(text[2])
print(text[3])
print(text[4])
print(text[5])

# Access all characters 
text = "python"
for char in text:
    print(char)

# len() used to check the number of characters 
print("Length Of String: ",len(text))

# slicing -> string[start:end:step]
text = "python"
print(text[:])
print(text[::])
print(text[0:3:1]) # pyt
print(text[1:3]) # yt
print(text[0:5:2]) # pto

         #    0  1  2  3  4  5   [Positive Indexing]
        #     p  y  t  h  o  n
        #    -6  -5 -4 -3 -2 -1  [Negative Indexing]

print(text[-4:-1:1]) # tho
print(text[-4:-1:-1]) # empty
print(text[-4:-6:-1]) # ty

# String Concatenation 
s = "good"
m = "morning"
print(s+m)

age = 30
# print("My Age is: "+age) # TypeError: can only concatenate str (not "int") to str

# Formatted String Literals (f-strings)
print(f"My Age is: {age}")

# String Repetition 
laugh = "HaHaHa"
print(laugh)

hard_laugh = laugh * 10
print(hard_laugh)

# String Immutability 
greet = "hello" # -> Hello
print(greet)
print(greet[0])
# greet[0] = "H" # TypeError: 'str' object does not support item assignment
list_greet = ['h','e','l','l','o']
print(list_greet)
print(list_greet[0])
list_greet[0] = "H"
print(list_greet)
print(list_greet[0])

# string methods
print(dir(greet))