class Person():
    def __init__(self):
        self.fname = "Jai"
        self.lname = "Gho"
        self.age = 29
    
    def __repr__(self):
        return f"<Person class - fname: {self.fname}, lname: {self.lname}, age: {self.age}>"
    
    def __str__(self):
        return f"Person {self.fname} {self.lname} is {self.age} yrs old"
    
    def __bytes__(self):
        val = f"Person:{self.fname}:{self.lname}:{self.age}"
        return bytes(val.encode("utf-8"))


def main():
    cls1 = Person()

    print(str(cls1))
    print(repr(cls1))
    print("Formatted: {0}".format(cls1))
    print(bytes(cls1))


if __name__ == "__main__":
    main()
