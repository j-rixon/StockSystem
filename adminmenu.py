from hashlib import sha256

attempt = input("Enter passcode: ")
if sha256(attempt+u"xRphzROrS1pq6r3d").hexdigest() == "a8fd658832275a90dbe8a5f6eaa5bd94cefeaf0aa01f5501000b43395b8b46bc":
    print("yes")