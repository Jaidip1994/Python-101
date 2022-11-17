class ClassTest:
    def instance_method(self):
        print(f"Called instance method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class method of {cls}")
    
    @staticmethod
    def static_method():
        print("Inside static method")

    def __repr__(self):
        return "Repr purpose"


ClassTest().instance_method()
ClassTest.class_method()
ClassTest.static_method()