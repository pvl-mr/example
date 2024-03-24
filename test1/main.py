import time

from functest import get_string


def start_up0(**kwargs):
    print("some functions with arguments:", kwargs)


def start_up():
    kwargs_for_target_function = {'param1': 'value1', 'param2': 'value2'}
    start_up0(**kwargs_for_target_function)
    print(get_string())
    return get_string() # "[323, 2323, 21]"
