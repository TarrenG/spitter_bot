import string, random, time, datetime, webbrowser, requests, json, sys, os

from json import loads
from urllib.request import urlopen
from Read import getUser, getMessage
from Socket import openSocket, sendMessage
from Init import joinRoom
from Settings import channel



s = openSocket()
joinRoom(s)
readbuffer = ""
last = time.time()

#TRIVIA STUFF
trivia = open("trivia.txt", "r")
trivia_str = trivia.read()
trivia_list = trivia_str.split("\n")
question_list = []
answer_list = []
counter = 0
trivia_dict= {}
used_dict = {}
active = False
for index in trivia_list:
        #print(index)
        trivia_dict[counter] = index.split("?")[0] +"|"+ index.split("?")[1]
        #if counter%2 == 0:
          #      trivia_dict[counter] = index
        #else:
         #       trivia_dict[counter - 1] += index
        counter = counter + 1
#print(trivia_dict)

#TWITCH API CHATTERS
response = urlopen("https://tmi.twitch.tv/group/user/"+channel+"/chatters")
readable = response.read().decode("utf-8")
chatlist = loads(readable)
chatters = chatlist['chatters']
chatterlist = chatters.values()


#print(chatlist.values())

#UPDATING VARS
leave = False
donatetimer = time.time()
findtimer = time.time()
spittimer = time.time()
triviatimer = time.time()
jahtimer = time.time()
confirmtimer = time.time()
goldDict = {}
golddueltimer = time.time()
ninjatimer = time.time()
howehtimer = time.time()
gimmetimer = time.time()
bottimer = time.time()
gradytimer = time.time()
yababytimer = time.time()
winratetimer = time.time()
dueltimer = time.time()
cringeTimer = time.time()
updatetime = time.time()
#print("chatterlist " +str(chatterlist))
counterTimer = time.time()
counter  = 0
cringes = []
#YOUTUBE API CRINGE PLAYLIST
cringe1 = urlopen("https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails%2C+id&playlistId=LLjqZhH6L-O9zC774cNLoeXA&maxResults=50&pageToken=CDIQAQ&key=AIzaSyAZhQ9hTXD26ZAVG61Byfi3fg9usU2-T4Q")
for word in cringe1.readlines():
        cringes.append(word.strip().decode("utf-8"))
cringe2 = urlopen("https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails%2C+id&playlistId=LLjqZhH6L-O9zC774cNLoeXA&maxResults=50&pageToken=CDIQAA&key=AIzaSyAZhQ9hTXD26ZAVG61Byfi3fg9usU2-T4Q")
for word in cringe2.readlines():
        cringes.append(word.strip().decode("utf-8"))
cringe3 = urlopen("https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails%2C+id&playlistId=LLjqZhH6L-O9zC774cNLoeXA&maxResults=50&pageToken=CGQQAA&key=AIzaSyAZhQ9hTXD26ZAVG61Byfi3fg9usU2-T4Q")
for word in cringe3.readlines():
        cringes.append(word.strip().decode("utf-8"))
cringeable = cringe1.read().decode("utf-8") + cringe2.read().decode("utf-8") + cringe3.read().decode("utf-8")

videoIds = []
for line in cringes: #VIDEOIDS IS A LIST
        i = 0
        if 'videoId' in line:
                videoIds.append(line[12:-1])
                i += 1
                
print("donezo")




def search(values, searchFor):
        print("entering")
        for k in values:
                print("k is "+k)
                for v in values[k]:
                        #print("v is "+v)
                        if searchFor.strip() == v.strip():      
                                return True
        return False


def ping():
        global s
        s.send("PONG :pingis\n")

        
def yaBaby(msg):
        if "1738" in msg:
                global yababytimer
                if time.time() > yababytimer:
                        yababytimer = time.time() + 30
                        sendMessage(s, "YAAA BABYYYY")

def trivia(msg,trivia_dict,active,used_dict):
        if "!trivia" in msg:
                global triviatimer
                if time.time() > triviatimer:
                        triviatimer = time.time() + 8
                        if "q" not in trivia_dict.keys():
                                qNum = random.randint(0,int(len(trivia_dict)) -1)
                                if qNum in used_dict.keys():
                                        qNum = random.randint(0,int(len(trivia_dict)) -1)
                                        while qNum in used_dict.keys():
                                                qNum = random.randint(0,int(len(trivia_dict)) -1)

                                
                                used_dict[qNum] = qNum
                                print(str(qNum))
                                question_info = trivia_dict.get(qNum)
                                print(question_info)
                                question = question_info.split("|")[0]+ "????????????"
                                print("question: "+question)
                                answer = question_info.split("|")[1]
                                sendMessage(s, question+"?")
                                trivia_dict["a"] = answer
                                trivia_dict["q"] = question
                                del trivia_dict[qNum]
                                print(str(len(trivia_dict)))
                        else:
                                sendMessage(s, "answer the current question first: "+trivia_dict["q"])
                                
