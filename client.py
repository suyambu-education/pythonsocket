import socket

def main():
    con = socket.socket()
    host = 'localhost'
    port=1337

    con.connect((host,port))

    message = input("Type[@]:~")
    while message !="quit()":
        con.send(message.encode())
        data = con.recv(1024).decode()
        print("Message From Server[R]:~"+data)
        message = input("Type[@]:~")
    con.close()

if __name__ == "__main__":
    main()