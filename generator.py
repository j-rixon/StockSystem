import random, string, barcode  # import the necessary modules


def newID():  # function to make 11 character random alphanumeric IDs
    x = ''.join(random.choice(string.ascii_letters.upper() + string.digits) for _ in range(11))
    # generate a random uppercase letter or number and append it to a string 11 times
    return x  # return string


ID = input("Enter barcode to generate, or leave blank for random:")
if ID == '':
    ID = newID()  # generate 20 IDs
elif len(ID) != 11:
    print("Invalid ID")  # FIX ME
bc = barcode.Code39(ID.upper())  # create a code39 barcode with a checksum for the ID
name = bc.save('barcode')  # save it under the name "barcode<number>.svg"