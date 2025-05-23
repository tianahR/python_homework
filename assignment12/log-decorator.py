# Task 1: Writing and Testing a Decorator

import logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))

# 1.2 Declare a decorator called logger_decorator. This should log the name of the called function (func.__name__), 
# the input parameters of that were passed, and the value the function returns, to a file ./decorator.log. 
# Functions may have positional arguments,keyword arguments, both, or neither. 
# So for each invocation of a decorated function, the log would have:
# function: <the function name>
# positional parameters: <a list of the positional parameters, or "none" if none are passed>
# keyword parameters: <a dict of the keyword parameters, or "none" if none are passed>
# return: <the return value>



def log_decorator(func):
    def wrapper(*args, **kwargs):
        logger.log(logging.INFO, f"function: {func.__name__}")
        if args:
            arg_param = args
        else:
            arg_param = "none"
        logger.log(logging.INFO, f"positional parameters: {arg_param}")
        if kwargs:
            kwarg_param = kwargs
        else:
            kwarg_param = "none"
        logger.log(logging.INFO, f"keyword parameters: {kwarg_param}")
        result = func(*args, **kwargs)
        logger.log(logging.INFO, f"return: {result}")
        return result
    return wrapper

# 1.3 Declare a function that takes no parameters and returns nothing. 
# Maybe it just prints "Hello, World!". Decorate this function with your decorator.

@log_decorator
def hello_world():
    print("Hello, World!")

# 1.4 Declare a function that takes a variable number of positional arguments and returns True. 
# Decorate this function with your decorator.
@log_decorator
def positional_args(*args):
    return True

# 1.5 Declare a function that takes no positional arguments and a variable number of keyword arguments,
# and that returns logger_decorator. Decorate this function with your decorator.
@log_decorator
def keyword_args(**kwargs):
    return log_decorator

# 1.6 Within the mainline code, call each of these three functions, passing parameters for the functions that take positional 
# or keyword arguments. 
# Run the program, and verify that the log file contains the information you want.
hello_world()

positional_args("fara", "tiana")
        
keyword_args(first="fara", second="tiana")