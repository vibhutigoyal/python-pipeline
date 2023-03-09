def cp():
    try:
        with open("/home/ec2-user/f1.txt", "w") as f1:
            f1.write("hello this is my jenkins pipeline")
        with open("/home/ec2-user/f1.txt", "r") as f1:
            data = f1.read()
        with open("/home/ec2-user/file2.txt", "x") as f2:
            f2.write(data)
            print("File data has been copied successfully!")
    except FileExistsError:
        with open("/home/ec2-user/file2.txt", "a") as f2:
            f2.write(data)
            print("File data has been appended successfully!")
    except PermissionError:
        print("Permission denied. Unable to write to file.")
