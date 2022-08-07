import datetime


def print_datetime(f):
    def wrapper(*args, **kwargs):
        print(f'start: {datetime.datetime.now()}')
        f(*args, **kwargs)
        print(f'end: {datetime.datetime.now()}')

    return wrapper


@print_datetime
def squared(x):
    print(x ** 3)


# print_datetime(squared)()
squared(3)
