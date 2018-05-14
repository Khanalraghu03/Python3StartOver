aList = [3, 6, 7, 9, 17, 11, 19]
print("Here are the number that are still available")

for i in range(1, 20):
    if i in aList:
        continue
    print(i)

#continue skips the statement from being excecuated
#break completely breaks out of the loop