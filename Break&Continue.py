# in this program, I will learn how to use break/continue

magicNum = 5

for n in range(10):
    if n is magicNum:
        print(magicNum, "is the magic number")
        break  # break out of the loop
    else:
        print("else statement executed")

print("\n")

    # elif n < magicNum:
    #     print("magic number is a little bigger")
    # else:
    #     print("Magic num is a little smaller")

print("Raghu " + "Khanal")

# print ("Raghu" + 4) won't work

print("\n")

print("Raghu", 5)


#  loop num 1 - 100 and print number
#  message it' multiple of 4

for i in range(100):
    if i % 4 is 0:
        print(i, "is multiple of 4")

#  Continue has a different file