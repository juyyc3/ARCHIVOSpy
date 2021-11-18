import socket 

class TCP:
    def __init__(self, ip, puerto): # Conectar a la computadora
        connection1 = access = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        connection1.bind( (ip, puerto) ) # Especifica por donde se hace la conección y cómo lo va a hacer
        connection1.listen(0)
        print('Connection...')
        self.connection, addr = connection1.accept()
        print('Connection... Enable to ' + str(addr))
    
    def commands(self, command): # Pasar comandos
        self.connection.send(command.encode())
        return self.connection.recv(1024).decode()

    def start(self): # Input de comandos
        while True:
            command = input(">")
            result = self.commands(command)
            print(result)

run = TCP() # Conección por IP y puerto
run.start()
