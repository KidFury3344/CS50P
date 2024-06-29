file_name = input("File Name: ").lower().strip()
dot_index = file_name.find(".")

if file_name[dot_index:] == ".gif":
    print("image/gif")
elif (file_name[dot_index:] == ".jpg") or (file_name[dot_index:] == ".jpeg"):
    print("image/jpeg")
elif file_name[dot_index:] == ".png":
    print("image/png")
elif file_name[dot_index:] == ".pdf":
    print("application/pdf")
elif file_name[dot_index:] == ".txt":
    print("text/plain")
elif file_name[dot_index:] == ".zip":
    print("application/zip")
else:
    print("application/octet-stream")