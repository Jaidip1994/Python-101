def my_function(arg1, arg2, *, suppressException=False):
    pass


def main():
    my_function(1, 2, suppressException=True)


if __name__ == "__main__":
    main()
