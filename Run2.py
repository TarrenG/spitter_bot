import string, random, time, webbrowser, requests, json, sys, os, re, math, soundcloud

from datetime import datetime
from json import loads
from urllib.request import urlopen
from Read import getUser, getMessage
from Socket import openSocket, sendMessage, sendWhisper, capReq
from Init import joinRoom
from Settings import channel

s = openSocket()
joinRoom(s)
capReq(s)
readbuffer = ""
last = time.time()

#MODLIST
modlist = ['beza93','ryssh','yoloswagbruh_','grady_wilson','delete_yolo_please','prould1','skyline1478','stopgingerhate','pokegaard']

#TRIVIA STUFF
validTrivia = ['listedtrivia','listedtrivia2','mitchtrivia','SportsTrivia','bigTrivia','misctrivia']

trivia = open("bigTrivia.txt", "r")
activeTrivia = "bigTrivia"
trivia_str = (trivia.read())
#print(trivia_str)
trivia_list = trivia_str.split("\n")
del trivia_list[len(trivia_list)-1]
#print(trivia_list)
question_list = []
answer_list = []
counter = 0
trivia_dict= {}
used_dict = {}
active = False

currAnswer = ""
qNum = -1
for index in trivia_list:
        #print(index+"--")
        #print(counter)
        trivia_dict[counter] = index.split("?")[0] +"|"+ index.split("?")[1]
        #if counter%2 == 0:
          #      trivia_dict[counter] = index
        #else:
         #       trivia_dict[counter - 1] += index
        counter = counter + 1
#print(trivia_dict)
i = 0
trivia_list2 = []
for q in trivia_list:
        trivia_list2.append(i)
        i += 1


#TWITCH API CHATTERS
response = requests.get("https://tmi.twitch.tv/group/user/"+channel+"/chatters") ##################################################
readable = response.text
#print(readable)
chatlist = loads(readable)
#print(chatlist)
chatters = chatlist['chatters']
namesOnly = (readable.split("moderators\": [")[1]).split("],")[0].strip()+","
namesOnly += (readable.split("staff\": [")[1]).split("],")[0].strip()
namesOnly += (readable.split("admins\": [")[1]).split("],")[0].strip()
namesOnly += (readable.split("global_mods\": [")[1]).split("],")[0].strip()
namesOnly += (readable.split("viewers\": [")[1]).split("]")[0].strip()
namesOnly = re.sub("[!@#$\"'\n\t\"      \"]", '', namesOnly)
namesOnly = namesOnly.split(",")
#print(namesOnly)
chatterlist = chatters.values()
#request = requests.get("https://tmi.twitch.tv/group/user/"+channel+"/chatters")
#print(request.text)


#print(chatlist.values())

#UPDATING VARS
loogieOff = False
loogied = "-"
loogiedTimer = "0.0"
pokebot = 0
leave = False
goldDict = {}
ignorelist = []
counter  = 0
cringes = []
cringestring = ""
index_list = []
testIds = []

#TIMERS
timer4sec = time.time()
findtimer = time.time()
triviatimer = time.time()
musictimer = time.time()
confirmtimer = time.time()
golddueltimer = time.time()
dueltimer = time.time()
updatetime = time.time()
counterTimer = time.time()


#YOUTUBE API CRINGE PLAYLIST 
cringe1 = requests.get("https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails%2C+id&playlistId=LLjqZhH6L-O9zC774cNLoeXA&maxResults=50&pageToken=CDIQAQ&key=AIzaSyAZhQ9hTXD26ZAVG61Byfi3fg9usU2-T4Q")

cringe2 = requests.get("https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails%2C+id&playlistId=LLjqZhH6L-O9zC774cNLoeXA&maxResults=50&pageToken=CDIQAA&key=AIzaSyAZhQ9hTXD26ZAVG61Byfi3fg9usU2-T4Q")

cringe3 = requests.get("https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails%2C+id&playlistId=LLjqZhH6L-O9zC774cNLoeXA&maxResults=50&pageToken=CGQQAA&key=AIzaSyAZhQ9hTXD26ZAVG61Byfi3fg9usU2-T4Q")


videoIds = []

cringestring = cringe1.text + cringe2.text + cringe3.text
testIds = cringestring.split('"videoId": "')
for index in testIds:
        videoIds.append(index[:11])
del videoIds[0]

#SOUNDCLOUD
client = soundcloud.Client(client_id="bd93144f19440691b9740cd333d18279")

#MUSIC
musics = []
music1 = requests.get("https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails%2C+id&playlistId=PLA0CABD0F5F112418&maxResults=50&pageToken=CDIQAQ&key=AIzaSyAZhQ9hTXD26ZAVG61Byfi3fg9usU2-T4Q")

music2 = requests.get("https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails%2C+id&playlistId=PLA0CABD0F5F112418&maxResults=50&pageToken=CDIQAA&key=AIzaSyAZhQ9hTXD26ZAVG61Byfi3fg9usU2-T4Q")

music3 = requests.get("https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails%2C+id&playlistId=PLA0CABD0F5F112418&maxResults=50&pageToken=CGQQAA&key=AIzaSyAZhQ9hTXD26ZAVG61Byfi3fg9usU2-T4Q")

music4 = requests.get("https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails%2C+id&playlistId=PLA0CABD0F5F112418&maxResults=50&pageToken=CJYBEAA&key=AIzaSyAZhQ9hTXD26ZAVG61Byfi3fg9usU2-T4Q")

music5 = requests.get("https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails%2C+id&playlistId=PLA0CABD0F5F112418&maxResults=50&pageToken=CMgBEAA&key=AIzaSyAZhQ9hTXD26ZAVG61Byfi3fg9usU2-T4Q")

music6 = requests.get("https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails%2C+id&playlistId=PLA0CABD0F5F112418&maxResults=50&pageToken=CPoBEAA&key=AIzaSyAZhQ9hTXD26ZAVG61Byfi3fg9usU2-T4Q")

music7 = requests.get("https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails%2C+id&playlistId=PLA0CABD0F5F112418&maxResults=50&pageToken=CKwCEAA&key=AIzaSyAZhQ9hTXD26ZAVG61Byfi3fg9usU2-T4Q")


musicstring = music1.text + music2.text + music3.text + music4.text + music5.text + music6.text + music7.text
plsIds = musicstring.split('"videoId": "')
musicIds = []

for index in plsIds:
        musicIds.append(index[:11])
        
del musicIds[0]


