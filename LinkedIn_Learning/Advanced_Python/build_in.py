def main():
    list1 = [0,1,2,3,4]
    print(any(list1))
    print(any([]))
    
    print(all(list1)) # this is false as there is a 0 in the list

if __name__ == "__main__":
    main()