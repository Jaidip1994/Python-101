from enum import Enum, unique, auto


@unique  # To ensure all the values are unique
class Fruit(Enum):
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    KIWI = 4
    PEAR = auto()


def main():
    print(Fruit.APPLE, type(Fruit.APPLE), repr(Fruit.APPLE))

    print(Fruit.APPLE.name, Fruit.APPLE.value)

    print(Fruit.PEAR.value)

    # Enums are hashable and they can be used as keys
    myDict = {}
    myDict[Fruit.APPLE] = "Keeps Doc Away"
    print(myDict)


if __name__ == "__main__":
    main()