i = 0
full_list = []
for index in musicIds:
        index_list.append(i)
        full_list.append(i)
        i += 1
#TOP 100
topList = []
top1 = requests.get("https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails%2C+id&playlistId=PLx0sYbCqOb8TBPRdmBHs5Iftvv9TPboYG&maxResults=50&pageToken=CDIQAQ&key=AIzaSyAZhQ9hTXD26ZAVG61Byfi3fg9usU2-T4Q")

top2 = requests.get("https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails%2C+id&playlistId=PLx0sYbCqOb8TBPRdmBHs5Iftvv9TPboYG&maxResults=50&pageToken=CDIQAA&key=AIzaSyAZhQ9hTXD26ZAVG61Byfi3fg9usU2-T4Q")

topstring = top1.text + top2.text
topIds = topstring.split('"videoId": "')

for index in topIds:
        topList.append(index[:11])
        
del topList[0]
        
print(str(len(index_list))+" "+str(len(full_list))+" "+str(len(musicIds)))
print("donezo")

def forceUpdate(msg,user):
        if "!update" in msg:
                global musics
                global musicIds
                musics = []
                music1 = requests.get("https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails%2C+id&playlistId=PLA0CABD0F5F112418&maxResults=50&pageToken=CDIQAQ&key=AIzaSyAZhQ9hTXD26ZAVG61Byfi3fg9usU2-T4Q")

                music2 = requests.get("https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails%2C+id&playlistId=PLA0CABD0F5F112418&maxResults=50&pageToken=CDIQAA&key=AIzaSyAZhQ9hTXD26ZAVG61Byfi3fg9usU2-T4Q")

                music3 = requests.get("https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails%2C+id&playlistId=PLA0CABD0F5F112418&maxResults=50&pageToken=CGQQAA&key=AIzaSyAZhQ9hTXD26ZAVG61Byfi3fg9usU2-T4Q")

                music4 = requests.get("https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails%2C+id&playlistId=PLA0CABD0F5F112418&maxResults=50&pageToken=CJYBEAA&key=AIzaSyAZhQ9hTXD26ZAVG61Byfi3fg9usU2-T4Q")

                music5 = requests.get("https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails%2C+id&playlistId=PLA0CABD0F5F112418&maxResults=50&pageToken=CMgBEAA&key=AIzaSyAZhQ9hTXD26ZAVG61Byfi3fg9usU2-T4Q")

                music6 = requests.get("https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails%2C+id&playlistId=PLA0CABD0F5F112418&maxResults=50&pageToken=CPoBEAA&key=AIzaSyAZhQ9hTXD26ZAVG61Byfi3fg9usU2-T4Q")

                music7 = requests.get("https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails%2C+id&playlistId=PLA0CABD0F5F112418&maxResults=50&pageToken=CKwCEAA&key=AIzaSyAZhQ9hTXD26ZAVG61Byfi3fg9usU2-T4Q")


                musicstring = music1.text + music2.text + music3.text + music4.text + music5.text + music6.text + music7.text
                plsIds = musicstring.split('"videoId": "')
                musicIds = []

                for index in plsIds:
                        musicIds.append(index[:11])
                        
                del musicIds[0]


                i = 0
                full_list = []
                for index in musicIds:
                        index_list.append(i)
                        full_list.append(i)
                        i += 1

                global topList
                global topIds
                topList = []
                top1 = requests.get("https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails%2C+id&playlistId=PLx0sYbCqOb8TBPRdmBHs5Iftvv9TPboYG&maxResults=50&pageToken=CDIQAQ&key=AIzaSyAZhQ9hTXD26ZAVG61Byfi3fg9usU2-T4Q")

                top2 = requests.get("https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails%2C+id&playlistId=PLx0sYbCqOb8TBPRdmBHs5Iftvv9TPboYG&maxResults=50&pageToken=CDIQAA&key=AIzaSyAZhQ9hTXD26ZAVG61Byfi3fg9usU2-T4Q")

                topstring = top1.text + top2.text
                topIds = topstring.split('"videoId": "')

                for index in topIds:
                        topList.append(index[:11])
                        
                del topList[0]

                global response
                global readable
                global chatterlist
                global namesOnly
                global chatters
                global chatlist
                response = requests.get("https://tmi.twitch.tv/group/user/"+channel+"/chatters") ##################################################
                readable = response.text
                #print(readable)
                chatlist = loads(readable)
                #print(chatlist)
                chatters = chatlist['chatters']
                namesOnly = (readable.split("moderators\": [")[1]).split("],")[0].strip()+","
                namesOnly += (readable.split("staff\": [")[1]).split("],")[0].strip()
                namesOnly += (readable.split("admins\": [")[1]).split("],")[0].strip()
                namesOnly += (readable.split("global_mods\": [")[1]).split("],")[0].strip()
                namesOnly += (readable.split("viewers\": [")[1]).split("]")[0].strip()
                namesOnly = re.sub("[!@#$\"'\n\t\"      \"]", '', namesOnly)
                namesOnly = namesOnly.split(",")
                #print(namesOnly)
                chatterlist = chatters.values()
                print("update forced " +str(len(musicIds)))



