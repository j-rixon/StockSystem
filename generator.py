import random, string, barcode, os  # import the necessary modules


def newID():  # function to make 11 character random alphanumeric IDs
    x = ''.join(random.choice(string.ascii_letters.upper() + string.digits) for _ in range(11))
    # generate a random uppercase letter or number and append it to a string 11 times
    return x  # return string


ID = ""
while len(ID) != 11 or ID.isalnum() is False:
    ID = input("Enter barcode to generate, or leave blank for random:")
    if ID == '':
        ID = newID()  # generate ID
        break
    elif len(ID) != 11 or ID.isalnum() is False:
        print("Invalid ID")
bc = barcode.Code39(ID.upper())  # create a code39 barcode with a checksum for the ID
name = bc.save('barcode')  # save it under the name "barcode.svg", overwrite existing file with this name
os.startfile("barcode.svg")  # open the file
