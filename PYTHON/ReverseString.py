# def reverse_string(s):
#     return s[::-1]
# print(reverse_string("uha"))

# 2nd method
String = "uha"
String_rev = ""

for i in range(len(String)-1, -1, -1):
    String_rev += String[i]

print(String_rev)