def search(values, searchFor):
        print("entering")
        for k in values:
                #print("k is "+k)
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
                global timer4sec
                if time.time() > timer4sec:
                        timer4sec = time.time() + 4
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
                                question = question_info.split("|")[0]+ "?"
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
                        global loogied
                        print(loogied)
                        hunnidk = open("hunnidk.txt","a")
                        records = open("record.txt", "a")
                        with open('top.txt','r') as f:
                                top = f.readline()
                        f.close()
                        with open('low.txt','r') as f:
                                low = f.readline()
                        f.close()
                        loser = low.split(" ")[0]
                        lowest = int(low.split(" ")[1])
                        leader = top.split(" ")[0]
                        highest = int(top.split(" ")[1])
                        print("leader: "+leader+", "+str(highest))
                        target =  msg.split(" ")[1]
                        if (target.lower() == "usuallylosesduels"):
                        	target = "usuallyhigh"
                        dueltimer = time.time() + 3.2
                        #LOOGIE ROLL CONSTRAINTS
                        if (user.lower() != loogied and target.lower() != loogied):
                                roll = random.randint(1,100000)
                                print("no loogied")
                        elif (user.lower() == loogied):
                                roll = random.randint(1,70000)
                                print("user loogied")
                        else:
                                roll = random.randint(30000,100000)
                                print("target loogied")
                        if user.lower() == target.lower():
                                sendMessage(s, "you can't duel yourself ideot KKona")
                                return
                        elif search(chatters, target.lower()) == False:
                                sendMessage(s,"I can't find that user WutFace")
                                return
                       # elif target.lower() == "usuallyhigh":
                       #         hacks = random.randint(50001,100000)
                       #         if hacks > 50000:
                       #                 sendMessage(s,"/me spits on "+target+"! ("+str(hacks)+")")
                       #                 return
                       #         else:
                       #                 sendMessage(s,"/me spits on "+user+"! ("+str(hacks)+")")
                       #                 return
                                        
                        elif roll > 50000:
                                sendMessage(s,"/me spits on "+target+"! ("+str(roll)+")")
                                records.write(user+" win"+" \r\n")
                                records.write(target+ " lose"+" \r\n")
                                records.close()
                                if roll == 100000:
                                        hunnidk.write(user +" 100k \r\n")
                                        hunnidk.close()
                                #keeping track of highest roll
                                if roll > highest:
                                        lines = open("top.txt","r").readlines()
                                        lines[0] = user+" "+str(roll)
                                        top = open('top.txt','w')
                                        for line in lines:
                                                top.write(line)
                                        top.close()
                                        print("higher")
                                return
                        elif roll <50001:
                                sendMessage(s,"/me spits on "+user+"! ("+str(roll)+")")
                                records.write(target+" win"+" \r\n")
                                records.write(user+ " lose"+" \r\n")
                                records.close()
                                if roll == 1:
                                        hunnidk.write(user +" 1 \r\n")
                                        hunnidk.close()
                                #keeping track of lowest roll
                                if roll < lowest:
                                        lines = open("low.txt","r").readlines()
                                        lines[0] = user+" "+str(roll)
                                        low = open('low.txt','w')
                                        for line in lines:
                                                low.write(line)
                                        top.close()
                                return

def spit(user,msg):
        if "!spit " in msg:
                global timer4sec
                if time.time() > timer4sec:
                        target = msg.split(" ")[1]
                        timer4sec = time.time() + 4
                        if search(chatters, target.lower()) ==  False:
                                sendMessage(s, "I can't find that user WutFace")
                        elif target.lower() == "yoloswagbruh_":
                                sendMessage(s, "never spit on yolo DansGame")
                                return
                        elif target.lower() == "pokegaard":
                                sendMessage(s, "/me splts on pokegaard PuppeyFace")
                                return
                        elif target.lower() == "grady_wilson":
                                if user.lower() != "yoloswagbruh_":
                                
                                        sendMessage(s, "/me spits on "+user+" 4Hand")
                                        return
                                else:
                                        sendMessage(s, "/me spits on "+target+" 4Hand")
                                        return
                        else:
                                sendMessage(s, "/me spits on "+target)

def tDuel(user, msg):
        if "!battle " in msg:
                global golddueltimer
                if time.time() > golddueltimer:
                        golddueltimer = time.time() + 6
                        records = open("record.txt", "a")
                        target =  msg.split(" ")[1]
                        wager = 5
                        if target+" " in msg:
                                wager = int(msg.split(" ")[2])
                        if math.isnan(wager):
                                wager = int(5)
                        if search(chatters, target.lower()) == False:
                                sendMessage(s, "I can't find that person WutFace")
                                return
                        if int(wager) / 1:
                                if int(wager) < 0:
                                        return
                                hashq = random.getrandbits(128)
                                hashstr = str(hashq)[0:4]
                                sendMessage(s, target+", you have been challenged to a timeout battle by "+user+" for "+str(wager)+" seconds, type !confirm "+hashstr+" to accept")
                                goldDict[hashstr] = user+" "+target+" "+str(wager)
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
                        wager = int(infostring.split(" ")[2])
                        roll = random.randint(1,100)
                        print(str(challenger)+" is the challenger "+str(challengee)+" is the target "+str(wager)+" is the wager")
                        if user.lower() == challengee.lower():
                                #print("made it here")
                                if search(chatters, challenger.lower()) == False:
                                        sendMessage(s,"both users need to be in chat for timeout duels")
                                        return
                                elif roll > 50:
                                        time.sleep(.5)
                                        #sendMessage(s,str(challenger)+" rolls a "+str(roll)+", "+str(challengee)+" is timed out for "+str(wager)+" seconds!")
                                        sendMessage(s, str(challengee)+",  ded notsquishY "+"   "+"roll: "+str(roll)+" duration: "+str(wager))
                                        sendWhisper(s,"FourTwentyBot", "/timeout "+challengee+" "+ str(wager))
                                        del goldDict[duelID]
                                        return
                                elif roll <51:
                                        time.sleep(.5)
                                        #sendMessage(s,str(challenger)+" rolls a "+str(roll)+", "+str(challenger)+" is timed out for "+str(wager)+" seconds!")
                                        sendMessage(s, str(challenger)+",  ded notsquishY"+"   "+"roll: "+str(roll)+" duration: "+str(wager))
                                        sendWhisper(s,"FourTwentyBot", "/timeout "+challenger+" "+ str(wager))
                                        del goldDict[duelID]
                                        return
                        

def winrate(user,msg):
        if "!winrate" == msg:
                global timer4sec
                wins = 0
                total = 0
                if time.time() > timer4sec:
                        timer4sec = time.time() + 4
                        records = open("record.txt","r")
                        for line in records:
                                if user.lower() in line.lower():
                                        if "win" in line:
                                                wins += 1
                                                total += 1
                                        else:
                                                total += 1
                        if (user.lower() == "pokegaard"):
                                global pokebot
                                wins = wins - pokebot
                                total = total - pokebot
                        if total > 0:
                                winrate = (wins / total)*100
                                sendMessage(s, user+" wins: "+str(wins)+", total: "+str(total)+", winrate: "+str("%.2f" % winrate)+"%")
                        else:
                                sendMessage(s, "you need to play more matches, "+user)
                        return
                
def winrate2(user,msg):
        if "!winrate " in msg:
                global timer4sec
                target = msg.split(" ")[1]
                wins = 0
                total = 0
                if search(chatters, target.lower()) == True:
                        if time.time() > timer4sec:
                                timer4sec = time.time() + 4
                                records = open("record.txt","r")
                                target = target + " "
                                for line in records:
                                        if target.lower() in line.lower():
                                                if "win" in line:
                                                        wins += 1
                                                        total += 1
                                                else:
                                                        total += 1
                                if (target.lower() == "pokegaard"):
                                        global pokebot
                                        wins = wins - pokebot
                                        total = total - pokebot
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
        if "!grady" in msg:
                global timer4sec
                if time.time() > timer4sec:
                        timer4sec = time.time() + 5
                        #sendMessage(s, "whose hand is that KKona")
                        sendMessage(s, "we found aliens 4Hand http://imgur.com/tU1uDPN")