def answer(user, msg, trivia_dict):
        try:
                print("looking for : "+trivia_dict["a"])
                if trivia_dict["a"].lower() in msg.lower():
                        sendMessage(s, user+" got the correct answer: "+trivia_dict["a"])
                        del trivia_dict["a"]
                        del trivia_dict["q"]
        except:
                pass
def duel(user, channel, msg):
        if "!duel " in msg:
                global dueltimer
                if time.time() > dueltimer:
                        hunnidk = open("hunnidk.txt","a")
                        records = open("record.txt", "a")
                        target =  msg.split(" ")[1]
                        dueltimer = time.time() + 4
                        roll = random.randint(1,100000)
                        if user.lower() == target.lower():
                                sendMessage(s, "you can't duel yourself ideot KKona")
                                return
                        elif search(chatters, target.lower()) == False:
                                sendMessage(s,"I can't find that user WutFace")
                                return
                        elif roll > 50000:
                                sendMessage(s,"/me spits on "+target+"! ("+str(roll)+")")
                                records.write(user+" win"+" \r\n")
                                records.write(target+ " lose"+" \r\n")
                                records.close()
                                if roll == 100000:
                                        hunnidk.write(user +" 100k \r\n")
                                        hunnidk.close()
                                return
                        elif roll <50001:
                                sendMessage(s,"/me spits on "+user+"! ("+str(roll)+")")
                                records.write(target+" win"+" \r\n")
                                records.write(user+ " lose"+" \r\n")
                                records.close()
                                if roll == 1:
                                        hunnidk.write(user +" 1 \r\n")
                                        hunnidk.close()
                                return

def spit(user,msg):
        if "!spit " in msg:
                global spittimer
                if time.time() > spittimer:
                        target = msg.split(" ")[1]
                        spittimer = time.time() + 4
                        if search(chatters, target.lower()) ==  False:
                                sendMessage(s, "I can't find that user WutFace")
                        elif target.lower() == "yoloswagbruh":
                                sendMessage(s, "never spit on yolo DansGame")
                                return
                        elif target.lower() == "pokegaard":
                                sendMessage(s, "/me splts on pokegaard PuppeyFace")
                                return
                        elif target.lower() == "wrexomania":
                                sendMessage(s, "/me spits on the ghost of Wrexomania AngelThump")
                                return
                        elif target.lower() == "tehonlyninja":
                                sendMessage(s, "/me spits on TehOnlyNinja bUrself")
                                return
                        else:
                                sendMessage(s, "/me spits on "+target)

def goldduel(user, msg):
        if "!duelgold " in msg:
                wager = msg.split(" ")[2]
                if wager:
                        global golddueltimer
                        if time.time() > golddueltimer:
                                records = open("record.txt", "a")
                                target =  msg.split(" ")[1]
                                golddueltimer = time.time() + 4
                                if search(chatters, target.lower()) == False:
                                        sendMessage(s, "I can't find that person WutFace")
                                        return
                                if int(wager) / 1:
                                        if int(wager) < 0:
                                                return
                                        hashq = random.getrandbits(128)
                                        hashstr = str(hashq)[0:4]
                                        sendMessage(s, target+", you have been challenged to a gold duel by "+user+" for "+wager+" gold, type !confirm "+hashstr+" to accept")
                                        goldDict[hashstr] = user+" "+target+" "+wager
                                        print(str(goldDict))


def confirm(msg, goldDict, user):
        if "!confirm " in msg:
                duelID = msg.split(" ")[1]
                global confirmtimer
                if time.time() > confirmtimer:
                        confirmtimer = time.time() + 4
                        infostring = goldDict.get(duelID)
                        challenger = infostring.split(" ")[0]
                        challengee = infostring.split(" ")[1]
                        wager = infostring.split(" ")[2]
                        roll = random.randint(1,100)
                        print(str(challenger)+" is the challenger "+str(challengee)+" is the target "+str(wager)+" is the wager")
                        if user.lower() == challengee.lower():
                                #print("made it here")
                                if search(chatters, challenger.lower()) == False:
                                        sendMessage(s,"both users need to be in chat for gold duels")
                                        return
                                elif roll > 50:
                                        time.sleep(.5)
                                        sendMessage(s,str(challenger)+" rolls a "+str(roll)+", "+str(challengee)+" owes "+str(challenger)+" "+str(wager)+" gold!")
                                        del goldDict[duelID]
                                        return
                                elif roll <51:
                                        time.sleep(.5)
                                        sendMessage(s,str(challenger)+" rolls a "+str(roll)+", "+str(challenger)+" owes "+str(challengee)+" "+str(wager)+" gold!")
                                        del goldDict[duelID]
                                        return
                        

