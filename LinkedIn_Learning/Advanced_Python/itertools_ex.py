import itertools
import operator


def testFunction(x):
    return x < 5


def get_state(person):
    return person['state']


def main():
    seq = ["Jai", "Sash", "Ron"]

    # Infinite iterators
    # For creating infinite loop using itertools
    cycle1 = itertools.cycle(seq)
    for _ in range(5):
        print(next(cycle1))

    try:
        repeat1 = itertools.repeat(2, times=2)
        for _ in range(3):
            print(next(repeat1))
    except StopIteration:
        print("Stop Iteration got fired")

    squares = map(pow, range(10), itertools.repeat(2))
    print(list(squares))

    squares1 = itertools.starmap(pow, zip(range(10), itertools.repeat(2)))
    print(list(squares1))

    count1 = itertools.count(100, 10)
    for _ in range(5):
        print(next(count1))

    ###########################

    lst1 = [1, 2, 3, 4, 5, 9, 7, 0]
    acc1 = itertools.accumulate(lst1)
    print(list(acc1))

    print(list(itertools.accumulate(lst1[:-1], operator.mul)))

    chn1 = itertools.chain('ABCD', '1234')
    print(list(chn1))

    # ZIP considers only the collections which has the smallest length
    # But the zip_longest considers the length of the largest collections and rest all elements turns out to be None
    print(list(itertools.zip_longest(range(5), seq)))

    # Permutation and combination using itertools
    letters = ['a', 'b', 'c', 'd']
    numbers = [0, 1, 2, 3, 4, 5]
    names = ["Jay", "Sash"]

    combin = itertools.combinations(letters, 2)  # order doesn't matter
    print(list(combin))

    print(list(itertools.permutations(letters, 2)))  # order does matter

    # for the repeat with permutation
    print(list(itertools.product(numbers, repeat=2)))

    # combination with repeatation
    print(list(itertools.combinations_with_replacement(numbers, 2)))

    ############################

    result = itertools.islice(range(10), 1, 6, 2)
    print(list(result))

    with open('test.txt', 'r') as f:
        lines = itertools.islice(f, 3)

        for l in lines:
            print(l, end='')

    selectors = [True, True, False, True]
    # similar to filter function
    result = itertools.compress(letters, selectors)
    print(list(result))

    print(list(filter(testFunction, numbers)))
    print(list(itertools.filterfalse(testFunction, numbers)))

    # Take values after the condition is met
    print(list(itertools.dropwhile(testFunction, lst1)))
    # Take values until the condition is not met
    print(list(itertools.takewhile(testFunction, lst1)))

    people = [
        {
            'name': 'John Doe',
            'city': 'Gotham',
            'state': 'NY'
        },
        {
            'name': 'Jane Doe',
            'city': 'Kings Landing',
            'state': 'NY'
        },
        {
            'name': 'Corey Schafer',
            'city': 'Boulder',
            'state': 'CO'
        },
        {
            'name': 'Al Einstein',
            'city': 'Denver',
            'state': 'CO'
        },
        {
            'name': 'John Henry',
            'city': 'Hinton',
            'state': 'WV'
        },
        {
            'name': 'Randy Moss',
            'city': 'Rand',
            'state': 'WV'
        },
        {
            'name': 'Nicole K',
            'city': 'Asheville',
            'state': 'NC'
        },
        {
            'name': 'Jim Doe',
            'city': 'Charlotte',
            'state': 'NC'
        },
        {
            'name': 'Jane Taylor',
            'city': 'Faketown',
            'state': 'NC'
        }
    ]

    # Only pre-condition is groupby key should be in sorted fashion
    person_group = itertools.groupby(people, get_state)
    for key, group in person_group:
        print(key, list(group))

    # how to do copy of the iterables
    copy1, copy2 = itertools.tee(person_group)
    print(id(copy1), id(copy2))

if __name__ == "__main__":
    main()