def cringe(msg, timer4sec):
        if "!cringe" in msg:
                if (time.time() > timer4sec):
                        timer4sec = time.time() + 30
                        num = random.randint(0,int(len(videoIds) - 1))
                        print(str(len(videoIds)))
                        sendMessage(s, "cringe video #"+str(num)+" : https://www.youtube.com/watch?v="+videoIds[int(num)])    
                        return


def stronk(msg):
        if "!find doctorstronk" in msg.lower():
                global timer4sec
                if time.time() > timer4sec:
                        timer4sec = time.time() + 4
                        sendMessage(s, "leave doctorstronk alone BabyRage")
                        

def ignore(msg,user):
        if "!ig" in msg:
                if user.lower() in modlist:
                        target = msg.split(" ")[1].lower()
                        ignorelist.append(target)

def unignore(msg,user):
        if "!unig" in msg:
                if user.lower() in modlist:
                        target = msg.split(" ")[1].lower()
                        if target in ignorelist:
                                ignorelist.remove(target)
                                        


def howeh(msg):
        if "!howeh" in msg:
                global timer4sec
                if time.time() > timer4sec:
                        timer4sec = time.time() + 4
                        sendMessage(s, "@Howeh https://www.youtube.com/watch?v=_F95GCRK7RU EleGiggle")
                        #https://www.youtube.com/watch?v=P-hk6gnoxqY&feature=youtu.be&t=2m25s
def basedgod(msg):
        if "! BasedGod" in msg:
                global timer4sec
                if time.time() > timer4sec:
                        timer4sec = time.time() + 4
                        sendMessage(s, "https://www.youtube.com/watch?v=48XQJdMzu2g BasedGod")
                        
def ninja(msg):
        if "!ninja" in msg:
                global timer4sec
                if time.time() > timer4sec:
                        timer4sec = time.time() + 4
                        sendMessage(s, "Ninja!? https://www.youtube.com/watch?v=NXUTLNPNnG4 bUrself")


def jah(msg):
        if "!jah" in msg:
                global timer4sec
                if time.time() > timer4sec:
                        timer4sec = time.time() + 4
                        sendMessage(s,"BrokeBack https://imgur.com/a/SNLzs")
def leaveChan(msg,user):
        global leave
        if "!leave" == msg:
                if not leave:
                        sendMessage(s, "ok bye KKona 4Hand")
                        leave = True
        elif "!join" in msg:
                if leave and user.lower() in modlist:
                        sendMessage(s, "back again tell a friend KKona")
                        leave = False 
                
def heypoke(msg,user):
        if "!poke" in msg:
                global timer4sec
                if time.time() > timer4sec:
                        timer4sec = time.time() + 4
                        sendMessage(s, "you weird homie https://www.youtube.com/watch?v=Jug2HZ3dkoc&feature=youtu.be&t=4m4s")
                        
def donate(msg):
        if "!donate" in msg:
                global timer4sec
                if time.time() > timer4sec:
                        timer4sec = time.time() + 4
                        sendMessage(s,"donate for hacks at https://streamtip.com/t/yoloswagbruh thx MingLee")


def dev(msg):
        if "!spitterbot" in msg:
                global timer4sec
                if time.time() > timer4sec:
                        timer4sec = time.time() + 4
                        sendMessage(s,"I'm a bot developed by Grady_Wilson 4Hand")

def hunnidk(msg):
        if "!100k" in msg:
                global timer4sec
                if time.time() > timer4sec:
                        timer4sec = time.time() + 4
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
                                winners = winners[:-2]
                                losers = losers[:-2]
                                if winners != "":
                                        sendMessage(s, "100k Hall of Fame PogChamp : "+winners)
                                time.sleep(1.3)
                                if losers != "":
                                	sendMessage(s, "1's Hall of Shame EleGiggle : "+losers)
                        

def find(msg,user):
        if "!find " in msg:
                global findtimer
                if time.time() > findtimer:
                        target2 = msg.split(" ")[1]
                        if target2.lower() == "yoloswagbruh_":
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
                                

def music(msg,index_list):
        if "!pls" in msg.lower():
                global musictimer
                if (time.time() > musictimer):
                        musictimer = time.time() + 4
                        if len(index_list) == 0:
                                index_list = full_list
                        num_index = random.randint(0,int(len(index_list) - 1))
                       # print(str(num_index))
                        num = int(index_list[num_index])
                        #print(str(num))
                        del index_list[num_index]
                        print("size: "+str(len(index_list)))
                        sendMessage(s, "MitchPls #"+str(num)+" : https://www.youtube.com/watch?v="+musicIds[int(num)])    
                        return

def openTrivia(msg,user):
        if "!load " in msg and user.lower() in modlist:
                desiredList = msg.split(" ")[1]
                print("in load")
                if desiredList in validTrivia:
                        try:
                                trivia = open(desiredList+".txt", "r")
                                activeTrivia = desiredList
                                global activeTrivia
                                print("opened")
                                trivia_str = (trivia.read())
                                #print(trivia_str)
                                trivia_list = trivia_str.split("\n")
                                del trivia_list[len(trivia_list)-1]
                                #print(trivia_list)
                                global question_list
                                question_list = []
                                global answer_list
                                answer_list = []
                                counter = 0
                                global trivia_dict
                                trivia_dict= {}
                                global used_dict
                                used_dict = {}
                                active = False
                                
                                global currAnswer
                                currAnswer = ""
                                global qNum
                                qNum = -1
                                for index in trivia_list:
                                        #print(index+"--")
                                        #print(counter)
                                        trivia_dict[counter] = index.split("?")[0] +"|"+ index.split("?")[1]
                                        #if counter%2 == 0:
                                          #      trivia_dict[counter] = index
                                        #else:
                                         #       trivia_dict[counter - 1] += index
                                        counter = counter + 1
                                #print(trivia_dict)
                                i = 0
                                trivia_list2 = []
                                for q in trivia_list:
                                        trivia_list2.append(i)
                                        i += 1
                                global trivia_list
                                sendMessage(s,"trivia loaded: "+desiredList)
                                qNum = -1
                                currAnswer = "asdklasdlkhasdasadvvnzzzzmfs"
                        except:
                                sendMessage(s,"error loading trivia")
                                pass
                else:
                        sendMessage(s,"not a valid trivia list, try one of these: "+str(validTrivia))
                

