# Python Datatypes

# 00. Naming Conventions

# lower_with_under:     parameters, local variables, packages + PUBLIC modules, functions, global variables, methods
# _lower_with_under:    PRIVATE modules, functions, global variables, methods
# CapWords:             PUBLIC classes
# _CapWords:            PRIVATE classes

# 01. Variables

int_variable = 1                    # integer
float_variable = 1.0                # float / decimal
bool_variable = True                # boolean
str_variable = "Hello " + 'World'   # String: " " and ' ' both can be used.

print(type(int_variable))           # <class 'int'>
print(type(float_variable))         # <class 'float'>
print(type(bool_variable))          # <class 'bool'>
print(type(str_variable))           # <class 'str'>

# 02. Arrays

list_sequence = [1, 2, 3]           # list is an array where the content can be modified (denoted by [])
tuple_sequence = (1, 2, 3)          # tuple is an array where the content is unchanged / immutable (denoted by ())

print(type(list_sequence))          # <class 'list'>
print(type(tuple_sequence))         # <class 'tuple'>