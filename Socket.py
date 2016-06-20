import socket
from Settings import host, groupHost, port, password, nick, channel

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

def openSocketToGroup():
    PW = "PASS " + password + "\r\n"
    NICK = "NICK " + nick + "\r\n"
    JOIN = "JOIN #" + channel + "\r\n"
    w = socket.socket()
    w.connect((groupHost,port,))
    w.send(PW.encode("utf-8"))
    w.send(NICK.encode("utf-8"))
    w.send(JOIN.encode("utf-8"))
    return w


def sendMessage (s, message):
    messageTemp = "PRIVMSG #" + channel + " :" + message
    MSGTEMP = messageTemp.encode()
    MSGTEMP2 = messageTemp + "\r\n"
    s.send(MSGTEMP2.encode())
    print("Sent: " + messageTemp)
    
    
def sendWhisper (s, user, message):
    messageTemp = "PRIVMSG #" + channel + " :/w "+user+" "+ message
    MSGTEMP = messageTemp.encode()
    MSGTEMP2 = messageTemp + "\r\n"
    s.send(MSGTEMP2.encode())
    print("Whispered: " + messageTemp)

def capReq (s):
    messageTemp = "CAP REQ twitch.tv/commands"
    MSGTEMP = messageTemp.encode()
    MSGTEMP2 = messageTemp + "\r\n"
    s.send(MSGTEMP2.encode())
    print("request sent: " + messageTemp)

