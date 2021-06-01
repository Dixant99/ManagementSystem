import os


def management(path, file, format):
    os.chdir(path)
    i = 1
    files = os.listdir(path)
    with open(file) as f:
        filelist = list(f.read().split("\n"))
        print(filelist)
    for item in files:
        if item in filelist:
            os.rename(item, item.lower())
        else:
            os.rename(item, item.capitalize())

        if os.path.splitext(item)[1] == format:
            os.rename(item, f"{i}{format}")
            i += 1


if __name__ == "__main__":
    print("please do not put file in same directory as path")
    path = input("Enter the full path : \n")
    file = input("Enter the file which contains neglect : \n")
    format = input("Enter the extension  you want numerically :\n")
    management(path, file, format)
