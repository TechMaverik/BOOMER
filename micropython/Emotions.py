happy=['happy','awesome','cool','pleasant','wonderful','joyful','excited','good','jolly','great','cheerful','greatful','merry','amazing','rocking','cherish','thrilled','light hearted','glowing','blushing']
sad=['sad','terrible','frustrated','angry','not','unhappy','depressed','sorrow','disappointed','ugly','disaster', 'neither', 'nor','grief','regret','down','gloomy','tragic','crying','afraid','negative','aweful','fool','foolish','stupid','dump','dumped','sorry','solitary','alone','dissapointed','unfortunate']
greetings=['hello','hi','hey','bye','good bye','tata','greetings','hai']
water=['water','Water','WATER']



def detect_emotion(data):
    score=[]
    prev=1
    finalscore=0
 
    #converting to list (pre processing)
    dataList=data.split(" ")
    for word in dataList:
        if(word in happy):
            score.append(1)
        elif (word in sad):
            score.append(-1)
        elif (word in greetings):           
            return "greet"
        elif (word in water):           
            return "water"
        


    #print(score)
    for x in score:
        finalscore=x*prev
        prev=x

    if(finalscore<0):
        return(False)
    elif(finalscore>0):
        return(True)
    else:
        return("idle")



