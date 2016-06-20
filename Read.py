import string
from Settings import channel

def getUser(line):
        if (line != ":tmi.twitch.tv USERSTATE #"+channel):
                separate = line.split(":") #, 2
                user = separate[1].split("!")[0]
                return user

def getMessage(line):
        if (line != ":tmi.twitch.tv USERSTATE #"+channel):
                seperate = line.split(":")
                msg = seperate[2]
                return msg

                