def trivia2(msg,trivia_list):
        global currAnswer
        global qNum
        if "!trivia" in msg:
                if len(trivia_list) == 0:
                         print("out of questions")
                         return
                elif qNum == -1:
                        qNum = random.randint(0,len(trivia_list)-1)
                        print("qNum is  -1 / no valid question")
                        question = trivia_list[qNum].split("?")[0]
                        currAnswer = trivia_list[qNum].split("?")[1]
                        sendMessage(s,question+"?")
                        print("currAnswer: "+str(currAnswer)+", qNum: "+ str(qNum))
                        time.sleep(1)
                        return
                else:
                        question = trivia_list[qNum].split("?")[0]
                        sendMessage(s,"current question: "+question+"?")
                        time.sleep(1)
                        return

def answer2(msg,user,trivia_list):
        global currAnswer
        global qNum
        global currAList
        #print("currAnswer: "+str(currAnswer)+", qNum: "+ str(qNum))
        if " or " in currAnswer.lower():
                try:        
                        currAList = currAnswer.lower().split(" or ")
                        if (int(currAList.index(msg.lower())) + 1):
                                if currAList != []:
                                        sendMessage(s,user+" got the correct answer: "+str(currAList))
                                        #tRecords = open("tRecords.txt","r+")
                                        #found = 0
                                        #lines = tRecords.readlines()
                                        #for line in lines:
                                        #        print("line: "+line)
                                        #        pts = line.split(" ")[1]
                                        #        print(line.split(" ")[0])
                                        #        if (line.split(" ")[0].lower() == user.lower()):
                                        #                pts = int(pts)
                                        #                newPts = pts+1
                                        #                old = line
                                        #                new = user+" "+str(pts)+"\n"
                                        #                line = line.replace(line, user+" "+str(pts)+"\n")
                                        #                print("incremented pts"+str(newPts))
                                        #                found = 1
                                        #                break
                                        #if (found == 0):
                                        #        tRecords.write(user+" "+str(1)+"\n")
                                        #        print("gave 1 pt")
                                        #tRecords.write(line)
                                        #tRecords.close()
                                        del trivia_list[qNum]
                                        qNum = -1
                                        currAnswer = "asdklasdlkhasdasadvvnzzzzmfs"
                                        return
                except:
                        pass
        elif currAnswer.lower() in msg.lower():
                if currAnswer != "":
                        sendMessage(s,user+" got the correct answer: "+currAnswer)
                del trivia_list[qNum]
                qNum = -1
                currAnswer = "asdklasdlkhasdasadvvnzzzzmfs"
                return

def skip(msg,user,trivia_list):
        global currAnswer
        global qNum
        if "!skip" in msg and qNum != -1 :
                if user.lower() in modlist:
                        global timer4sec
                        if time.time() > timer4sec:
                                del trivia_list[qNum]
                                qNum = -1
                                if " or " in currAnswer.lower():
                                        currAList = currAnswer.split(" or ")
                                        if currAList != []:
                                                sendMessage(s,"skipped, correct answer: "+str(currAList))
                                else:
                                        sendMessage(s,"skipped, correct answer: "+currAnswer)
                                time.sleep(1.8)
                                qNum = random.randint(0,len(trivia_list)-1)
                                print("qNum is"+str(qNum))
                                question = trivia_list[qNum].split("?")[0]
                                currAnswer = trivia_list[qNum].split("?")[1]
                                sendMessage(s,question+"?")
                                return
                                

def copygrady(msg,user):
        if user.lower() == "yoloswagbruh_":
                #sendMessage(s,msg+" 4Hand")
                sendWhisper(s,user,msg)
                return

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)


def follows(msg,user):
        #https://api.twitch.tv/kraken/users/grady_wiison/follows/channels
        if "!followage" == msg.split(" ")[0]:
                global timer4sec
                hehe = random.randint(5,13)
                if time.time() > timer4sec+4:
                        timer4sec = time.time()
                        name1 = msg.split(" ")[1]
                        name2 = "watchmeblink1"
                        if name1+" " in msg:
                                name2 = msg.split(" ")[2]
                        if len(name2) < 3:
                                name2 = "watchmeblink1"
                        print("name1 is "+name1)
                        print("name2 is "+name2)

                        followsurl = requests.get("https://api.twitch.tv/kraken/users/"+ name1 +"/follows/channels/"+name2)
                        found = followsurl.text[14:25]
                        print("found: "+found)
                        if name1[0:1] == "!" or name1[0:1] == "/" or name1[0:1] == "." or name2[0:1] == "!":
                                sendMessage(s,user+" thinks hes clever, but he aint")
                                return
                        if found[0:3] != "Fou" :
                                today = datetime.today()
                                print(today)
                                change = days_between(found[1:].split("T")[0],str(today).split(" ")[0])
                                #if (name1.lower() == 'FOLLOWER NAME' and name2.lower() == 'FOLLOWED NAME'):
                                #        change = change+152
                                
                                if (change < 365):
                                        sendMessage(s, name1+" has been following "+name2+" for "+str(change)+" days")
                                else:
                                        years = str(int(change / 365))
                                        days = str(change % 365)
                                if int(years) == 1:
                                        sendMessage(s, name1+" has been following "+name2+" for "+years+" year and "+days+" days")
                                else:
                                        sendMessage(s, name1+" has been following "+name2+" for "+years+" years and "+days+" days")
                        else:
                                sendMessage(s,name1+" is not following "+name2)

def age(msg,user):
        if "!age" == msg.split(" ")[0]:
                global timer4sec
                if time.time() > timer4sec+4:
                        timer4sec = time.time()
                        #https://api.twitch.tv/kraken/users/thisistux
                        name = user
                        if "!age " in msg:
                                name = msg.split(" ")[1]
                        if len(name) < 3:
                                name = user
                        ageUrl = requests.get("https://api.twitch.tv/kraken/users/"+name)
                        print(ageUrl.text[0:19])
                        if (ageUrl.text[0:20] == '{"error":"Not Found"'):
                                sendMessage(s, "that account doesn't exist")
                                return
                        elif(ageUrl.text[0:31] == '{"error":"Unprocessable Entity"'):
                                sendMessage(s, "that account is banned FeelsBadMan")
                                return
                        ageText = ageUrl.text.split('created_at":"')[1]
                        ageText = ageText.split('","')[0]
                        today = datetime.today()
                        print(str(today))
                        change = days_between(ageText.split("T")[0],str(today).split(" ")[0])
                        print(str(change))
                        if (change > 365):
                                years = str(int(change / 365))
                                days = str(change % 365)
                                if (int(years) == 1):
                                        sendMessage(s, str(name)+" was created "+years+" year and "+str(days)+" days ago ("+str(ageText.split("T")[0])+")")
                                        return
                                else:
                                        sendMessage(s, str(name)+" was created "+years+" years and "+str(days)+" days ago ("+str(ageText.split("T")[0])+")")
                                        return
                        else:
                                sendMessage(s, str(name)+" was created "+str(change)+" days ago ("+str(ageText.split("T")[0])+")")
                                return

        

                        
                        
                        
                        

