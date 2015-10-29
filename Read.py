import string


def getUser(line):
	separate = line.split(":", 2)
	user = separate[1].split("!", 1)[0]
	return user

def getMessage(line):
    seperate = line.split(":", 2)
    msg = seperate[2]
    return msg
    
