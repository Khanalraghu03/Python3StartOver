def main():
    print("Hello World")

    # Nothing happens with just those two lines of code
    # Must call the function main to get executed
    ##############################################################
    #Declare a variable and initialize it
    f = 0
    #  print("f is", f)

    #re-declaring the variable works!
    #f = "abc"
    #print("f is", f)

    #ERROR variables of different types cannot be combined
        # print("This is a string" + 123)
        # #in java this statement works
        # But in python, must use str()
    #print("This is a string " + str(123))

    # Global vs. local variables in functions
    def someFunction():
        global f
        f = "def"
        print(f)

    someFunction()
    print(f)

    #############################################################
if __name__ == "__main__":
    main()

    # if name == main then call main method
    # now the what is in the main method will get executed.
