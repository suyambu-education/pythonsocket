from socket import *

def main():
    print ("Server Start v0.1 ! \n ")

    con = socket()

    host ='localhost'
    port=1337

    con.bind((host,port))

    con.listen(10)

    client , address =  con.accept()

    while True:
        print("Cliet Address :~"+str(address))
        data = client.recv(1024).decode()
        if not data:
            break
        print("Message - [R]:#"+data)
        message = input("Type[@]:#")
        client.send(message.encode())
    client.close()
if __name__ == "__main__":
    main()