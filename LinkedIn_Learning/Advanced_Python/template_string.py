from string import Template


def main():
    str1 = "Name is {0} and age is {1}".format("Jaidip", 22)
    print(str1)

    templ = Template("Name is ${name} and age is ${age}")
    str2 = templ.substitute(name="Jaidip", age=22)
    print(str2)

    data = {
        "name": "Jaidip",
        "age": 22
    }
    str3 = templ.substitute(data)
    print(str3)


if __name__ == "__main__":
    main()
