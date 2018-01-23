import random, string, barcode  # import the necessary modules


def newIDs(num):  # function to make 11 character random alphanumeric IDs
    list1 = []  # initialise the list as empty
    for var in range(num):  # for each ID requested
        x = ''.join(random.choice(string.ascii_letters.upper() + string.digits) for _ in range(11))
        # generate a random uppercase letter or number and append it to a string 11 times
        list1.append(x)  # append that string to a list
    return list1  # return said list


list2 = newIDs(20)  # generate 20 IDs
for item in list2:  # for each item in the list produced
    bc = barcode.Code39(str(item))  # create a code39 barcode with a checksum for the ID
    name = bc.save('barcode{0}'.format(list2.index(item)))  # save it under the name "barcode<number>.svg"
