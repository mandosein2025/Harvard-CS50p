format = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip"
}

file_name = input("File name: ").strip().lower()

if "." in file_name:
    index = file_name.rindex(".") + 1
    answer = file_name[index:]
    if answer in format:
        print(format[answer])
    else:
        print("application/octet-stream")
else:
    print("application/octet-stream")
