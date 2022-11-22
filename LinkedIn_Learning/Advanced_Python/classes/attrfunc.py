class MyColor():
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100

    def __getattr__(self, name):
        if name == "rgbcolor":
            return (self.red, self.green, self.blue)
        elif name == "hexcolor":
            return "#{0:02x}{1:02x}{2:02x}".format(
                self.red, self.green, self.blue
            )
        else:
            raise AttributeError

    def __setattr__(self, name, value):
        if name == "rgbcolor":
            self.red, self.green, self.blue = value
        else:
            super().__setattr__(name, value)

    # use dir to list the available properties
    def __dir__(self):
        return ("red", "green", "blue", "rgbcolor", "hexcolor")


def main():
    cls1 = MyColor()

    print(cls1.rgbcolor)
    print(cls1.hexcolor)

    cls1.rgbcolor = (10, 20, 30)
    print(cls1.rgbcolor)
    
    print(dir(cls1))


if __name__ == "__main__":
    main()