def winrate(user,msg):
        if "!winrate" == msg:
                global winratetimer
                wins = 0
                total = 0
                if time.time() > winratetimer:
                        winratetimer = time.time() + 4
                        records = open("record.txt","r")
                        for line in records:
                                if user.lower() in line.lower():
                                        if "win" in line:
                                                wins += 1
                                                total += 1
                                        else:
                                                total += 1
                        if total > 0:
                                winrate = (wins / total)*100
                                sendMessage(s, user+" wins: "+str(wins)+", total: "+str(total)+", winrate: "+str("%.2f" % winrate)+"%")
                        else:
                                sendMessage(s, "you need to play more matches, "+user)
                        return
def winrate2(user,msg):
        if "!winrate " in msg:
                global winratetimer
                target = msg.split(" ")[1]
                wins = 0
                total = 0
                if search(chatters, target.lower()) == True:
                        if time.time() > winratetimer:
                                winratetimer = time.time() + 4
                                records = open("record.txt","r")
                                for line in records:
                                        if target.lower() in line.lower():
                                                if "win" in line:
                                                        wins += 1
                                                        total += 1
                                                else:
                                                        total += 1
                                if total > 0:
                                        winrate = (wins / total)*100
                                        sendMessage(s, target+" wins: "+str(wins)+", total: "+str(total)+", winrate: "+str("%.2f" % winrate)+"%")
                                else:
                                        sendMessage(s, "unable to find records for "+target)
                                return
                else:
                        sendMessage(s, "make sure your target is currently in chat")
                        return

def grady(msg):
        if "tU1uDPN" in msg:
                global gradytimer
                if time.time() > gradytimer:
                        gradytimer = time.time() + 30
                        sendMessage(s, "whose hand is that? KKona")
        

def cringe(msg, cringetimer):
        if "!cringe" in msg:
                if (time.time() > cringeTimer):
                        global cringeTimer
                        cringeTimer = time.time() + 30
                        num = random.randint(0,int(len(videoIds) - 1))
                        print(str(len(videoIds)))
                        sendMessage(s, "cringe video #"+str(num)+" : https://www.youtube.com/watch?v="+videoIds[int(num)])    
                        return
                elif "!cringe" in msg:
                        sendMessage(s,"cringe has a 30sec cd")
                        return

def bots(msg):
        if "No bots" in msg:
                global bottimer
                if time.time() > bottimer:
                        gradytimer = time.time() + 30
                        sendMessage(s, "No bots here 4Hand")
                        
def give(msg,user, trivia_dict):
        if "!skip" in msg:
                if user.lower() == "ryssh" or user.lower() == "grady_wilson" or user.lower() == "arendiko" :
                        global gimmetimer
                        if time.time() > gimmetimer:
                                gimmetimer = time.time() + 3
                                sendMessage(s, trivia_dict["a"])
def color(msg,user):
        if "!color" in msg:
                if user.lower() == "yoloswagbruh" :
                        global gimmetimer
                        if time.time() > gimmetimer:
                                color = msg.split(" ")[1]
                                gimmetimer = time.time() + 3
                                sendMessage(s, "/color "+color)


def howeh(msg):
        if "!howeh" in msg:
                global howehtimer
                if time.time() > howehtimer:
                        howehtimer = time.time() + 30
                        sendMessage(s, "Howeh IRL: https://www.youtube.com/watch?v=P-hk6gnoxqY&feature=youtu.be&t=2m25s KKona")

def ninja(msg):
        if "!ninja" in msg:
                global ninjatimer
                if time.time() > ninjatimer:
                        howehtimer = time.time() + 30
                        sendMessage(s, "Ninja!? https://www.youtube.com/watch?v=NXUTLNPNnG4 bUrself")

def copygrady(msg,user):
        if user.lower() == ".":
                sendMessage(s,msg+" Kappa")

def jah(msg):
        if "!jah" in msg:
                global jahtimer
                if time.time() > jahtimer:
                        jahtimer = time.time() + 5
                        sendMessage(s,"BrokeBack https://imgur.com/a/SNLzs")
def leaveChan(msg):
        global leave
        if "!leave #"+channel in msg:
                if not leave:
                        sendMessage(s, "ok bye KKona 4Hand")
                        leave = True
        elif "!join" in msg:
                if leave and user.lower() == "yoloswagbruh" or user.lower() == "usuallyhigh" or user.lower() == "tehonlyninja" or user.lower() == "grady_wilson":
                        sendMessage(s, "back again tell a friend KKona")
                        leave = False 
                
def heypoke(msg,user):
        if "!poke" in msg:
                global jahtimer
                if time.time() > jahtimer:
                        jahtimer = time.time() + 160
                        sendMessage(s, "you weird homie https://www.youtube.com/watch?v=Jug2HZ3dkoc&feature=youtu.be&t=4m4s")
                        
