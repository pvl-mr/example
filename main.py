import time

def start_up0(**kwargs):
    print("some functions with arguments:", kwargs)


def start_up():
    kwargs_for_target_function = {'param1': 'value1', 'param2': 'value2'}
    start_up0(**kwargs_for_target_function)
    # time.sleep(100)
    return [323, 2323, 21] # "[323, 2323, 21]"
