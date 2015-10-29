from Socket import sendMessage
import string

def joinRoom(s):
    readbuffer = ""
    loading = True
    while loading:
        readbuffer = readbuffer + s.recv(1024).decode('utf-8')
        temp = str.split(readbuffer, "\n")
        readbuffer = temp.pop()

        for line in temp:
            print(line)
            loading = loadingComplete(line);
   # sendMessage(s, "/me spits on everyone in chat")
    
            

def loadingComplete(line):
    if("End of /NAMES list" in line):
        return False
    else:
        return True
            
