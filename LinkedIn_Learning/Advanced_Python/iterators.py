def main():
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    daysNo = [1, 2, 3, 4, 5, 6, 7]

    i = iter(days)
    print(next(i))

    with open('test.txt', 'r') as fp:
        # sentinel value '' is used, this is the EOF and the iter will stop there
        for line in iter(fp.readline, ''):
            print(line)

    for i, m in enumerate(days, start=1):
        print(i, m)

    for i, j in zip(days, daysNo):
        print(i, j)


if __name__ == "__main__":
    main()
