def celsius_to_fahrenheit(temp):
    return (temp * 9/5) + 32


def fahrenheit_to_celsius(temp):
    return (temp - 32) * 5/9


def main():
    ctemps = [0, 12, 34, 100]
    ftemps = [32, 65, 100, 212]

    print(list(map(celsius_to_fahrenheit, ctemps)))
    print(list(map(fahrenheit_to_celsius, ftemps)))

    print(list(map(lambda x: (x * 9/5) + 32, ctemps)))
    print(list(map(lambda x: (x - 32) * 5/9, ftemps)))


if __name__ == "__main__":
    main()
