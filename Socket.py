import socket
from Settings import host, port, password, nick, channel
def openSocket():
    PW = "PASS " + password + "\r\n"
    NICK = "NICK " + nick + "\r\n"
    JOIN = "JOIN #" + channel + "\r\n"
    
    s = socket.socket()
    s.connect((host, port,))
    s.send(PW.encode("utf-8"))
    s.send(NICK.encode("utf-8"))
    s.send(JOIN.encode("utf-8"))
    return s

def sendMessage (s, message):
    messageTemp = "PRIVMSG #" + channel + " :" + message
    MSGTEMP = messageTemp.encode()
    MSGTEMP2 = messageTemp + "\r\n"
    s.send(MSGTEMP2.encode())
    print("Sent: " + messageTemp)
    
    
