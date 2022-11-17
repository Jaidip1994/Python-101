# string contains unicode, bytes contains raw 8-bit values

def main():
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(b)

    s = "This is a string"
    print(s)

    # Combining a byte and a string
    # Bytes needs to be decoded first prior to joining with string
    s2 = b.decode('utf-8')
    print(s+s2)

    # String needs to be encoded prior to joining with bytes
    b2 = s.encode('utf-8')
    print(b+b2)


if __name__ == "__main__":
    main()
