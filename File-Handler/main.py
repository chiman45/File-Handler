import os
num = int(input("Enter how many folders you want to create : "))

def createfolder(num):
    for i in range(num):
        name = input(f"Enter {i+1} Folder Name : ")
        if os.path.isdir(name):
            pass
        else:
            os.makedirs(name)
        typ = input("Which type of file you want to store in this folder : ")
        move(typ,name)

def move(typ,name):
    imageext = [".png",".jpg",".jpeg",".bmp"]
    docs = [".txt",".docx",".pptx",".ppt",".xlsx"]
    video = [".mp4",'.mov']
    if typ.lower() == "image":
        lst = os.listdir()
        for  i in lst:
            split_lst = os.path.splitext(i)
            ext = split_lst[1]
            for j in imageext:
                if ext == j:
                    os.replace(i,f"{name}/{i}")


    elif typ.lower() == "docs":
        lst = os.listdir()
        for  i in lst:
            split_lst = os.path.splitext(i)
            ext = split_lst[1]
            for j in docs:
                if ext == j:
                    os.replace(i,f"{name}/{i}")


    elif typ.lower() == "video":
        lst = os.listdir()
        for  i in lst:
            split_lst = os.path.splitext(i)
            ext = split_lst[1]
            for j in video:
                if ext == j:
                    os.replace(i,f"{name}/{i}")


    else:
        print("Extension not defined")


if __name__ == "__main__":
    createfolder(num)