def currTrivia(msg):
        if "!currtrivia" in msg.lower():
                global timer4sec
                global activeTrivia
                global trivia_list
                if time.time() > timer4sec:
                        timer4sec = time.time()+4
                        print(len(trivia_list))
                        sendMessage(s, "current trivia list: "+activeTrivia)
                        return

def totalduels(msg):
        global timer4sec
        global ignorelist
        if "!duelcount" in msg and time.time() > timer4sec:
                print(ignorelist)
                timer4sec = time.time()+4
                records = open("record.txt","r")
                total = 0
                for line in records:
                        if "lose" or "win" in line:
                                total += 1
                total = total/2
                total = int(total)
                "{:,}".format(total)
                sendMessage(s, "There have been "+str("{:,}".format(total))+" duels so far 4Hand")

def top(msg):
        global timer4sec
        if "!top" == msg and time.time() > timer4sec:
                timer4sec = time.time()+4
                with open('top.txt','r') as f:
                        top = f.readline()
                f.close()
                leader = top.split(" ")[0]
                highest = int(top.split(" ")[1])
                sendMessage(s, "Current highest: "+leader+" with a "+str(highest)+" KKona Clap")
                return

def low(msg):
        global timer4sec
        if "!low" == msg and time.time() > timer4sec:
                timer4sec = time.time()+4
                with open('low.txt','r') as f:
                        low = f.readline()
                f.close()
                loser = low.split(" ")[0]
                low = int(low.split(" ")[1])
                sendMessage(s, "Current lowest: "+loser+" with a "+str(low)+" EleGiggle Clap")
                return
                
        


def distance(msg):
        if "!distance " in msg:
                global timer4sec
                if time.time() > timer4sec:
                        try:
                                timer4sec = time.time() + 4
                                origin = msg.split(",")[0][8:]
                                destination = msg.split(",")[1]
                                mode = "driving"
                                if len(msg.split(",")) > 2:
                                        if "walk" in msg.split(",")[2]:
                                                mode = "walking"
                                        if "bi" in msg.split(",")[2]:
                                                mode = "bicycling"
                                origin.replace(" ","+")
                                destination.replace(" ","+")
                                info = requests.get("https://maps.googleapis.com/maps/api/distancematrix/json?origins="+origin+"&destinations="+destination+"&mode="+mode+"&language=EN&key=AIzaSyAZhQ9hTXD26ZAVG61Byfi3fg9usU2-T4Q")
                                dest_addr = info.text.split('"destination_addresses" : [ "')[1]
                                dest_addr = dest_addr.split('"')[0]
                                print(dest_addr)
                                origin_addr = info.text.split('"origin_addresses" : [ "')[1]
                                origin_addr = origin_addr.split('"')[0]
                                print(origin_addr)
                                distance = info.text.split('"text" : "')[1]
                                distance = distance.split('"')[0]
                                travel_time = info.text.split('"text" : "')[2]
                                travel_time = travel_time.split('"')[0]
                                sendMessage(s, distance+" from ["+origin_addr+"] to ["+dest_addr+"] taking roughly "+travel_time+" if you are "+mode)
                                return
                        except:
                                sendMessage(s,"Couldn't find a route WutFace")
                                return

def hostViews(hostsList):
        i = 0
        totalHC = 0
        while i <= len(hostsList):
                print("i is :"+ str(i))
                hostID = hostsList[1].split(',"target_id":')[0] #hosts.text.split('"host_login":"')[1]
                hostID = hostID.split('","target_login":')[0]
                print(hostID)
                hostChatters = requests.get("https://tmi.twitch.tv/group/user/"+hostID+"/chatters")
                hostChatters = hostChatters.text.split('chatter_count": ')[1]
                hostChatters = hostChatters.split(",")[0]
                print("hosted chatters for "+str(hostID)+": "+str(hostChatters))
                #print("\n" + str(hostsList)+ "\n")
                totalHC = totalHC + int(hostChatters)
                del hostsList[0]
                i = i+1
               # print("\n" + str(hostsList))
                return totalHC
        

