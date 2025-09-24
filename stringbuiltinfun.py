# s="chinku,{}!"
# print(s.format("babu"))

def notify(user, missedcalls):
    data = {"user":user,"calls": missedcalls}
    template = "{user} has {calls} missedcalls."
    return template.format_map(data)
print(notify("chinku",7))


# def isalnum_internal(s):
#     if len(s) == 0:
#         return False
#     for c in s:
#         if not (('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9')):
#             return False
#     return True

# s="chinku,{}!"
# print(s.format("babu"))

# print(12345.isalpha())

# write user defined function code for 1.swapcase( ) 2.strip( ) , lstrip( ) , rstrip( ) 3.count( ) 4.Replace( )

#1.swapcase( )
def user_swapcase(s):
    result = ""
    for char in s:
        if char.islower():
            result += char.upper()
        elif char.isupper():
            result += char.lower()
        else:
            result += char
    return result

print(user_swapcase("dallie 123!"))

#2. strip(),lstrip(), rstrip()
def user_strip(s):
    return user_lstrip(user_rstrip(s))

def user_lstrip(s):
    i = 0
    while i < len(s) and s[i].isspace():
        i += 1
    return s[i:]

def user_rstrip(s):
    i = len(s) - 1
    while i >= 0 and s[i].isspace():
        i -= 1
    return s[:i+1]

# Example:
print(user_strip("   hello world   "))   # 'hello world'
print(user_lstrip("   hello world   "))  # 'hello world   '
print(user_rstrip("   hello world   "))  # '   hello world'

#3. User-Defined count()
def user_count(s, sub):
    count = 0
    for i in range(len(s)-len(sub)+1):
        if s[i:i+len(sub)] == sub:
            count += 1
    return count

print(user_count("konkanan", "n"))

#4. replace()
def user_replace(s, old, new):
    result = ""
    i = 0
    while i < len(s):
        if s[i:i+len(old)] == old:
            result += new
            i += len(old)
        else:
            result += s[i]
            i += 1
    return result

print(user_replace("hello world", "l", "M"))  

