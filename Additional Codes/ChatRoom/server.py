#!/usr/bin/python

import socket
from thread import start_new_thread as st_th


s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host,port))
s.listen(5)
message = ''
clients_no = []

def client(c,addr):
        c.send("WELCOME")
        clients_no.append(addr)
        while True:
                r_msg = c.recv(1024)
                if(r_msg == "stop" or r_msg == "exit"):
                        print "closing connection from client..."
                        break
                else:
                        print "client says : ",r_msg
                s_msg = str(raw_input("Your reply : "))
                if(s_msg == "stop" or s_msg == "exit"):
                        print "closing connection from server .."
                        c.send("BYE")
                else:
                        c.send(s_msg)
        c.close()

while True:
        c,addr = s.accept()
        print "got connection from ",addr
        st_th(client,(c,addr,))
c.close()