def donate(msg):
        if "!donate" in msg:
                global donatetimer
                if time.time() > donatetimer:
                        donatetimer = time.time() + 4
                        sendMessage(s,"donate for hacks at https://streamtip.com/t/yoloswagbruh thx MingLee")

def hunnidk(msg):
        if "!100k" in msg:
                global jahtimer
                if time.time() > jahtimer:
                        jahtimer = time.time() + 4
                        hunnid = open("hunnidk.txt","r")
                        winners = ""
                        losers = ""
                        for line in hunnid:
                                if "100k" in line:
                                        winners += line.split(" ")[0]+", "
                                elif "1" in line:
                                        losers += line.split(" ")[0]+", "
                        if winners == "" and losers == "":
                                sendMessage(s, "No one has rolled a 100k or a 1 yet FeelsBadMan")
                        else:
                                sendMessage(s, "winners: "+winners)
                                time.sleep(1.3)
                                sendMessage(s, "losers: "+losers)
                        

def find(msg,user):
        if "!find " in msg:
                global findtimer
                if time.time() > findtimer:
                        target2 = msg.split(" ")[1]
                        if target2.lower() == "yoloswagbruh":
                                sendMessage(s, "wouldn't you like to know deIlluminati")
                                return
                        sendMessage(s, "looking for "+target2+" please wait")
                        findtimer = time.time() +10
                        following = ""
                        follows = []
                        followerurl = urlopen("https://api.twitch.tv/kraken/users/"+target2+"/follows/channels?direction=desc&limit=200")
                        #index = 1
                        for word in followerurl.readlines():
                                following += word.strip().decode("utf-8")
                        follows = following.split("follows/channels/")
                        del follows[0]
                        temp = ""
                        namelist = []
                        for element in follows:
                                namelist.append(element[:20].split('"')[0])    
                        watching = ""
                        for channel in namelist:
                                response = urlopen("https://tmi.twitch.tv/group/user/"+channel+"/chatters")
                                readable = response.read().decode("utf-8")
                                chatlist = loads(readable)
                                chatters = chatlist['chatters']        
                                print(channel)
                                if search(chatters, target2.lower()):
                                        if channel == "ethanthejones":
                                                watching += ""
                                        else:
                                                watching += channel+", "
                        if watching != "":
                                sendMessage(s, target2+" is in "+watching)
                        elif watching == "":
                                sendMessage(s, target2+" is not in any channels FeelsBadMan")
                        
#def loogie():
#        num = random.randint(0,1)
#        if num == 1 or num == 0:
#                #sendMessage(s, "/me gargles up a huge loogie and takes aim at chat...")
#                print("gargles")
#                #time.sleep(5)
#                userlist = list(chatlist.values())
#                for i in userlist:
#                        print(i)
#                print(userlist)
#                print(victim);
                
                
                   
#loogie()
while True:
        try:
                readbuffer = readbuffer + s.recv(1024).decode('utf-8')
                temp = str.split(readbuffer, "\n")
                readbuffer = temp.pop()

                for line in temp:
                        line = str.rstrip(line)
                        #print(line.encode("utf-8"))
                        if(line[0] == "P"):
                                s.send(bytes("PONG %s\r\n" % line[1], "UTF-8"))
                                print("sent ping")
                                break
                        user = getUser(line)
                        msg = getMessage(line)
                        now = time.time()
                        
                                
                        if now - updatetime > 100:
                                try:
                                        updatetime = time.time()
                                        response = urlopen("https://tmi.twitch.tv/group/user/"+channel+"/chatters")
                                        readable = response.read().decode("utf-8")
                                        chatlist = loads(readable)
                                        chatters = chatlist['chatters']
                                        updatetime = time.time() +100
                                        print("lists updated")
                                except:
                                        pass
                        print(user + " says: " + str(msg))
                        leaveChan(msg)
                        print(leave)
                        if leave is False:
                                #loogie()
                                #find(msg, user)
                                donate(msg)
                                hunnidk(msg)
                                heypoke(msg,user)
                                color(msg,user)
                                #trivia(msg,trivia_dict,active,used_dict)
                                answer(user, msg, trivia_dict)
                                cringe(msg, cringeTimer)
                                howeh(msg)
                                ninja(msg)
                                jah(msg)
                                give(msg,user, trivia_dict)
                                bots(msg)
                                yaBaby(msg)
                                grady(msg)
                                spit(user,msg)
                                goldduel(user, msg)
                                confirm(msg, goldDict, user)
                                duel(user, channel, msg)
                                winrate(user,msg)
                                winrate2(user,msg)
                                copygrady(msg,user)
        except:  
                print("problem")
                pass




