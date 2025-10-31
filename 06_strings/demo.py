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