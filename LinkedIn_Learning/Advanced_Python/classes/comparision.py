class Employee():
    def __init__(self, fname, lname, level, yrsService):
        self.fname = fname
        self.lname = lname
        self.level = level
        self.seniority = yrsService

    def __ge__(self, other):
        if self.level == other.level:
            return self.seniority >= other.seniority
        return self.level >= other.level

    def __gt__(self, other):
        if self.level == other.level:
            return self.seniority > other.seniority
        return self.level > other.level

    def __lt__(self, other):
        if self.level == other.level:
            return self.seniority < other.seniority
        return self.level < other.level

    def __le__(self, other):
        if self.level == other.level:
            return self.seniority <= other.seniority
        return self.level <= other.level

    def __eq__(self, other):
        return self.level == other.level


def main():
    dept = []
    dept.append(Employee("Jai", "Gho", 5, 9))
    dept.append(Employee("John", "Sin", 20, 15))
    dept.append(Employee("Sas", "bha", 2, 5))
    
    print(dept[0] < dept[1])
    
    # Object comparison class functions enable objects to be sortable
    emps = sorted(dept)
    for emp in emps:
        print(emp.fname)


if __name__ == "__main__":
    main()
