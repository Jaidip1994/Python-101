import collections
from collections import defaultdict


def main():
    Point = collections.namedtuple("Point", "x y")
    p1 = Point(10, 20)
    p2 = Point(30, 50)
    print(p1, p2)
    print(p1.x, p1.y)

    p1 = p1._replace(x=100)
    print(p1)

    fruits = ['apple', 'pear', 'orange', 'banana',
              'apple', 'grape', 'banana', 'banana']
    fruitCounter = {}
    fruitCounterDefaultDict = defaultdict(lambda: 100)

    for fruit in fruits:
        fruitCounter[fruit] = fruitCounter.get(fruit, 0) + 1
        fruitCounterDefaultDict[fruit] += 1
    print(fruitCounter)
    print(fruitCounterDefaultDict)


if __name__ == "__main__":
    main()
