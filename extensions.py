txt = input("Type the name of your document ")

#   The user enters the name of his file and the program determines the media type
if txt.endswith(".gif"):
    print("image/gif")
elif txt.endswith(".jpg"):
    print("image/jpg")
elif txt.endswith(".jpeg"):
    print("image/jpeg")
elif txt.endswith(".png"):
    print("image/png")
elif txt.endswith(".pdf"):
    print("application/pdf")
elif txt.endswith(".txt"):
    print("text/txt")
elif txt.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")

#Harvard cs50 #7
