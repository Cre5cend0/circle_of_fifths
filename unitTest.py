import types


def a_func():
    return True

print(type(a_func))

print(isinstance(a_func, types.FunctionType))

print(type(input))
