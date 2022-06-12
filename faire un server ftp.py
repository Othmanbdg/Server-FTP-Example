from pyftpdlib import servers
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.authorizers import DummyAuthorizer

port=2121
address = ("127.0.0.1",port) # Changer l'ip pour que le serveur soit accessible sur le réseau local
user="admin"
passw="password"
folder=""  #Path du répertoire pour l'utilisateur


#On crée un "manager" virtuel qui va permettre de gérer les utilisateurs
auth= DummyAuthorizer()

#On crée notre utilisateur, avec son répertoire et ses permissions
auth.add_user(user,passw,folder,perm="elradfmw")

#On crée maintenant handler pour le serveur
handler= FTPHandler
#On dit au handler que celui qui va gérer les users c'est auth
handler.authorizer = auth

handler.banner = "Vous êtes connecté"  #Message d'acceuil quand on se connecte


server = servers.ThreadedFTPServer(address,handler) #server

server.max_cons = 256 # Maximum de connexion
server.max_cons_per_ip = 5 # Maximum de connexion par ip

server.serve_forever() #On lance le server

