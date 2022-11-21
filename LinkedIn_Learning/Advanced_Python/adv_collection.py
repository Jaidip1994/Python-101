import collections
from collections import defaultdict
from collections import Counter
from collections import OrderedDict
from collections import deque
import string


def main():
    ######################################################
    Point = collections.namedtuple("Point", "x y")
    p1 = Point(10, 20)
    p2 = Point(30, 50)
    print(p1, p2)
    print(p1.x, p1.y)

    p1 = p1._replace(x=100)
    print(p1)
    ######################################################

    fruits = ['apple', 'pear', 'orange', 'banana',
              'apple', 'grape', 'banana', 'banana']
    fruitCounter = {}
    fruitCounterDefaultDict = defaultdict(lambda: 100)

    for fruit in fruits:
        fruitCounter[fruit] = fruitCounter.get(fruit, 0) + 1
        fruitCounterDefaultDict[fruit] += 1
    print(fruitCounter)
    print(fruitCounterDefaultDict)
    ######################################################

    class1 = ["c1", "c2", "c3", "c4", "c4", "c1"]
    class2 = ["c5", "c6", "c2", "c1", "c7"]

    c1 = Counter(class1)
    c2 = Counter(class2)

    print(c1, c2)
    print(c1 + c2)  # Adding two dictionary
    print(c1-c2)  # Subtracting two dictionary

    print(c1.most_common(3))
    print(c1 & c2)  # Common between two dictionary
    ######################################################

    sportsTeam = [("T1", (18, 12)), ("T2", (24, 6)), ("T3", (15, 15)),
                  ("T4", (29, 1)), ("T5", (22, 8)), ("T6", (12, 18))]

    sportsTeam = sorted(sportsTeam, key=lambda x: x[1][0], reverse=True)
    print(sportsTeam)

    teams = OrderedDict(sportsTeam)
    print(teams)

    wl, ls = teams.popitem(last=False)
    print("Top Team", wl, ls)

    for i, team in enumerate(teams, start=1):
        print(i, team)
        if i == 4:
            break

    a = OrderedDict({"a": 1, "b": 2, "c": 3})
    b = OrderedDict({"a": 1, "c": 2, "b": 3})
    print("Equality test:", a == b, a == {"a": 1, "b": 2, "c": 3})
    ######################################################

    d = deque(string.ascii_lowercase)
    print("Item Count", len(d))

    for elem in d:
        print(elem, end=",")
    print()

    d.pop()
    d.popleft()
    print("After deleting from both end:", d)

    d.rotate(1)
    print("rotating right:", d)
    d.rotate(-1)
    print("rotating left:", d)
    
    d.append('z')
    d.appendleft('a')
    print("After appending:", d)


if __name__ == "__main__":
    main()
