import socket
import motor

localIP     = "10.120.0.89"
localPort   =5005
bufferSize  = 1024
msgFromServer       = "Hello UDP Client"

bytesToSend         = str.encode(msgFromServer)
# Create a datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


# Bind to address and ip

UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")
# Listen for incoming datagrams

while(True):

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    command = message.decode()
    address = bytesAddressPair[1]


    #clientMsg = "Message from Client:{}".format(message)
    #clientIP  = "Client IP Address:{}".format(address)
    #print(clientMsg)
    #print(clientIP)
    #print(message)
    if command=="w":
        print("forward")
        motor.move_forward()
    elif command =="s":
        print("backward")
        motor.move_backward()
    elif input():
        print("stop")
        motor.stop_motor()
    elif command == "a":
        motor.move_left()
        print("left")
    elif command == "d":
        motor.move_right
        print("right")
    # Sending a reply to client

    #UDPServerSocket.sendto(bytesToSend, address)

