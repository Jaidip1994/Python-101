import logging

extraData = {
    'user': 'Jaidip'
}


def anotherFunction():
    logging.debug("This is a debug level message", extra=extraData)


def main():
    # user is the key of the dictionary
    fmtstr = "User:%(user)s %(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d %(message)s"
    datestr = "%m/%d/%Y %I:%M:%S %p"
    logging.basicConfig(level=logging.DEBUG,
                        filename="output.log",
                        filemode="w",
                        format=fmtstr,
                        datefmt=datestr)

    logging.debug("This is a debug message", extra=extraData)
    logging.info("This is a info message", extra=extraData)
    logging.warning("This is a warning message", extra=extraData)
    logging.error("This is a error message", extra=extraData)
    logging.critical("This is a critical message", extra=extraData)

    anotherFunction()


if __name__ == "__main__":
    main()