def viewbot(msg):
        if "!botcheck " in msg:
                global timer4sec
                if time.time() > timer4sec:
                        timer4sec = time.time() + 4
                        channel =  msg.split(" ")[1].lower()
                        response1 = requests.get("https://api.twitch.tv/kraken/streams/"+channel)
                        #print(str(response1.text[1:7]))
                        if (response1.text[1:14] == '"stream":null'):
                                sendMessage(s, channel+" is not live")
                                return
                        if (response1.text[1:7] == '"error'):
                                sendMessage(s, channel+" is not a real channel")
                                return
                        viewers = response1.text.split('viewers":')[1]
                        viewers = viewers.split(",")[0]
                        _id = response1.text.split('_id":')[2]
                        _id = _id.split(",")[0]
                        hosts = requests.get("http://tmi.twitch.tv/hosts?include_logins=1&target="+_id)
                        hostsList = hosts.text.split('host_login":"')
                        
                        hostCount = len(hostsList) - 1
                        #print(" ")
                        #print(hostsList[1:])
                        #print(" ")
                        #hostChatters = 0
                        #print(hostCount)
                        #if hostCount <= 10:
                         #       try:
                          #              print("getting host views")
                          #              hostChatters = hostViews(hostsList)
                          #              print(str(hostChatters) + " is host chatters")
                          #      except:
                          #              print("host view error")
                        # # #              hostChatters = hostViews(hostsList)
                                        #viewbot(msg)
                                #i = 0
                                #while i <= len(hostsList):
                                #        print("i is :"+ str(i))
                                #        hostID = hostsList[1].split(',"target_id":')[0] #hosts.text.split('"host_login":"')[1]
                                #        hostID = hostID.split('","target_login":')[0]
                                #        print(hostID)
                                #        hostChatters = requests.get("https://tmi.twitch.tv/group/user/"+hostID+"/chatters")
                                #        hostChatters = hostChatters.text.split('chatter_count": ')[1]
                                #        hostChatters = hostChatters.split(",")[0]
                                #        print("hosted chatters for "+str(hostID)+": "+hostChatters)
                                #        print("\n" + str(hostsList)+ "\n")
                                #        del hostsList[0]
                                #        i = i+1
                                #        print("\n" + str(hostsList))
                                        
                                        
                        #print(hosts)
                        #print(_id)
                        #print(viewers+" is viewers")
                        #viewers = int(viewers) + int(hostChatters)
                        response2 = requests.get("https://tmi.twitch.tv/group/user/"+channel+"/chatters")
                        try:
                                #print(viewers)
                                #viewers = int(viewers + hostChatters)
                                chatters = response2.text.split('chatter_count":')[1]
                                chatters = chatters.split(",")[0]
                                ratio = (float(chatters)/float(viewers))*100
                                if (ratio <= 20):
                                        emote = 'MrDestructoid'
                                elif (ratio <= 40 and ratio > 20):
                                        emote = 'WutFace'
                                elif (ratio <= 60 and ratio > 40):
                                        emote = 'ResidentSleeper'
                                elif (ratio <= 70 and ratio > 60):
                                        emote = 'OMGScoots'
                                elif (ratio <= 80 and ratio > 70):
                                        emote = 'SeemsGood'
                                elif  (ratio <=90 and ratio > 80):
                                        emote = 'FeelsGoodMan'
                                elif (ratio <=98 and ratio > 90):
                                        emote = 'PogChamp'
                                elif (ratio > 100):
                                        emote = '(puke)'
                                else:
                                        emote = 'NotLikeThis'
                                        
                                #if (hostChatters != 0):
                                #        sendMessage(s, channel+": "+viewers+" viewers, "+chatters+" in chatlist, "+str(hostCount) +" hosts, "+str(hostChatters)+" viewers from host, "+ str("%.2f" % ratio)+"% interaction "+ emote)
                                #        return
                                if (hostCount > 1 or hostCount == 0):
                                        sendMessage(s, channel+": "+viewers+" viewers, "+chatters+" in chatlist, "+str(hostCount) +" hosts, "+ str("%.2f" % ratio)+"% interaction "+ emote)
                                        return
                                else:
                                        sendMessage(s, channel+": "+viewers+" viewers, "+chatters+" in chatlist, "+str(hostCount) +" host, "+ str("%.2f" % ratio)+"% interaction "+ emote)
                                        return
                        except:
                                print("calling again")
                                donatetimer = donatetimer - 4
                                viewbot(msg)


                                
ans = 1273982173871289378912738912879389127389718293789217
def mathTrivia(msg):
        if "!dork" in msg:
                global ans
                global triviatimer
                if triviatimer < time.time():
                        if ans == 1273982173871289378912738912879389127389718293789217:
                                triviatimer = time.time() + 3
                                num1 = random.randint(1,200)
                                num2 = random.randint(1,200)
                                operation = random.randint(0,4)
                                if (operation == 0):
                                        sendMessage(s, ""+str(num1) +" * "+str(num2)+" = ?")
                                        op = " * "
                                        ans = num1 * num2
                                        return
                                elif (operation == 1):
                                        sendMessage(s, ""+str(num1) +" / "+str(num2)+" = ? (two decimal places)")
                                        op = " / "
                                        ans = "{0:.2f}".format(num1 / num2)
                                        return
                                elif (operation == 2):
                                        num1 = random.randint(1,1000)
                                        num2 = random.randint(1,1000)
                                        sendMessage(s, ""+str(num1) +" + "+str(num2)+" = ?")
                                        op = " + "
                                        ans = num1 + num2
                                        return
                                elif (operation == 3):
                                        num1 = random.randint(1,20)
                                        num2 = random.randint(2,9)
                                        sendMessage(s, ""+str(num1) +" ^  "+str(num2)+" = ?")
                                        op = " ^ "
                                        ans = num1**(num2)
                                else:
                                        num1 = random.randint(1,1000)
                                        num2 = random.randint(1,1000)
                                        sendMessage(s, ""+str(num1) +" - "+str(num2)+" = ?")
                                        op = " - "
                                        ans = num1 - num2
                                        return
                        else:
                                global num1
                                global num2
                                global op
                                sendMessage(s, "current: "+str(num1)+op+str(num2)+" = ?")
                                return


def mathAnswer(msg,user):
        global ans
       # print("answer: "+str(ans))
        if " "+str(ans)+" " in msg or " "+str(ans) in msg or str(ans)+" " in msg or str(ans) == msg:
                sendMessage(s, user + " got the right answer: "+str(ans))
                ans = 1273982173871289378912738912879389127389718293789217
                return
                        
                        

#league shit
# to get ID -> https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/<SUMMONER NAME>?api_key=de76537c-262a-48fe-b6fd-ba75e40311a6
# current game -> https://na.api.pvp.net/observer-mode/rest/consumer/getSpectatorGameInfo/NA1/<SUMMONER ID>?api_key=de76537c-262a-48fe-b6fd-ba75e40311a6
# ranked stats -> https://na.api.pvp.net/api/lol/na/v1.3/stats/by-summoner/<SUMMONER ID>/ranked?season=SEASON2016&api_key=de76537c-262a-48fe-b6fd-ba75e40311a6                        
                        
#regex shit
# http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))

def islink(msg,user):
        if re.match('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))',msg) :
                #print("is a link")
                return True
        else:
                #print("not a link")
                return False
def finger(msg,user):
        if "!finger" == msg.split(" ")[0]: 
                sendMessage(s,"( ° ͜ʖ͡°)╭∩╮ Hey "+str(user)+" heres a !finger for you ( ° ͜ʖ͡°)╭∩╮")
                return

def noLoogie(msg):
        global timer4sec
        global loogieOff
        global modlist
        if "!loogieoff" == msg.lower() and user.lower() in modlist:
                loogieOff = True
                print("loogies off")
                return
        if "!loogieon" == msg.lower():
                loogieOff = False
                print("loogies on")
                return


