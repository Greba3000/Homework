# 1) Find a way to call `inner_function` without moving it from inside of `enclosed_function`.
# a = "I am global variable!"
#
#
# def enclosing_function():
#     global inner_function
#     a = "I am variable from enclosed function!"
#
#     def inner_function():
#         global a
#         a = "I am local variable!"
#         print(a)
#
#
# enclosing_function()
# print(dir())
# inner_function()

# 2.1) Modify ONE LINE in `inner_function` to make it print variable 'a' from global scope.
# a = "I am global variable!"
#
#
# def enclosing_function():
#     global inner_function
#     a = "I am variable from enclosed function!"
#
#     def inner_function():
#         b = "I am local variable!"
#         global a
#         print(a,b)
#
#
# enclosing_function()
# inner_function()

# 2.2) Modify ONE LINE in `inner_function` to make it print variable 'a' form enclosing function.
a = "I am global variable!"


def enclosing_function():
    global inner_function
    a = "I am variable from enclosed function!"

    def inner_function():
        b = "I am local variable!"
        nonlocal a
        print(a, b)


enclosing_function()
inner_function()
