"""
Task 3
Write a program, which has two print statements to print the following text
(capital letters "O" and "H", made from "#" symbols):
#########
#       #
#       #
#       #
#########

#       #
#       #
#########
#       #
#       #

Pay attention that usage of spaces is forbidden, as well as creating the whole result 
text string using """ """, use '\n' and '\t' symbols instead.
"""

# version in one print
print ('#########', '\n#\t\t#', '\n#\t\t#','\n#\t\t#','\n#########')
print ('\n#\t\t#', '\n#\t\t#', '\n#########', '\n#\t\t#', '\n#\t\t#')
print('\n')  #retreat

# version in any prints
print(9 *'#')
print('#\t\t#')
print('#\t\t#')
print('#\t\t#')
print(9 *'#')
print('\n')  #retreat
print('#\t\t#')
print('#\t\t#')
print(9 *'#')
print('#\t\t#')
print('#\t\t#')