def loogie(loogieOff):
        num = random.randint(0,250)
        global loogied
        #print("loogieoff "+str(loogieOff));
        #print(str(num)+" is loogie number")
        if num == 23 and loogied == "-" and (loogieOff == False):
                time.sleep(1.5)
                sendMessage(s, "/me gargles up a huge loogie and takes aim at chat...")
                print("gargles")
                time.sleep(3.5)
                userlist = namesOnly
                print(len(userlist))
                target = random.randint(1,len(userlist)-1)
                i = 0;
                while(i < len(userlist)):
                        if target == i:
                                loogied = userlist[i]
                                loogiedTimer = time.time()
                                global loogiedTimer
                                global loogied
                                break
                        i+= 1
                sendMessage(s, loogied+" has been hit with a loogie and has reduced duel chances for 30 seconds!")


def unloogie(user,msg):
        global loogiedTimer
        global loogied
        if (time.time()-30 > float(loogiedTimer) and loogied != "-") or (user.lower() == loogied and msg.lower() == "wipeoff"):
                time.sleep(1)
                sendMessage(s, loogied+" has finally wiped all the loogie off themselves and is no longer vulnerable")
                time.sleep(1)
                loogied = "-"
                loogiedTimer = "0.0"


def top100(msg, topList):
       if "!top100 " in msg: 
                global timer4sec
                if time.time() > timer4sec +4:
                        timer4sec = time.time()
                        print(datetime.today())
                        rank = int(msg.split(" ")[1])
                        rank = rank - 1
                        if rank > 99 or rank < 0:
                                print("invalid number")
                                return
                        else:
                                song = topList[rank]
                                sendMessage(s, "Current top 100 rank #"+str(rank+1)+" https://www.youtube.com/watch?v="+song)
                                return
def soundcloud(msg):
        if "!randompls" in msg:
                global timer4sec
                if time.time() > timer4sec+4:
                        global client            
                        try:
                                track = client.get('/tracks/%s' % random.randint(0, 1000000000))
                                #tracks = client.get('/tracks')
                                #track = random.choice(tracks)
                                sendMessage(s,"MitchPls "+str(track.permalink_url))
                                return
                        except:
                                print("calling sc again")
                                soundcloud("!randompls")

def timeout(msg,user):
        if "!out " in msg and user.lower() == "yoloswagbruh_":
                target = msg.split(" ")[1]
                time = msg.split(" ")[2]
                sendWhisper(s,"FourTwentyBot", "/timeout "+target+" "+ time)
                return

def banmepls(msg,user):
        if "!banmepls" == msg.split(" ")[0]: 
                sendWhisper(s,"FourTwentyBot", "/timeout "+user+" 1")
                return

def fuckthatkid(user):
        if user.lower() == "i_am_a_pleb__":
                sendWhisper(s,"FourTwentyBot", "/timeout "+str(user)+" 600")
                return


def saythis(msg,user):
        if "!say " in msg and user.lower() == "yoloswagbruh_":
                saying = msg.split("!say ")[1]
                sendMessage(s, saying)
                return
                
        
while True:
        time.sleep(0.1)
        try:
        #while True:
                readbuffer = readbuffer + s.recv(1024).decode('utf-8')
                temp = str.split(readbuffer, "\n")
                readbuffer = temp.pop()
                #print("TEMP IS :"+temp)
                for line in temp:
                        line = str.rstrip(line)
                        #print(line)
                        if(line[0] == "P"):
                                s.send(bytes("PONG %s\r\n" % line[1],"UTF-8"))
                                print("sent ping")
                                break
                        #print("LINE IS:"+line)
                        #line is valid so we can grab user and msg
                        if (line != ":tmi.twitch.tv USERSTATE #"+channel):
                                #print("not userstate ^")
                                user = getUser(line)
                                msg = getMessage(line)
                                now = time.time()
                        #line is not valid so we set user and msg to "-" just in case
                        else:
                                user = "-"
                                msg = "-"
                                
                        if now - updatetime > 100:
                                try:
                                        updatetime = time.time()
                                        response = requests.get("https://tmi.twitch.tv/group/user/"+channel+"/chatters")
                                        readable = response.text
                                        chatlist = loads(readable)
                                        chatters = chatlist['chatters']
                                        updatetime = time.time() +100
                                        namesOnly = (readable.split("moderators\": [")[1]).split("],")[0].strip()+","
                                        namesOnly += (readable.split("staff\": [")[1]).split("],")[0].strip()
                                        namesOnly += (readable.split("admins\": [")[1]).split("],")[0].strip()
                                        namesOnly += (readable.split("global_mods\": [")[1]).split("],")[0].strip()
                                        namesOnly += (readable.split("viewers\": [")[1]).split("]")[0].strip()
                                        namesOnly = re.sub("[!@#$\"'\n\t\"      \"]", '', namesOnly)
                                        namesOnly = namesOnly.split(",")
                                        print("lists updated")
                                except:
                                        pass
                        if (user != "-"):
                                print(user + " says: " + str(msg))
                                
                        leaveChan(msg,user)
                        #fuckthatkid(user)
                        if leave is False and user.lower() not in ignorelist:
                                #noLoogie(msg)
                                #loogie(loogieOff)
                                #unloogie(user,msg)
                                #soundcloud(msg)
                                finger(msg,user)
                                #timeout(msg,user)
                                #banmepls(msg,user)
                                saythis(msg,user)
                                forceUpdate(msg,user)
                                openTrivia(msg, user)
                                top100(msg,topList)
                                #find(msg, user)
                                totalduels(msg)
                                #islink(msg,user)
                                basedgod(msg)
                                follows(msg,user)
                                age(msg,user)
                                top(msg)
                                low(msg)
                                viewbot(msg)
                                mathTrivia(msg)
                                mathAnswer(msg,user)
                                dev(msg)
                                distance(msg)
                                music(msg, index_list)
                                #donate(msg)
                                hunnidk(msg)
                                currTrivia(msg)
                                #heypoke(msg,user)
                                ignore(msg,user)
                                unignore(msg,user)
                                cringe(msg, timer4sec)
                                howeh(msg)
                                ninja(msg)
                                jah(msg)
                                #skip(msg,user,trivia_list)
                                stronk(msg)
                                #yaBaby(msg)
                                grady(msg)
                                spit(user,msg)
                                #tDuel(user, msg)
                                #confirm(msg, goldDict, user)
                                duel(user, channel, msg)
                                winrate(user,msg)
                                winrate2(user,msg)
                                #copygrady(msg,user)
                                #answer2(msg, user, trivia_list)
                                #print("hello end of while, msg: "+msg)
                                #trivia2(msg,trivia_list)
        except Exception as err:
                print(" ")
                e = sys.exc_info()[0]
                print(err)
                print(e)
                print("problem")
                pass




