def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('Start function')
        func(*args, **kwargs)
        print('End function')

    return wrapper