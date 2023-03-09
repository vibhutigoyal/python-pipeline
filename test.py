import os 

if os.path.exists("/home/ec2-user/file2.txt")==True:
    print("file exists here")
else:
    print("file does not exists")
